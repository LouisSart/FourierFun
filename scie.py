import math
import numpy as np

def make_f(E, T):
    def f(t):
        assert(not t > t)
        if t <= 0.5 * T:
            return 2 * E / T * t
        else:
            return 2 * E / T * (t - T / 2)
    return f