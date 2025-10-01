# Décomposition de Fourier d'un signal créneau
import matplotlib.pyplot as plt
import numpy as np
import scie as sci
import pic as pic
import cercle as cer
import creneau as crn
import triangle as tri
import sys
from integration import *
from matplotlib.widgets import TextBox
        
def fourier(x, f, T, n):
    w = 2.0 * np.pi / T
    an = a(x, f, T, n)
    bn = b(x, f, T, n)
    return lambda t: an * np.cos(n * w * t) + bn * np.sin(n * w * t)

def harmonics(x, f, T, N):
    # Generate all harmonics up to n = N
    ret = np.zeros((N + 1, len(x)))
    mean = c0(x, f, T)
    ret[0, :] = [mean]
    for n in range(1, N + 1):
        h = fourier(x, f, T, n)
        ret[n, :] = ret[n - 1, :] + np.array([h(t) for t in x])
    return ret
    
if __name__ == "__main__":
    
    T = 5.23
    E = 100
    N = 500
    x = np.linspace(0, T, N)
    
    match sys.argv[1]:
        case "creneau":
            f = crn.make_f(E, T)
        case "triangle":
            f = tri.make_f(E, T)
        case "cercle":
            f = cer.make_f(T)
        case "scie":
            f = sci.make_f(E, T)
        case "pic":
            f = pic.make_f(E, T)
        case _:
            print("Argument error:", sys.argv[1])
            exit()

    f_arr = np.array([f(_) for _ in x])
    f_fourier_arr = harmonics(x, f, T, 100)
    
    fig, ax = plt.subplots()
    f_plot, = ax.plot(x, f_arr)
    f_approx_plot, = ax.plot(x, np.zeros_like(x))

    def submit(text):
        n = int(text)
        f_approx_plot.set_ydata(f_fourier_arr[n, :])
        ax.relim()
        ax.autoscale_view()
        plt.draw()

    fig.subplots_adjust(bottom=0.2)
    axbox = fig.add_axes([0.4, 0.05, 0.2, 0.075])
    text_box = TextBox(axbox, "Nombre d'harmoniques: ", textalignment="center")
    text_box.on_submit(submit)
    # text_box.set_val("0")
    plt.show()