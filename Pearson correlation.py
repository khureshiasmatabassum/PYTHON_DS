import numpy as np
hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 75, 90]
correlation = np.corrcoef(hours, marks)
print(correlation)