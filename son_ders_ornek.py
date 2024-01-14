# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:02:52 2023

@author: ahmet
"""
import numpy as np
import scipy.stats as st

x1 = np.array([5,6,4,7,8,6])
x2 = np.array([7,4,5,7,9,10])
x3 = np.array([10,11,9,12,10,8])
x4 = np.array([1,2,3,3,2,1])

X = np.concatenate((x1,x2,x3,x4))

Xi_ort = np.mean(X[t==(i+1)])
Xj_ort = 

Si = st.ppf()