import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
x = np.linspace(-4, 4, 500)
plt.plot(x, t.pdf(x, df=10))
plt.title("Student's t Distribution")
plt.xlabel("t")
plt.ylabel("Density")
plt.show()