# -*- coding: iso-8859-15 -*-
"""
Created on Sat Nov 04 20:46:20 2017

@author: allisson
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.plot(x,y)
plt.title("Exibicao dos eixos X e Y")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()