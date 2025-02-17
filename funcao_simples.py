import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-1.681,1.87474,100)
# y = (-(0.76 * x - 0.65)**4 - (0.76 * x - 0.65)**3 + (0.76 * x - 0.65)**2 - (0.76 * x - 0.65) + 1) * 0.7
x = np.linspace(-5.65,5.65,10000)
y = -(1/16) * x**2 + 2

z = np.zeros_like(y)

n = 3
for k in range(n * 2**n + 1):
    for i in range(len(y)):
        if k != n * 2**n:
            if y[i] >= k * 2**(-n) and y[i] < (k + 1) * 2**(-n):
                z[i] = k * 2**(-n)
            if y[i] == k:
                print(f"f(x) = {k} in {x[i]}")
        else:
            if y[i] >= n:
                z[i] = k * 2**(-n)
            if y[i] == k:
                print(f"f(x) = {k} in {x[i]}")

plt.plot(x,y)
plt.plot(x,z)
plt.show()

# table = np.zeros((len(x),2))
# for i in range(len(x)):
#     table[i,0] = x[i]
#     table[i,1] = z[i]
    
# for i in range(len(x)):
#     print(f"{table[i,0]:.3f}, {table[i,1]:.3f}")