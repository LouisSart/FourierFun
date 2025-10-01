def make_f(E, T):
    d = 0.1 * T
    def f(t):
        assert(not t > T)
        if ((T / 2 - t)**2)**0.5 < d:
            return E
        else:
            return 0.0
    return f