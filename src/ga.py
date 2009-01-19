#!/usr/bin/python

import inputs, datastore, simulator
import constraints as constr
import constants
from math import sqrt, log, fabs

import sys, time
from random import random, randint

# A metric of the diversity of the population.
# If every individual is the same, the value is 0
#  ( Treat each individual as a Q-dimensional vector,
#    elements are the entries in the constraint matrix
#    as well as a few samplings of their input f(x) )
#  Use distance formula or some sort of metric I find
#   online.
def diversity(pop):
    # Deal with constraints
    # Specifically, calculate the sum of the distances of every organism from
    #  every other organism.
    c_tot, i_tot = 0,0
    for org in pop:
        for other in pop:
            c_tot = c_tot + constraint_dist(org, other)/(float(len(pop))**2)
            i_tot = i_tot + input_dist(org, other)/(float(len(pop))**2)
    return c_tot, i_tot

def constraint_dist(o1, o2):
    c1, c2 = o1['constraints'], o2['constraints']
    tot = 0
    for r in xrange(len(c1)):
        for c in xrange(len(c2)):
            tot = tot + (c1[r][c] - c2[r][c])**2
    return sqrt(tot)

def input_dist(o1, o2):
    i1, i2 = o1['input'], o2['input']
    eqns1 = inputs.input_as_lambdas(i1)
    eqns2 = inputs.input_as_lambdas(i2)
    syst1 = { 'n' : 2, 'consts' : [], 'eqns' : eqns1 }
    syst2 = { 'n' : 2, 'consts' : [], 'eqns' : eqns2 }
    test_iterates = (constants.num_warmup_iterations +
                     constants.num_measur_iterations )
    x1, x2 = [0,0], [0,0]
    traj1, traj2 = [], []
    for i in xrange(test_iterates):
        traj1.append(x1)
        traj2.append(x2)
        x1 = simulator.iterate(syst1, x1)
        x2 = simulator.iterate(syst2, x2)
    diff = [(fabs(traj1[i][1] - traj2[i][1]))/test_iterates 
                  for i in xrange(len(traj1))]
    dist = log(log(sqrt(sum(diff))+1)+1)
    return dist

def test_input_dist():
    i1 = inputs.build_random_input()
    i2 = inputs.build_random_input()
    print "i1:", inputs.input_to_string(i1)
    print "i2:", inputs.input_to_string(i2)
    print "dist:", input_dist({'input':i1}, {'input':i2})

def crossover(o1, o2):
    mutation_rate = constants.mutation_rate
    o = {}
    o['constraints']=crossover_constraints(o1['constraints'],o2['constraints'])
    o['input']      =crossover_inputs(     o1['input'],      o2['input']      )
    if random() < mutation_rate:
        o = mutate(o)
    o['fitness']    =fitness(o)
    return o

def crossover_constraints(c1, c2):
    r,c = randint(0,len(c1)-1), randint(0,len(c1[0])-1)
    child = [row for row in c1]
    child[r:] = [row for row in c2[r:]]
    child[r][:c] = [ele for ele in c1[r][:c]]
    return child

def crossover_inputs(i1, i2):
    # Let the inputs module handle this.  Its messy.
    return inputs.crossover(i1,i2)


def mutate(o):
    if random() < 0.5:
        o['constraints'] = mutate_constraints(o['constraints'])
    else:
        o['input'] = mutate_input(o['input'])
    return o

def mutate_constraints(constraints):
    r,c = randint(0,len(constraints)-1), randint(0,len(constraints[0])-1)
    constraints[r][c] = constraints[r][c] + ((random() * 4) - 2)
    return constraints

def mutate_input(input):
    # Let the inputs module handle this.  Its messy.
    return inputs.mutate(input)

# TODO -- determine fitness variability with a coded test.
def fitness(o, num_instances=constants.num_instances):
    if 'fitness' in o:
        return o['fitness']
    try:
        nets = constr.instantiate(o['constraints'], o['input'], num_instances)
    except Exception:  # Unsatisfiable set of constraints.
        return -10000000
    lyaps = [simulator.measure_lyapunov(net) for net in nets]

    ### TODO -- maybe consider this?
    ### Weighted sum of lyaps
    #lyaps.sort()
    #weighted_lyaps = [lyaps[i]/(num_instances-i) for i in range(num_instances)]
    #return sum(weighted_lyaps)/num_instances

    ### Or not:
    return sum(lyaps)/num_instances

    ### Or, just look for the best.
    #return max(lyaps)

# Initialize an organism
#  n is the number of neurons in the systems to be represented.
def init_organism(n):
    # Organisms are python dictionaries
    o = {   'constraints' : constr.build_random_constraints(n),
            'input'       : inputs.build_random_input() }
    # Cache the fitness
    o['fitness'] = fitness(o)
    return o

# Initialize a population.
#  N is the number of organisms in the population.
#  n is the number of neurons in networks.
def init_population(N=constants.num_organisms_in_population, 
                    n=constants.num_neurons):
    print "Initializing population.  N =", N, "n =", n
    assert(N >= 4)
    assert(n >= 2)
    pop = []
    for i in xrange(N):
        print "\r%", 100.0*float(i)/N,
        sys.stdout.flush()
        o = init_organism(n)
        while fitness(o) < -25:# -10000000:
            o = init_organism(n)
        pop.append(o)
    print "Done."
    return pop


def selection(population):
    indices = []
    for i in xrange(4):
        index = randint(0,len(population)-1)
        while index in indices:
            index = randint(0,len(population)-1)
        indices.append(index)

    p1, p2 = population[indices[0]], population[indices[1]]
    p3, p4 = population[indices[2]], population[indices[3]]

    if fitness(p1) > fitness(p2):
        winner1, loser1 = p1, p2
    else:
        winner1, loser1 = p2, p1

    if fitness(p3) > fitness(p4):
        winner2, loser2 = p3, p4
    else:
        winner2, loser2 = p4, p3

    # Fitness is measured before crossover is complete and automatically
    #  cached in a tuple.  child1 and child2 should be tuples now.
    child1 = crossover(winner1, winner2)
    child2 = crossover(winner2, winner1)

    ## Only replace losers if children are more fit
    #if ( fitness(child1) > fitness(loser1) ):
    #    population[population.index(loser1)] = child1
    #if ( fitness(child2) > fitness(loser2) ):
    #    population[population.index(loser2)] = child2
    ## Or .. just replace them anyways:
    population[population.index(loser1)] = child1
    population[population.index(loser2)] = child2

    population.sort(lambda x,y : cmp(fitness(x), fitness(y)))

    return population

# Main method.
def run(ID):
    print "Running with ID:", ID
    population = init_population()

    generation = 0
    while ( True ):
        datastore.store(population, generation, ID)
        generation = generation + 1
        population = selection(population)


if __name__ == '__main__':
    ID = int(time.time())
    if len(sys.argv) > 1:
        ID = sys.argv[1]
    run(ID)
    #test_input_dist()

