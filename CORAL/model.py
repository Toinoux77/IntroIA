import matplotlib.pyplot as plt
import numpy as np

def show_coral(dots):
    
    for x , y in dots:
        plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)

    plt.title("Mon graphique avec des points et un fil")

    plt.grid(True)
    plt.show()


