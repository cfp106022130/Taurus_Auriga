# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 05:36:07 2021

@author: sharon
"""

import numpy as np
import matplotlib.pyplot as plt

name = 'Target_a.txt'
file = '../中研院天文所/'+name
x, d_x= np.loadtxt(file, dtype='str', unpack=True)

u_x = []

for i in range(len(x)):
    if(x[i][0] == '<'):
        x[i] = x[i][1:]
        u_x.append(i)

X = x.astype(float)
fig = plt.figure(figsize=(6, 6))
plt.hist(X, bins=int(np.max(X)/0.3), density=True, histtype='step', cumulative=-1)

plt.legend()
plt.xlim([0.38, 6])
plt.xlabel('\u03B1', size=12)
plt.ylabel('P ( > \u03B1 )', size=12)
plt.savefig(name+'.png', dpi=1000)