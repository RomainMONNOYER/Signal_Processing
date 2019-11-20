#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:15:08 2019

@author: romainmonnoyer anthonyzanotto
"""

import numpy as np
import matplotlib.pyplot as plt


"""
Creation signal de test
Par Shannon:
fe>=2fmax
fmax=500
"""

A=10;
f=500;
fe=10000;
t=np.arange(200)/fe;
fct=A*np.sin(2*np.pi*f*t);

"""
Affichage du signal test
"""

plt.plot (t,fct);
plt.show();

"""
Normalisation du signal
"""
Max_fct=np.max(fct);
f1=fct/Max_fct;
plt.plot(t,f1);
plt.show();

