import numpy as np

x = [1.4, 1.7, 2.0, 2.3, 2.6, 2.9, 3.2]
y = [3.3, 4.4, 5.3, 4.7, 3.1, -0.3, -3.3]
h = 0.3

integral = h/2 * (y[0] + 2*sum(y[1:-1]) + y[-1])
print(integral)