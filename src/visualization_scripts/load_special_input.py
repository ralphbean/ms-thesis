#!/usr/bin/python

import shelve
import pynotify

def load_special_input():
    pynotify.init("foo")

    # big pops are 1238458193.52700.pop
    #          and 1238453879.56300.pop
    pop = shelve.open("dat/1238458193.52700.pop")['pop']
    #pop = shelve.open("dat/1238453879.56300.pop")['pop']

    print pop[0]['fitness']
    input = pop[0]['org']

    #input = [[-1,1,1,1],[1,1,1,1]]

    n = pynotify.Notification("Input loaded.", str(input))
    n.show()

    return input


