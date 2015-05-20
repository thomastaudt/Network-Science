# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:36:38 2015

@author: Erik
"""

import numpy as np
import matplotlib.pyplot as plt

def couple(theta, K , w):
  sums = np.zeros(len(theta))  
  for i in range(0, len(theta)):
    sums[i] = np.average(np.sin(theta - theta[i]))
  sums *= K
  sums += w
  return sums

def calc_r( N, K ):
  TIME = 1000
  theta = np.random.random(N) * 2 * np.pi
  plots = np.zeros((TIME))
  r = np.zeros(TIME)
  w = np.random.normal(size=N)
  print(w)
  for i in range(TIME):
    #print((couple(theta, K, w) * 0.1)[0])
    theta += couple(theta, K, w) * 0.01
    theta %= 2*np.pi
    plots[i] = theta[0]
    r[i] = np.abs(np.average(np.exp(1j * theta)))

  #plt.scatter(np.arange(TIME), plots)
  return np.average(r[-100:-1])
  #plt.plot(r)

def B11( N ):
  STEPS = 50
  r = np.zeros(STEPS)    
  for fgnsfksgj in range(30):  
    for i in range(STEPS):
      r[i] += calc_r(N, i * 0.1)
  #plt.plot(np.arange(STEPS, step=0.1), r)
  return r/30