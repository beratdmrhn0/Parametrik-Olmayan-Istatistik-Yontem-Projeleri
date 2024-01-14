# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 01:08:47 2023

@author: ahmet
"""

import scipy.stats as st
import numpy as np 

m = np.array([25.2,17.4,22.8,21.9,19.7,23.0,16.9,21.8,23.6,22.5])
b = np.array([18.0,22.9,26.4,24.8,26.9,17.8,21.0,25.2])

istatistik,p_value =st.shapiro(m)
istatistik,p_value =st.shapiro(b)

print(istatistik,p_value)
