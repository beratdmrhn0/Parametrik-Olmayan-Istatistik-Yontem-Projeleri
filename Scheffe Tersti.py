# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:00:17 2023

@author: ahmet
"""
import numpy as np 
import scipy.stats as st
import math


x1 = np.array([5,6,4,7,8,6])
x2 = np.array([7,4,5,7,9,10])
x3 = np.array([10,11,9,12,10,8])
x4 = np.array([1,2,3,3,2,1])

X = np.concatenate((x1,x2,x3,x4))
t = np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4])
c,g =np.unique(t,return_counts = True)

def anova(X,t):
    X_o = np.mean(X)
    SST = np.sum((X-X_o)**2)
    n = len(X)
    c,g =np.unique(t,return_counts = True)
    k = len(c)
    SSB = 0
    SSE = 0
    for i in range(k):
        SSB+=g[i]*((np.mean(X[t==i+1])-X_o)**2)
        SSE+=np.sum((X[t==(i+1)]-np.mean(X[t==(i+1)]))**2)
        
        
    MSB=SSB/(k-1)
    MSE=SSE/(n-k)
    F = MSB/MSE
    return(F,MSE)
    
F,MSE = anova(X,t)
n=24
k =4
#Grup ortalamaları
Xort = []
for i in range(k):
    Xort.append(np.mean(X[t==(i+1)]))
    
cc = np.array([1,-1,0,0])
l = np.sum(cc*Xort)

s = math.sqrt((k-1)*st.f.ppf(0.95,k-1,n-k))*math.sqrt(MSE*np.sum(cc*2/g))
print(s)




##x1_ort = 6
##x2_ort = 7
##x3_ort = 10
##x4_ort = 2

#c,n=np.unique(t,return_counts=True)
#k=len(c)

