
import numpy as np
import matplotlib.pyplot as plt
from odu_vfi import searchProblem

sp = searchProblem(F_a=1, F_b=1, G_a=3, G_b=1.2)
grid = np.linspace(0, 2, 150)
fig, ax = plt.subplots()
ax.plot(grid, sp.f(grid), label=r'$f$', lw=2)
ax.plot(grid, sp.g(grid), label=r'$g$', lw=2)
ax.legend(loc=0)
fig.show()
