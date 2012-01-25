#!/usr/bin/python

import pylab


def fmu(x, mu):
    return mu * x * (1 - x)





import sys
import gtk, gobject
import pylab as p
import matplotlib.numerix as nx
import time

print "./dynamical_example.py <MU> | 'bifurc'"

animate_bifurc = False
if sys.argv[1] == 'bifurc':
    animate_bifurc = True
    MU = 2.5
else:
    MU = float(sys.argv[1])

p.figure(figsize=[12,8])
ax = p.subplot(111)
canvas = ax.figure.canvas

# create the initial line
X = nx.arange(-0.2, 1.2, 0.01)
line1, = p.plot(X*0, X, 'b-')
line2, = p.plot(X, X*0, 'b-')
line3, = p.plot(X, fmu(X, MU), 'g-')
line4, = p.plot(X, X, 'b-')
line5, = p.plot(X, X*0+1, 'b-')
line6, = p.plot(X*0+1, X, 'b-')

def calculateXX(XX, MU):
    for i in range(40):
        XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
        XX.append([XX[-1][1], XX[-1][1]])
    return XX
r = 0
XX = calculateXX([[r,r]], MU)
traj, = p.plot(
      [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
p.title('f(x) = mu * x * (1 - x)')


# save the clean slate background -- everything but the animated line
# is drawn and saved in the pixel buffer background
background = canvas.copy_from_bbox(ax.bbox)

def update_line(*args):
    global MU
    try:
        canvas.restore_region(background)
        ax.draw_artist(line1)
        ax.draw_artist(line2)
        ax.draw_artist(line4)
        ax.draw_artist(line5)
        ax.draw_artist(line6)
       
        if animate_bifurc:
            r = 0.1
            MU = 2.5 + ((update_line.cnt/4.0)) / 400.0
            if MU > 4:
                MU = 4
            print "\r%f" % MU,
            sys.stdout.flush()
        else:
            r = (nx.sin((update_line.cnt+600.0) / 400.0) + 1)\
                    / 2.0 * 1.02 - 0.01
        XX = calculateXX([[r,r]], MU)
        traj.set_xdata([ele[0] for ele in XX])
        traj.set_ydata([ele[1] for ele in XX])

        line3.set_ydata(fmu(X, MU))
        ax.draw_artist(line3)
        ax.draw_artist(traj)
        
        canvas.blit(ax.bbox)



        update_line.cnt += 1
    except AssertionError:
        pass # Really.. let it go.

    return True
update_line.cnt = 0

gobject.idle_add(update_line)
p.show()

sys.exit(1)



pylab.title( "f(x) = 2.5 x (1-x)")
pylab.plot(
        X, [fmu(ele,MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-')
pylab.show()

from random import random
r = random()
r = 0.15
pylab.ion()
pylab.title( "f(x) = 2.5 x (1-x) : 1 iteration")
pylab.hold(True)
pylab.axes()
pylab.plot(
            X, [fmu(ele, MU) for ele in X], 'b-',
            X, X, 'g-',
            X, [0 for ele in X], 'b-',
            [0 for ele in X], X, 'b-')
for r in pylab.arange(-0, 1, 0.01):
    pass
    #pylab.show()
sys.exit(1)

for i in range(5):
    XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
    XX.append([XX[-1][1], XX[-1][1]])

pylab.title( "f(x) = 2.5 x (1-x) : 5 iterations")
pylab.plot(
        X, [fmu(ele, MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-',
        [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
pylab.show()




for i in range(500):
    XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
    XX.append([XX[-1][1], XX[-1][1]])

pylab.title( "f(x) = 2.5 x (1-x)  :  500 iterations")
pylab.plot(
        X, [fmu(ele, MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-',
        [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
pylab.show()


MU = 4
XX = [[r,r]]

for i in range(1):
    XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
    XX.append([XX[-1][1], XX[-1][1]])

pylab.title( "f(x) = " + str(MU) + " x (1-x) : 1 iteration")
pylab.plot(
        X, [fmu(ele, MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-',
        [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
pylab.show()

for i in range(10):
    XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
    XX.append([XX[-1][1], XX[-1][1]])

pylab.title( "f(x) = " + str(MU) + " x (1-x) : 10 iterations")
pylab.plot(
        X, [fmu(ele, MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-',
        [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
pylab.show()
for i in range(500):
    XX.append([XX[-1][0], fmu(XX[-1][0], MU)])
    XX.append([XX[-1][1], XX[-1][1]])

pylab.title( "f(x) = " + str(MU) + " x (1-x) : 500 iterations")
pylab.plot(
        X, [fmu(ele, MU) for ele in X], 'b-',
        X, X, 'g-',
        X, [0 for ele in X], 'b-',
        [0 for ele in X], X, 'b-',
        [ele[0] for ele in XX], [ele[1] for ele in XX], 'r-')
pylab.show()
