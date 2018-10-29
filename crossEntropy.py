from mpl_toolkits import mplot3d
from gifMkr import gifMkr
import numpy as np
import matplotlib.pyplot as plt
import os

def f(x, y):
    return np.log((np.power(1-x,y-1))/np.power(x,y))

x = np.linspace(0.01, 0.99, 30)
y = np.linspace(0.01, 0.99, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

g = 2
# need to define granularity and number of iterations follow from there

for i in range(int(360/g)):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=5, cstride=3, cmap='viridis', edgecolor='none')
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.set_zlabel('H')
    ax.view_init(30, g*i)
    fig.savefig('img/test' + str(i) + ".png")
    plt.close(fig)

gifMkr(impath = os.getcwd()+"/img", gifpath = os.getcwd(), giftitle = "/crossEntropy.gif", dur = 0.05)
