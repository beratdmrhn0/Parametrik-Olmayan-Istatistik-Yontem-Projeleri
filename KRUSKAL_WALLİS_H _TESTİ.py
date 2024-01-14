# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:00:26 2023

@author: ahmet
"""

# st.kruskal(x1,x2,x3,x4) = BÜTÜN TEST İSTATİSTİĞİNİ VERİR  KRUSKAL WALLİS İLE 

import numpy as np 
import scipy.stats as st


x1 = np.array([5,6,4,7,8,6])
x2 = np.array([7,4,5,7,9,10])
x3 = np.array([10,11,9,12,10,8])
x4 = np.array([1,2,3,3,2,1])


veri = np.concatenate((x1, x2, x3, x4))         #veriyi birleştirdik 
t = np.repeat([1,2,3,4],[6,6,6,6])      #veriyi grupladık; veriyi tekrarladık 6 tane 1 den 6 tane 2 den 6 tane 3 ten 6 tane de 4 den yaptık çünkü verimi,z 24 tane 

r = st.rankdata(veri)       #Veriyi sıralıyoruz 
c,n =np.unique(t,return_counts = True)      #Verideki eleman sayısını buluyoruz 

N = len(veri)

#  r[t==1]       #t'nin 1. gruptaki olanlarını verdi
# (r[t==1]**2)/n[0]
rj = []
rn = []
tt = 0

for i in c :
    rj.append(np.mean(r[t==i]))      #bir grubun ortalaması
    rn.append(np.sum(r[t==i]))
   # tt+=((r[t==i])**2)/n[i]   -HATALI     #herhangi biri için topladık ama biz bunların toplamını istiyoruz o yüzden yukarıya tt = 0 yazıyoruz 
   # r[t==i]         #Tüm grupları teker teker döndürcek



rr = (N+1)/2
rn = np.array(rn) #Diziye çevirdik yoksa hata verir
rj = np.array(rj) #Diziye çevirdik yoksa hata verir
H = (12/(N*(N+1)))*np.sum(n*((rj-rr)**2))
H = (12/(N*(N+1)))*np.sum((rn**2)/n)-3*(N+1)


tie = st.tiecorrect(r) #düzeltme faktörü bu düzeltmeyi printe ekleyerek işlemi tamamlyıoruz
H= H/tie 
print(H)

























