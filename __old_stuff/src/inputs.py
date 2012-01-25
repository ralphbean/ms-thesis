#!/usr/bin/python
from random import random, randint

lor = ['left', 'right']
ops = { '^' : (lambda x,y : x**y),
        '*' : (lambda x,y : x * y),
        '/' : (lambda x,y : x / y),
        '+' : (lambda x,y : x + y),
        '-' : (lambda x,y : x - y)}

def deep_copy(node):
    new_node = {}
    for k,v in node.iteritems():
        if type(v) == dict:
            new_node[k] = deep_copy(v)
        else:
            new_node[k] = v
    return new_node

def attach_at(root, c_p1, c_p2):
    if c_p1 == None:
        return deep_copy(c_p2)
    if c_p1 == root:
        root[lor[randint(0,1)]] = deep_copy(c_p2)
        return deep_copy(root)

    new_root = {'type':root['type'],'value':root['value']}
    if 'left' in root and 'right' in root:
        new_root['left']  = attach_at(root['left'], c_p1, c_p2)
        new_root['right'] = attach_at(root['right'], c_p1, c_p2)
    return new_root

def get_parent_of(root, c_p):
    if c_p == None:
        raise "Cannot find parent of None."
    if root == None:
        raise "None cannot have a child."
    if not 'left' in root and not 'right' in root:
        return None
    if root['left'] == c_p:
        return root
    if root['right'] == c_p:
        return root
    left_check = get_parent_of(root['left'], c_p)
    if left_check:
        return left_check
    right_check = get_parent_of(root['right'], c_p)
    if right_check:
        return right_check
    return None

def random_crossover_point(root):
    # Are we at a leaf, and by default, are we forced to choose this node?
    if not 'left' in root and not 'right' in root:
        return root
    # Should we keep diving?
    if random() < 0.5:
        return random_crossover_point(root[lor[randint(0,1)]])
    # Or should we choose this as the node?
    return root

def number_of_nodes(root):
    if root == None:
        return 0
    if 'left' in root:
        return number_of_nodes(root['left'])+number_of_nodes(root['right'])+1
    return 1

def crossover(i1, i2):
    p1, p2 = deep_copy(i1['eqn']), deep_copy(i2['eqn'])
    r_point1 = random_crossover_point(p1)
    c_point1 = get_parent_of(p1, r_point1)
    c_point2 = random_crossover_point(p2)
    final = deep_copy(i1['eqn'])
    eqn = attach_at(final, c_point1, c_point2) 

    r = random()
    dx = i1['dx']*r + (1-r)*i2['dx']

    return {'dx' : dx, 'eqn' : eqn}

def mutate(input):
    input['eqn'] = _mutate(input['eqn'])
    return input

# One of a few mutation operations:
def _mut_replace_node(root):
    del root
    return build_random_function()

# Another mutation operation:
def _mut_by_type(root):
    chance = random()
    if root['type'] == 'operator':
        # Change the operator
        root['value'] = ops.keys()[randint(0,len(ops.keys())-1)]
    elif root['type'] == 'parameter':
        # We only have one type of parameter... so nothing to do here.
        pass
    elif root['type'] == 'constant':
        root['value'] = str(float(root['value'])*(random()*2)+(random()*2-1))
    else:
        raise ValueError, "Undefined data type in _mutate."
    return root
# Note:  -- need to list all the mutation operations here
mut_fncs = [_mut_replace_node, _mut_by_type]

# This function uses all the mutation operations listed above.
def _mutate(root):
    if 'left' in root and 'right' in root:
        # Traverse children or mutate here?
        if random() < 0.5:
            i = randint(0,1)
            root[lor[i]] = _mutate(root[lor[i]])
            return root

    # Otherwise, we are mutating at this node.
    # Select from all the different types of mutations
    i = randint(0, len(mut_fncs)-1)
    return mut_fncs[i](root)

# Takes a tree as a dictionary and prints its nodes inorder
def tree_to_inorder_string(root):
    retval = ""
    if ( len(root.keys()) > 1 ):
        retval = retval + "("

    if ( root.__contains__('left') ):
        retval = retval + tree_to_inorder_string(root['left'])

    if root['type'] == 'operator':
        retval = retval + root['value']
    elif root['type'] == 'parameter':
        retval = retval + "a_{" + root['value'] + "}"
    elif root['type'] == 'constant':
        retval = retval + root['value']
    else:
        raise ValueError, "Undefined data type in inorder traversal."

    if ( root.__contains__('right') ):
        retval = retval + tree_to_inorder_string(root['right'])
    if ( len(root.keys()) > 1 ):
        retval = retval + ")"

    return retval


# Takes the dictionary structure of a system input and prints it in
#  human-readable form
def input_to_string( input ):
    s = "dx = " + str(input['dx'])
    s = s + " f(a_{0}) = " + tree_to_inorder_string(input['eqn'])
    return s

def function_as_lambda(func):
    if func['type'] == 'operator':
        left = function_as_lambda(func['left'])
        righ = function_as_lambda(func['right'])
        return lambda x : ops[func['value']](left(x),righ(x))
    elif func['type'] == 'parameter':
        return lambda x : float(x)
    elif func['type'] == 'constant':
        return lambda x : float(func['value'])
    else:
        raise "Malformed function."

def input_as_lambdas(input):
    t = lambda v, c : v[0] + float(input['dx'])
    f = lambda v, c : function_as_lambda(input['eqn'])(v[0])
    return [t,f]

def build_random_function():
    choice = randint(0,2)
    node = {}
    if choice == 0:
        # Only doing 1 dimensional.  So there is only one parameter.
        node['type'] = 'parameter'
        node['value'] = str(0)
    elif choice == 1:
        node['type'] = 'constant'
        node['value'] = str((random()*10)-5)
    else:
        node['type'] = 'operator'
        operators = ['^', '*', '/', '+', '-']
        node['value'] = operators[randint(0,4)]
        node['left'] = build_random_function()
        node['right'] = build_random_function()
    return node

def build_random_input():
    input = {}
    input['dx'] = random()
    input['eqn'] = build_random_function()
    return input

def mad_test():
    while True:
        print
        i1 = build_random_input()
        i2 = build_random_input()
        print "Before1:", input_to_string(i1)
        print "Before2:", input_to_string(i2)
        child = crossover(i1,i2)
        print "After1: ", input_to_string(i1)
        print "After2: ", input_to_string(i2)
        print "Child:  ", input_to_string(child)

