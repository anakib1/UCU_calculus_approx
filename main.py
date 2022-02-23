from itsdangerous import exc
import numpy as np 
from matplotlib import pyplot as plt

def show_graph(func, l = -4, r = 4, p = 1e-4): 
    """
    Shows graph of function func in segment [l; r] with precision p.
    Default parametrs are chosen to give most unerstandable graph.
    """
    x = np.arange(l,r, p) 
    y = func(x)
    plt.title("Graph") 
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.plot(x,y) 
    plt.show()

def dx_sin(n):
    """
    Returns n-th derivative of sin.
    """
    if n % 2 == 0:
        return 0
    if n % 4 == 1:
        return 1
    return -1

def taylor_for_sin(n, a):
    """
    Finds taylor series of sin(ax).
    Returns numpy polinomial.
    """
    coefs = []
    fact = 1
    pw = 1
    for i in range(n):
        if i > 0: 
            fact *= i
            pw *= a
        coefs.append(pw * dx_sin(i)/fact)

    return np.polynomial.Polynomial(coefs)

def taylor_for_sin3(n):
    """
    Returns series for sin^3(x) using known formula. 
    Returns numpy polinomial
    """

    z = (3 * taylor_for_sin(n, 2) - taylor_for_sin(n, 6)) /4 
    #z = taylor_for_sin(n, 1)
    return z

def compare_at_point(x, n):
    """
    Returns absoulte difference between sin(x)^3 from numpy and my series expansion.
    """
    my_series = taylor_for_sin3(n)
    return abs(np.sin(x)**3 - my_series(x))

def get_number_of_powers(eps, x = 3):
    """
    Returns minimum number of coefs in series to get desired preicsion <eps>.
    If number is more than 101 than returns None
    """
    l = 1
    r = 1001
    while r - l > 1:
        m = (l + r)//2
        if compare_at_point(x, m) > eps:
            l = m
        else:
            r = m
    if compare_at_point(x, m) <= eps:
        return l
    if compare_at_point(x, m) > eps:
        return None
    return r



if __name__ == '__main__':

    print('Welcome to my module. We are exemining function sin^3(x). First, some aproximation of taylor series with different n')
    print('=' * 100)
    vals = [1,5,10,25,50,100]
    for j in vals:
        print(f'n = {j}')
        print(taylor_for_sin3(j))
        print('=' * 100)

    print('=' * 100)
    print('Now, choose n to get graph with aproximation of n powers. n must lay in [1; 100]')
    n = input()
    while True:
        try:
            n = int(n)
            assert (n > 0 and n < 101)
            break
        except:
            print('n must lay in [1; 100]')
            n = input()

    show_graph(taylor_for_sin3(n))

