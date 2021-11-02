import scipy.optimize as opt

def fun(y, sign, V):
    return sign * y[V]

def do_max(a,b):
    print("V -> max:")
    cons = ({
                'type': 'ineq',
                'fun': lambda t: b*t[0] + b*t[1] - b*t[2] - a*t[3] - t[4]
            },
            {
                'type': 'ineq',
                'fun': lambda t: a*t[0] + a*t[2] - t[4]
            },
            {
                'type': 'eq',
                'fun': lambda t: t[0] + t[1] + t[2] + t[3] - 1 
            })

    bnc = ((0, None),(0, None),(0, None),(0, None),(None, None))
    res = opt.minimize(fun, x0=(1, 1, 1, 1, 1), args=(-1, 4), method='SLSQP', constraints=cons, bounds=bnc, options={'ftol': 1e-7})
    print(res)

def do_min(a,b):
    print("V -> min:")
    cons = ({
                'type': 'ineq',
                'fun': lambda t: t[2] - b*t[0] - a*t[1]
            },
            {
                'type': 'ineq',
                'fun': lambda t: t[2] - b*t[0]
            },
            {
                'type': 'ineq',
                'fun': lambda t: t[2] + b*t[0] - a*t[1]
            },
            {
                'type': 'ineq',
                'fun': lambda t: t[2] + a*t[0]
            },
            {
                'type': 'eq',
                'fun': lambda t: t[0] + t[1] - 1 
            })

    bnc = ((0, None),(0, None),(None, None))

    res = opt.minimize(fun, x0=(1, 1, 1), method='SLSQP', args=(1, 2), constraints=cons, bounds=bnc, options={'ftol': 1e-7})
    print(res)

if __name__=="__main__":
    a = int(input("Введите первую ставку) a = "));
    b = int(input("Введите вторую ставку) b = "));
    do_max(a,b)
    print('\n\n')
    do_min(a,b)'