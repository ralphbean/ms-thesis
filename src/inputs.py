from random import random, randint

ops = { '^' : (lambda x,y : x**y),
        '*' : (lambda x,y : x * y),
        '/' : (lambda x,y : x / y),
        '+' : (lambda x,y : x + y),
        '-' : (lambda x,y : x - y)}

# TODO - crossover
def crossover(i1, i2):
    return i1

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
            lor = ['left', 'right']
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
    s = "f(a_{0}) = " + tree_to_inorder_string(input['eqn'])
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
    t = lambda v, c : v[0] + input['dx']
    f = lambda v, c : function_as_lambda(input['eqn'])(v[0])
    return [t,f]

def build_random_function():
    choice = randint(0,3)
    node = {}
    if choice == 0:
        node['type'] = 'operator'
        operators = ['^', '*', '/', '+', '-']
        node['value'] = operators[randint(0,4)]
        node['left'] = build_random_function()
        node['right'] = build_random_function()
    elif choice == 1:
        # Only doing 1 dimensional.  So there is only one parameter.
        node['type'] = 'parameter'
        node['value'] = str(0)
    else:
        node['type'] = 'constant'
        node['value'] = str((random()*10)-5)
    return node

def build_random_input():
    input = {}
    input['dx'] = 1 #random()
    input['eqn'] = build_random_function()
    # TODO -- remove temporarily disabled random functions.
    #input['eqn'] = { 'type' : 'constant', 'value' : '0' }
    return input

