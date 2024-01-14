# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:16:23 2023

@author: ahmet
"""

import numpy as np 
import scipy.stats as st

k=np.array([34,36,41,43,44,37])
e=np.array([45,33,35,39,42])

n1=len(k)
n2=len(e)


X=np.concatenate((k, e)) #YADA AŞAĞIDAKİ 
#XX=np.append(e,k)

R=st.rankdata(X)

R1=np.sum(R[0:len(k)])

#R2=np.sum(R[len(k):len(R)])YADA R2=np.sum(R[-len(e)])
R2=np.sum(R[len(k):])

U1=R1-n1*(n1+1)/2
U2=R2-n2*(n2+1)/2
U=min(U1,U2)
print(U)
print(st.mannwhitneyu(k, e))
