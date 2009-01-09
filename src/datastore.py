# Separate module for keeping track of data over the long-run in files
import inputs
import pickle
import linalg

def store(population, generation, trial_ID):
    store_as_pickles(population, generation, trial_ID)
    store_fitnesses (population, generation, trial_ID)
    store_freevar_count(population,generation, trial_ID)
    print_out_heroes(population, generation, trial_ID)

def store_as_pickles(population, generation, trial_ID):
    # Pickle as a .pkp (pickled population)
    #pickle.dump(population, 
    #        "../dat/" + str(trial_ID) + "." + str(generation) + ".pkp")
    pass

def store_freevar_count(population, generation, trial_ID):
    if generation > 0:
        return
    frees = [len(linalg.determineFreeVariables(o['constraints'])) 
            for o in population]
    counts = {}
    for free in frees:
        counts[free] = counts.get(free,0) + 1
    vars = counts.keys()
    for v in counts.values():
        if not v in range(len(o['constraints'])):
            raise "hell"
    F = open("../dat/" + str(trial_ID) + ".fre", "a")
    F.writelines([ ",".join([str(counts.get(i,0)) 
             for i in range(len(o['constraints']))]) + '\n' ])
    F.close()

def store_fitnesses(population, generation, trial_ID):
    fits = [float(o['fitness']) for o in population]
    fits.sort()
    F = open("../dat/" + str(trial_ID) + ".fit", "a")
    F.writelines([ ",".join([str(ele) for ele in fits]) + '\n' ])
    F.close()


def print_out_heroes(population, generation, trial_ID):
    print "Trial: ", trial_ID, " Generation: ", generation
    print "Hero: "
    for o in [population[-1]]:
        print "Organism", population.index(o)
        print o['fitness']
        print inputs.input_to_string(o['input'])
        #for row in o['constraints']:
        #    print "", row

