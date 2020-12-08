import numpy as np

np.random.seed(42)
a = np.random.randn(3, 4)
a[2][2] = np.nan
print(a)

np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header="#1,#2,#3,#4")



