#!/usr/bin/python

from random import gauss, randint, random

from fourier import fft, ifft, nextpow2

# Returns two complimentary children
def crossover( org1, org2, crossover_fnc ):
    return crossover_fnc(org1, org2)

def piecewise_smash(number):
    if number > 1:
        return 1
    elif number < -1:
        return -1
    return number

# Unpack and repack are used by every crossover function below.
def unpack(org1, org2):
    o1, o2 = org1['org'][0], org2['org'][0]
    a1, a2 = org1['amplitude'], org2['amplitude']
    return o1, o2, a1, a2

def repack(c1, c2, a1, a2):
    c1 = [piecewise_smash(ele) for ele in c1]
    c2 = [piecewise_smash(ele) for ele in c2]

    child1 = [c1,[0,0,0]]
    child2 = [c2,[0,0,0]]

    mean = (a1 + a2) / 2.0
    std = abs(a1-mean)

    c1 = { 'org' : child1, 'amplitude' : abs(gauss(mean, std)) }
    c2 = { 'org' : child2, 'amplitude' : abs(gauss(mean, std)) }
    return c1, c2


def _fixed_single_point(o1, o2):
    p1 = int(len(o1)/2.0)
    p2 = int(len(o2)/2.0)
    c1 = o1[:p1] + o2[p2:]
    c2 = o2[:p2] + o1[p1:]
    return c1, c2
def _random_single_point(o1, o2):
    p1 = randint(0, len(o1)-1)
    p2 = randint(0, len(o2)-1)
    c1 = o1[:p1] + o2[p2:]
    c2 = o2[:p2] + o1[p1:]
    return c1, c2
def _gaussian_merge(o1, o2, child_len):
    mean = [(o1[i % len(o1)] + o2[i % len(o2)]) / 2.0 for i in range(child_len)]
    stds = [abs(o1[i % len(o1)] - mean[i])            for i in range(child_len)]
    #  Randomly select based on distribution of the parents
    c1   = [gauss(mean[i], stds[i])                   for i in range(child_len)]
    #  Make c2 complimentary to c1
    c2   = [2*mean[i] - c1[i]                         for i in range(child_len)]
    return c1, c2

def fft_unpack(org1, org2):
    o1, o2, a1, a2 = unpack(org1, org2)

    avg_len = (len(o1) + len(o2))/2.0
    std_len = abs(len(o1) - avg_len)

    child_len = -1
    while (child_len < 1):
        child_len = int(abs(gauss( avg_len, std_len )))

    # Find the next power of 2 greater than the longest length
    if len(o1) > len(o2):
        pow = nextpow2(len(o1))
    else:
        pow = nextpow2(len(o2))

    # Deep copy
    tmp1 = [ele for ele in o1]
    tmp2 = [ele for ele in o2]
    # Zero-pad
    tmp1.extend([0 for i in range(pow - len(tmp1))])
    tmp2.extend([0 for i in range(pow - len(tmp2))])
    o1, o2 = tmp1, tmp2

    o1 = fft(o1)
    o2 = fft(o2)

    return avg_len, std_len, child_len, pow, o1, o2, a1, a2

def fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2):
    # Zero-pad c1 and c2 if necessary
    c1.extend([0 for i in range(nextpow2(len(c1)) - len(c1))])
    c2.extend([0 for i in range(nextpow2(len(c2)) - len(c2))])

    # Invert fft
    c1   = ifft(c1)
    c2   = ifft(c2)

    #print "Truncated"
    c1 = c1[:child_len]
    c2 = c2[:child_len]
    # TODO -- try interpolating back down to a smaller (child_len) size?
    #print "fft crossover from:", \
    #        len(org1['org'][0]), len(org2['org'][0]), \
    #        "to", len(c1), len(c2)

    # Get rid of imaginary components...
    c1 = [ele.real for ele in c1]
    c2 = [ele.real for ele in c2]

    c1, c2 = repack(c1, c2, a1, a2)
    return c1, c2

precision = 64
def _binarize(num):
    num = int(abs(num * 2**precision))
    result = []
    for i in range(precision, -1, -1):
        if num - 2**i >= 0:
            num = num - 2**i
            result.append(1)
        else:
            result.append(0)
    return result

def binarize(nums):
    result = []
    for ele in nums:
        b_num = _binarize((ele+1.0)/2.0)
        result.extend(b_num)
    return result

def _unbinarize(num):
    res = 0
    for i in range(precision):
        if num[i]:
            res = res + 2**(precision-i)
    return res

def unbinarize(nums):
    result = []
    for i in range(0, len(nums), precision+1):
        seq = nums[i:i+precision+1]
        if len(seq) < precision+1:
            seq.extend([0 for ele in range(precision+1-len(nums[i:]))])
        result.append(_unbinarize(seq))
    return [(2*(ele / float(2**precision)))-1  for ele in result]

#case = [random()*2-1 for i in range(10)]
#print case
#back = unbinarize(binarize(case))
#err = [ abs(case[i] - back[i]) for i in range(len(case))]
#print err
#print sum(err)


def fixed_single_point(org1, org2):
    o1, o2, a1, a2  = unpack(org1, org2)
    c1, c2          = _fixed_single_point(o1, o2)
    c1, c2          = repack(c1, c2, a1, a2)
    return [c1, c2]
def random_single_point(org1, org2):
    o1, o2, a1, a2  = unpack(org1, org2)
    c1, c2          = _random_single_point(o1, o2)
    c1, c2          = repack(c1, c2, a1, a2)
    return [c1, c2]
def gaussian_merge(org1, org2):
    o1, o2, a1, a2 = unpack(org1, org2)
    avg_len = (len(o1) + len(o2))/2.0
    std_len = abs(len(o1) - avg_len)
    child_len = -1
    while (child_len < 1):
        child_len = int(abs(gauss( avg_len, std_len )))
    c1, c2 = _gaussian_merge(o1, o2, child_len)
    c1, c2 = repack(c1, c2, a1, a2)
    return [c1, c2]
def binary_random_single_point(org1, org2):
    o1, o2, a1, a2 = unpack(org1, org2)
    c1, c2 = binarize(o1), binarize(o2)
    c1, c2 = _random_single_point(c1, c2)
    c1, c2 = unbinarize(c1), unbinarize(c2)
    c1, c2 = repack(c1, c2, a1, a2)
    return [c1, c2]
def binary_fixed_single_point(org1, org2):
    o1, o2, a1, a2 = unpack(org1, org2)
    c1, c2 = binarize(o1), binarize(o2)
    c1, c2 = _fixed_single_point(c1, c2)
    c1, c2 = unbinarize(c1), unbinarize(c2)
    c1, c2 = repack(c1, c2, a1, a2)
    return [c1, c2]
def fft_random_single_point(org1, org2):
    avg_len, std_len, child_len, pow, o1, o2, a1, a2 = fft_unpack(org1, org2)
    c1, c2 = _random_single_point(o1, o2)
    c1, c2 = fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2)
    return [c1, c2]
def fft_fixed_single_point(org1, org2):
    avg_len, std_len, child_len, pow, o1, o2, a1, a2 = fft_unpack(org1, org2)
    c1, c2 = _fixed_single_point(o1, o2)
    c1, c2 = fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2)
    return [c1, c2]
def fft_gaussian_merge(org1, org2):
    avg_len, std_len, child_len, pow, o1, o2, a1, a2 = fft_unpack(org1, org2)
    c1, c2 = _gaussian_merge(o1, o2, pow)
    c1, c2 = fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2)
    return [c1, c2]
def fft_binary_random_single_point(org1, org2):
    avg_len, std_len, child_len, pow, o1, o2, a1, a2 = fft_unpack(org1, org2)
    c1, c2 = binarize(o1), binarize(o2)
    c1, c2 = _random_single_point(c1, c2)
    c1, c2 = unbinarize(c1), unbinarize(c2)
    c1, c2 = fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2)
    return [c1, c2]
def fft_binary_fixed_single_point(org1, org2):
    avg_len, std_len, child_len, pow, o1, o2, a1, a2 = fft_unpack(org1, org2)
    c1, c2 = binarize(o1), binarize(o2)
    c1, c2 = _fixed_single_point(c1, c2)
    c1, c2 = unbinarize(c1), unbinarize(c2)
    c1, c2 = fft_repack(avg_len, std_len, child_len, pow, c1, c2, a1, a2)
    return [c1, c2]


fn_list = [
    random_single_point,
    fixed_single_point,
    gaussian_merge,
    binary_random_single_point,
    binary_fixed_single_point,
    fft_random_single_point,
    fft_fixed_single_point,
    fft_gaussian_merge,
    fft_binary_random_single_point,
    fft_binary_fixed_single_point
    ]
