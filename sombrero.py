#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 Fall 2018
# Assignment: Classwork 12
###

import numpy as np
import matplotlib.pyplot as plt
import numba as nb


@nb.jit
def Df(t, r, F):
    return (np.array([r[1], -0.25*r[1] + r[0] - r[0]**3 + F*np.cos(t)]))


def stingray(F, x, y, N):
    cht = 0.001
    t = np.arange(0, 2*np.pi*N, cht)
    tk = len(t)
    ran = np.zeros((tk+1, 2))
    ran[0] = np.array([x, y])
    i = 1

    for i in range(tk):
        k1 = cht*(Df(t[i], ran[i], F))
        k2 = cht*(Df(t[i] + cht/2, ran[i] + (k1/2), F))
        k3 = cht*(Df(t[i] + cht/2, ran[i]+ (k2/2), F))
        k4 = cht*(Df(t[i] + cht, ran[i] + k3, F))
        ran[i+1] = ran[i] + ((k1 + 2*k2 + 2*k3 + k4)/6)
    return np.array([ran[:,0], ran[:,1]])
def linegraph(gr, F, title):
    plt.plot(gr[0], gr[1], label="Oscillation")
    plt.title(title)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def scattergraph(gr, F, title):
    plt.scatter(gr[0], gr[1], label="Scattered Oscillation", s=2)
    plt.title(title)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.legend()
    plt.grid(True)
    plt.show()







