#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:44:33 2019

@author: romainmonnoyer anthonyzanotto
"""
import numpy as np
import matplotlib.pyplot as plt

width=25
step=0;
pas=5;
while True:
    W=np.arange(0+step,width+step)/fe;
    fct=A*np.sin(2*np.pi*f*W)/Max_fct; 
    plt.plot(W,fct);
    plt.show();
    step=step+pas;
    if W[0]+width/fe>=np.max(t):
        break;
    