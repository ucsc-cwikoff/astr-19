import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 2 * np.pi, 1000)
    sinx = np.sin(x)
    
    plt.plot(x, sinx)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.show()
    
if __name__ == "__main__":
    main()