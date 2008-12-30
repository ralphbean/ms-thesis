#!/usr/bin/python

import inputs, datastore, simulator
import constraints as constr

import sys, time
from random import random, randint

# A metric of the diversity of the population.
# If every individual is the same, the value is 0
#  ( Treat each individual as a Q-dimensional vector,
#    elements are the entries in the constraint matrix
#    as well as a few samplings of their input f(x) )
#  Use distance formula or some sort of metric I find
#   online.
def diversity(population):
    pass


def crossover(o1, o2):
    mutation_rate = 0.02
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

def fitness(o):
    if 'fitness' in o:
        return o['fitness']

    num_instances = 2

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
def init_population(N=4, n=10):
    print "Initializing population.  N =", N, "n =", n
    assert(N >= 4)
    assert(n >= 2)
    pop = []
    for i in range(N):
        print "\r%", 100.0*float(i)/N,
        sys.stdout.flush()
        pop.append(init_organism(n))
    print "Done."
    return pop


def selection(population):
    indices = []
    for i in range(4):
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

    # Only replace losers if children are more fit
    if ( fitness(child1) > fitness(loser1) ):
        population[population.index(loser1)] = child1
    if ( fitness(child2) > fitness(loser2) ):
        population[population.index(loser2)] = child2

    population.sort(lambda x,y : cmp(fitness(x), fitness(y)))

    return population

# Main method.
def run():
    ID = int(time.time())
    print "Running with ID:", ID
    population = init_population(100,2)
    generation = 0
    while ( True ):
        datastore.store(population, generation, ID)
        generation = generation + 1
        population = selection(population)

if __name__ == '__main__':
    run()

