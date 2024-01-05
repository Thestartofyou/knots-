import matplotlib.pyplot as plt
import numpy as np

def parametric_equations(t):
    x = np.sin(t) + 2 * np.sin(2*t)
    y = np.cos(t) - 2 * np.cos(2*t)
    return x, y

def draw_knot():
    t = np.linspace(0, 2*np.pi, 1000)
    x, y = parametric_equations(t)

    plt.plot(x, y, label='Knot')
    plt.title('Parametric Equations of a Knot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    draw_knot()

