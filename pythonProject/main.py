import numpy as np
from matplotlib import pyplot as plt

x = [x/100 for x in range(0, 1201*6)]
y= []
for n in x:
    if n % 12 < 6:
        y.append((1.66/6)*(n%12))
    else:
        y.append((1.66 / 6) * (-n % 12))

xarr = np.array(x)
yarr = np.array(y)
plt.title("Função de administração")
plt.xlabel("Tempo (horas)")
plt.ylabel("Massa/Tempo (miligramas/hora)")
plt.plot(xarr, yarr)
plt.show()