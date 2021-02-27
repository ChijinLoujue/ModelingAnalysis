import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

x = np.random.normal(0, 1, 1000)

plt.plot(range(1000), x)
plt.show()
x = np.sort(x)
plt.plot(range(1000), x)
plt.show()
shuffle(x)
plt.plot(range(1000), x)
plt.show()