

x, mu, b    = var('x, mu, b');

def sarkovskii(f, the_var, verbose=False):
    print "Working with function f=="
    print f
    fixed_points = solve(f==the_var, the_var, explicit_solution=True)
    print "f has", len(fixed_points), "fixed point(s):"
    if verbose:
        for pt in fixed_points:
            print pt

    period_two = solve(f(f)==the_var, the_var, explicit_solution=True)
    if verbose:
        print "f has", len(period_two), "orbit(s) of period two."
    prime_period_two = [s for s in period_two if s not in fixed_points]
    print "f has", len(prime_period_two), "orbit(s) of prime period two."
    if verbose:
        for pt in prime_period_two:
            print pt

    period_three = solve(f(f(f))==the_var, the_var, explicit_solution=True)
    if verbose:
        print "f has", len(period_three), "orbit(s) of period three."
    prime_period_three = [s for s in period_three if s not in period_two]
    print "f has", len(prime_period_three), "orbit(s) of prime period three."
    if verbose:
        for pt in prime_period_three:
            print pt

    if verbose:
        print "By sarkovskii's theorem, if f has an orbit of prime period"
        print " three, then f has orbits of every other prime period (and is"
        print " therefore chaotic)."


eq = 2^x
f(x,mu,b) = (e^(mu*x+b) - e^(-(mu*x+b)))/(e^(mu*x+b) + e^(-(mu*x+b)))
f(x,mu,b) = e^(mu*x+b)
f(x,mu,b) = (mu*x+b)^2
sarkovskii(f, x, True)

