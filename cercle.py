
def make_f(T):
    def f(x):
        assert(not x > T)
        if x <= 0.5 * T:
            return ((0.25 * T) ** 2 - (x - 0.25 * T) ** 2) ** 0.5
        else:
            return ((0.25 * T) ** 2 - (x - 0.75 * T) ** 2) ** 0.5
    return f

  
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 1.0, 500)
    f = make_f(1.0, 1.0)
    y = [f(_) for _ in x]
    plt.plot(x, y)
    plt.show()