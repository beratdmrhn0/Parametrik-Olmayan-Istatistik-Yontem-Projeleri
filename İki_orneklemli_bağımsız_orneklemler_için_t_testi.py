#İKİ ÖRNEKLEMLİ BAĞIMSIZ ORNEKLEMLER İÇİN T TESTİ

import numpy as np 
import math 
import scipy.stats as st

X1 = np.array([56,58,59,77,81,88,89,91,91,92,93,94,95,96,96])#X1=KIZ
X2 = np.array([62,63,64,67,67,68,77,81,87,87,93,93])         #X2=ERKEK 
alfa = 0.05

def bagimsiz_t_testi(X1,X2,alfa=0.05):
    
    X1_ort = np.mean(X1)
    X2_ort = np.mean(X2)
    
    n1 = len(X1)
    n2 = len(X2)
    
    s1 = np.std(X1,ddof = 1)#Eğer ddof = 1 yazmazsak kitleninkini hesaplar 
    s2 = np.std(X2,ddof = 1)
    
    Sp = math0.sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/n1+n2-2)
    
    istatistik,p_value = st.levene(X1,X2,center="mean")

    if p_value < alfa: #Varyansların eşit olduğu durumda t_hesap(homojen)
        print("H0 reddedilir yani homojen değil.")
        t_hesap = ((X1_ort-X2_ort)/(Sp*np.sqrt(1/n1+1/n2)))
        df = n1+n2-2
    else:   #Varyansların eşit olmadığı durumda t_hesap(homojen değil)
        print("H0 reddedilemez yani homojen ")
        t_hesap = (X1_ort-X2_ort)/np.sqrt((s1**2/n1)+(s2**2/n2))
        df = ((((s1**2)/n1)+((s2**2)/n2))**2)/(((((s1**2)/n1)**2))/((n1-1))+(((((s2**2)/n2)**2))/(n2-1)))     
        
    return t_hesap,df

t_hesap , df=bagimsiz_t_testi(X1, X2)
print("t hesap = ",t_hesap)#t_hesap = 1.53 , df=25 olucak
print("df = " ,df)
    #Kütüphane kullanılarak hesaplama
    
#Varyansların eşitliğini kontrol etme 
lev,p = st.levene(X1,X2,center = "mean")#İstatistik,p_value = st.levene(X1,X2,center = "mean")

#Varyansların eşit
st.ttest_ind(X1,X2)
st.ttest_ind(X1,X2,equal_var = True)

#Varyanslar eşit değil 
st.ttest_ind(X1,X2,equal_var = False)    

    
        
