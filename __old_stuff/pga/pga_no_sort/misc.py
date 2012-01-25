import math
# Negative results
def display_orbit(input, amplitude=0.000001):
    import matplotlib.pyplot
    import pylab

    # Compare the power spectral density functions of the system with and
    #  without the input sequence.
    x = [0.4, 0.6]
    X = []
    for i in range(warmups):
        x = network(x)
        x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
        x[1] = x[1] + ( amplitude * input[1][i % len(input[1])] )
    for i in range(measure):
        X.append(x[0])
        x = network(x)
        x[0] = x[0] + ( amplitude * input[0][i % len(input[0])] )
        x[1] = x[1] + ( amplitude * input[1][i % len(input[1])] )
    pylab.subplot(2,1,1)
    matplotlib.pyplot.psd(X,1024,32)

    x = [0.4, 0.6]
    X = []
    for i in range(warmups):
        x = network(x)
        # x[0] = x[0] + ( amplitude * input[i % len(input)] )
    for i in range(measure):
        X.append(x[0])
        x = network(x)
        # x[0] = x[0] + ( amplitude * input[i % len(input)] )
    pylab.subplot(2,1,2)
    matplotlib.pyplot.psd(X,1024,32)

    pylab.show()


def test_lyapunov():
    # This is a key diagram:
    num_steps = 500.
    do_squeezer = False
    input = load_special_input()
    for i in range(1, num_steps):
        mu = float(i)/num_steps
        seed = [mu, 0.6]
        #syst = lambda x : logistic( x, 4 )
        syst = lambda x : network( x )
        print mu, lyapunov(input, syst, seed)

def arange(start, stop, step):
    top = int(math.ceil(stop/float(step)))
    return [i*step for i in range(top)]
