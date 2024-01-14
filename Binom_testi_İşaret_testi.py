#P=0.5 İKEN TEK ORNEKLEMLER İÇİN BİNOM TESTİ(İŞARET TESTİ)

import numpy as np 
import math 
import scipy.stats as st

X=np.array([30,65,27,34,66,40,36,52])
M=30
D=X-M
DD=D[D!=0]

k_hesap_p = np.sum(DD>0)#+
k_hesap_n = np.sum(DD>0)#-

print(st.binomtest(min(k_hesap_p,k_hesap_n), len(D),p=0.5))
print(st.binomtest(k_hesap_p,len(D),p=0.5 ))
print(st.binomtest(k_hesap_n,len(D),p=0.5 ))
print(k_hesap_p,k_hesap_n)

