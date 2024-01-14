# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:17:59 2023

@author: ahmet
"""

import numpy as np 
import scipy.stats as st
import math

once = np.array([18,21,16,22,19,24,17,21,23,18,14,16,16,19,18,20,12,22,15,17])
sonra = np.array([22,25,17,24,16,29,20,23,19,20,15,15,18,26,18,24,18,25,19,16])

D= once-sonra
D_ort=np.mean(D)
Sd=np.std(D,ddof=1)
Sd1=np.std(D)
n=len(D)
t=(D_ort-0)/(Sd/math.sqrt(n))
   
#Hazır fonksiyon           
print(st.ttest_rel(once, sonra))

#TESTLERİ ST.TTEST YAPARAK AÇIKLAMALARINA BAKARAK YAPABİLİRİZ/BULABİLİRİZ

#H0 HİPOTEZİ REDDEDİLİR
