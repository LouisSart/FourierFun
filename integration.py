import triangle as tri
import creneau as crn
import numpy as np

def midpoint(x, f):
    # Integrate f on all values of x with midpoint method
    ret = 0.0
    for i in range(len(x) - 1):
        mid = (x[i + 1] + x[i]) / 2.0
        dx = x[i + 1] - x[i]
        ret += f(mid) * dx
    return ret
   
def c0(x, f, T):
    # Mid value of f over x
    return 1. / T * midpoint(x, f)
        
def a(x, f, T, n):
    # Fourier coefficient for cos(n *w *t)
    w = 2 * np.pi / T
    def conv(x):
        return f(x) * np.cos(n * w * x)
    return 2.0 / T * midpoint(x, conv)
   
def b(x, f, T, n):
    # Fourier coefficient for sin(n *w *t)
    w = 2 * np.pi / T
    def conv(x):
        return f(x) * np.sin(n * w * x)
    return 2.0 / T * midpoint(x, conv)
    
if __name__ == "__main__":
    x = np.linspace(0, 1.0, 1000)
    f_crn = crn.make_f(1.0, 1.0)
    f_tri = tri.make_f(1.0, 1.0)
    # print(midpoint(x, f_crn))
    print(a(x, f_crn, 1.0, 1))
    print(b(x, f_crn, 1.0, 1))
    # print(midpoint(x, f_tri))