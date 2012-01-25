from random import randint

import metrics   as mtr
import crossover as cvr
import mutation  as mut

def four_indices( num ):
    indices = []
    for i in xrange(4):
        index = randint(0,num-1)
        while index in indices:
            index = randint(0,num-1)
        indices.append(index)
    return indices


def non_greedy_selection(population, crossover_fnc, cmp_fnc):
    indices = four_indices(len(population))

    parents = [population[indices[i]] for i in range(4)]
    parents.sort(lambda x,y : mtr.comparator(x,y,cmp_fnc))

    winner1, winner2 = parents[0], parents[1]
    loser1, loser2   = parents[2], parents[3]

    # Fitness is measured before crossover is complete and automatically
    #  cached in a tuple.  child1 and child2 should be tuples now.
    child1, child2 = cvr.crossover(winner1, winner2, crossover_fnc)

    # Mutate (if the check passes)
    child1 = mut.mutation(child1)
    child2 = mut.mutation(child2)

    # Replace the losers from selection
    population[population.index(loser1)] = child1
    population[population.index(loser2)] = child2

    return population

def greedy_selection(population, crossover_fnc, cmp_fnc):
    indices = four_indices(len(population))

    parents = [population[indices[i]] for i in range(4)]
    parents.sort(lambda x,y : mtr.comparator(x,y,cmp_fnc))

    winner1, winner2 = parents[0], parents[1]

    # Fitness is measured before crossover is complete and automatically
    #  cached in a tuple.  child1 and child2 should be tuples now.
    child1, child2 = cvr.crossover(winner1, winner2, crossover_fnc)

    # Mutate (if the check passes)
    child1 = mut.mutation(child1)
    child2 = mut.mutation(child2)

    # Add the children, resort, remove the worst 2
    population.append(child1)
    population.append(child2)
    population.sort(lambda x,y : mtr.comparator(x,y,cmp_fnc))
    population = population[:-2]

    return population

def mutant_hero(population, crossover_fnc, cmp_fnc):
    hero = population[0]
    hero_o = hero['org'][0]
    hero_a = hero['amplitude']
    child_o = [ele for ele in hero_o]
    child_o = [child_o, [0,0,0]]
    child = {'org' : child_o, 'amplitude' : hero_a}
    child = mut.mutation(child, True)
    population.append(child)
    population.sort(lambda x,y : mtr.comparator(x,y,cmp_fnc))
    population = population[:-1]
    return population

def non_greedy_mutant_hero(population, crossover_fnc, cmp_fnc):
    population = non_greedy_selection(population, crossover_fnc, cmp_fnc)
    population = mutant_hero(population, crossover_fnc, cmp_fnc)
    return population

def greedy_mutant_hero(population, crossover_fnc, cmp_fnc):
    population = greedy_selection(population, crossover_fnc, cmp_fnc)
    population = mutant_hero(population, crossover_fnc, cmp_fnc)
    return population

fn_list = [non_greedy_selection, greedy_selection, greedy_mutant_hero, non_greedy_mutant_hero, mutant_hero]
