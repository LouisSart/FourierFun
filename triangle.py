import math
import numpy as np


def make_f(E, T):
    def f(x):
        assert(not x > T)
        if x == T:
            return 0.0
        elif x <= 0.5 * T:
            return 2.0 * E * x / T
        else:
            return 2.0 * E * (1.0 - x / T)
    return f



def fourier(E, T):
    def a(n):
        if n % 2 == 0:
            return 0
        else:
            return -4.0 * E / (np.pi * n)**2
        
    w = 2.0 * math.pi / T
    
    def f_approx(m, x):
        ret = E / 2
        for n in range(1, m + 1):
            ret += a(n) * math.cos(n * w * x)
        return ret
    return f_approx