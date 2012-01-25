#!/usr/bin/python

import crossover, metrics, selection, sys

def get_name_of_experiment(ID):
    name = str(metrics.fn_list[int(ID[0])])[10:-15] + " "
    name = name + str(crossover.fn_list[int(ID[2])])[10:-15] + " "
    name = name + str(selection.fn_list[int(ID[4])])[10:-15] + " "
    name = name + " Trial:" + ID[6]
    return name

if __name__ == '__main__':
    print get_name_of_experiment(sys.argv[1])
