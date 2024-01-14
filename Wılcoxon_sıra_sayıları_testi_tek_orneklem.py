#WİLCOXON SIRA SAYILI İŞARET TESTİ

#Tek örneklem için 
#Parametrik olmayan bir testtir(normal dağılmayan)
#Medyanlar kullanılır(mu yerine)
#İşaret testini sıra sayıları eklenerek gelişmiş halidir

import numpy as np 
import scipy.stats as st

X=np.array([1.51,1.35,1.69,1.48,1.29,1.27,1.54,1.39,1.45])
M=1.4
D=np.round(X-M,2)
DD=D[D!=0]#Sıfır olanları çıkarttık 




r=st.rankdata(abs(DD))#Sıralamak için kullanılır 
T_hesap_p=np.sum(r*(DD>0))#toplam hesap
T_hesap_n=np.sum(r*(DD<0))



print(T_hesap_n)
print(T_hesap_p)

#Hazır fonksiyon 
print(st.wilcoxon(np.round(X-M,2)))#Kütüphane kullanarak wilcoxon işaretli sıra sayıları testi
print(st.wilcoxon(np.round(X-M,2),alternative='less'))
print(st.wilcoxon(np.round(X-M,2),alternative='greater'))
























