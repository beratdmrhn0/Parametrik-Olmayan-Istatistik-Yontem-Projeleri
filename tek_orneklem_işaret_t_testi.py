#TEK ÖRNEKLEM İŞARET T-TESTİ

#Tek örneklem için kullanılır 
#k test istatistiğidir 
#Parametrik olmayan bir testtir(normal dağılmayan)
#Medyanlar kullanılır(mu yerine)(parametrik olmadığı için)


import numpy as np  
import scipy.stats as st

x=np.array([32,65,27,34,66,40,36,52])#np.array yaparak listten dizi oldu for döngüsüne gerek kalmadı 
M=30
D=x-M
DD=D[D!=0]
k_hesap=0

for i in range(len(x)):
    if D[i]>0:
        k_hesap+=1
        
p=st.binom.cdf(k_hesap-1,len(x) ,0.5)#Hesapladığımız x değerinin bir eksiğini alıyoruz 
print(p)

k_hesap=np.sum(D>0)

print(k_hesap)
