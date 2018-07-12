import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

plt.plot(x, np.sin(x), "-r", label = "Sinus")
plt.plot(x, np.cos(x), "--g", label = "Cosinus")
plt.xticks([-10, 0, 10])
plt.yticks([-1, 0, 1])
plt.ylim(-2, 2)
plt.legend()
plt.grid()

plt.show()