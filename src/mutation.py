
from random import random, randint

# Some constants:
mutation_rate = 0.02

# Only have the most basic mutation for now.
def mutation( org, force=False ):
    o = [ele for ele in org['org'][0]]
    r_test = random()
    if r_test < mutation_rate or force:
        r = randint(0, 5)
        if r == 0:
            # Reassign a random index to a random value between -1 and 1
            o[randint(0,len(o)-1)] = random()*2-1
        elif r == 1:
            # Insert a random index with a -1 to 1 value
            o.insert(randint(0,len(o)-1), random()*2-1)
        elif r == 2:
            # Remove a random element
            if len(o) > 1:
                o.pop(randint(0, len(o)-1))
        elif r == 3:
            # Nudge a random element
            i = randint(0, len(o)-1)
            o[i] = o[i] + (random() * 0.1) - 0.05
        elif r == 4:
            # Replace the amplitude
            org['amplitude'] = random() * 0.2
        elif r == 5:
            # Replace the amplitude
            org['amplitude'] = org['amplitude'] + ((random() * 0.01) - 0.005)
            if org['amplitude'] < 0:
                org['amplitude'] = random() * 0.2
        else:
            raise "Impossible!"

        # Reassign:
        org['org'] = [o,[0,0,0]]
    return org

fn_list = [mutation]
