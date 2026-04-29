import numpy as np
import matplotlib.pyplot as plt

# Deine Daten (mm)
g = np.array([190, 180, 210, 300, 185])
b = np.array([650, 870, 490, 300, 715])

# x-Werte für Plot
x = np.linspace(0, 400, 500)

plt.figure()

# Geraden plotten
for gi, bi in zip(g, b):
    y = bi * (1 - x/gi)
    plt.plot(x, y, label=f"g={gi}, b={bi}")

# Achsen
plt.xlabel("g (mm)")
plt.ylabel("b (mm)")
plt.xlim(0, 400)
plt.ylim(0, 900)

# Diagonale (optional, hilft f zu sehen)
plt.plot(x, x, '--', color='gray', label="y = x")

plt.legend()
plt.grid()

plt.show()
