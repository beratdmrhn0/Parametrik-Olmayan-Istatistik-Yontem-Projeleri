#WİLCOXON İŞARET SIRA SAYILARI TESTİ(İKİ BAĞIMLI DEĞİŞKEN İÇİN)

import numpy as np 
import scipy.stats as st

def wilcoxon_iki_bagimli(X1,X2):
    D = np.round(X1-X2,2)       #<--round şu an virgülden sonraki haneyi 2 olarak alıyor.
    D1 = D[D!=0]                #<--Sıfır olanları çıkarttık
    r = st.rankdata(abs(D1))    #<--Sıralama işlemini yapar
    
    W_hesap = np.sum(r*(D1>0))  #pozitif olan sıra sayıları topladık 
    return W_hesap

oncesi = np.array([18,21,16,22,19,24,17,21,23,18,14,16,16,19,18,20,12,22,15,17])
sonrasi = np.array([22,25,17,24,16,29,20,23,19,20,15,15,18,26,18,24,18,25,19,16])
    
test_ist = wilcoxon_iki_bagimli(oncesi, sonrasi)
print(test_ist)

#Hazır fonksiyon

test_istatistiği = st.wilcoxon(oncesi,sonrasi,method='approx')  #yaklaşık p değerini hesaplar 
test_istatistiği1 = st.wilcoxon(oncesi,sonrasi)                 #bu şekildede olur ama bi uyarı verebilir 
print(test_istatistiği)
print("\n",test_istatistiği1)