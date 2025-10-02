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

def harmonic(a, b, w, n):
    return lambda t: a * np.cos(n * w * t) + b * np.sin(n * w * t)

def harmonics(x, f, T, N):
    # Generate all harmonics up to n = N
    w = 2.0 * np.pi / T
    H = np.zeros((N + 1, len(x)))
    A, B = np.zeros(N + 1), np.zeros(N + 1)
    A[0] = c0(x, f, T)
    H[0, :] = A[0]
    for n in range(1, N + 1):
        an = a(x, f, T, n)
        bn = b(x, f, T, n)
        A[n] = an
        B[n] = bn
        h = harmonic(an, bn, w, n)
        H[n, :] = H[n - 1, :] + np.array([h(t) for t in x])
    return A, B, H

if __name__ == "__main__":
    
    T = 5.00
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
    A, B, H = harmonics(x, f, T, 100)

    # Créer une figure avec deux sous-graphiques
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Premier subplot: signal original et approximation de Fourier
    f_plot, = ax1.plot(x, f_arr, label='Signal original')
    f_approx_plot, = ax1.plot(x, np.zeros_like(x), 'r-', label='Approximation Fourier')
    ax1.set_xlabel('Temps')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Signal et son approximation de Fourier')
    ax1.legend()
    ax1.grid(True)

    # Deuxième subplot: spectre d'amplitude avec bar plot
    n_harmonics = len(A)
    harmonics_idx = np.arange(n_harmonics)
    amplitudes = np.sqrt(A**2 + B**2)  # Amplitude = sqrt(an^2 + bn^2)

    # Créer le diagramme en barres
    nbars = 15
    bars = ax2.bar(harmonics_idx[:nbars], amplitudes[:nbars], 
                   color='lightgray', alpha=0.4)
    ax2.set_xlabel('Harmonique n')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Spectre d\'amplitude')
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(range(nbars + 1))

    # Fonction de mise à jour
    def submit(text):
        n = int(text)
        # Mettre à jour l'approximation de Fourier
        f_approx_plot.set_ydata(H[n, :])

        # Mettre à jour les couleurs des barres
        for i, bar in enumerate(bars):
            if i <= n:
                # Harmoniques utilisées - couleur vive
                bar.set_color('blue')
                bar.set_alpha(0.8)
            else:
                # Harmoniques non utilisées - couleur atténuée
                bar.set_color('lightgray')
                bar.set_alpha(0.4)

        ax1.relim()
        ax1.autoscale_view()
        plt.draw()

    fig.subplots_adjust(bottom=0.15, hspace=0.4)
    axbox = fig.add_axes([0.4, 0.02, 0.2, 0.05])
    text_box = TextBox(axbox, "Nombre d'harmoniques: ", textalignment="center")
    text_box.on_submit(submit)

    plt.show()