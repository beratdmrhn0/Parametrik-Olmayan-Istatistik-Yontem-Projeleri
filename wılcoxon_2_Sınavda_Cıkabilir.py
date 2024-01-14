#SINAVDA BÖYLE BİŞE ÇIKACAK 

import numpy as np 
import scipy.stats as st

def two_wilcox(X1,X2):
    D=np.round(X1-X2,2) 
    D= X1-X2   
    D1=D[D!=0]   
    r=st.rankdata(abs(D1))   
    W=np.sum(r*(D1>0))
    
    return W

once = np.array([2.11,1.85,1.82,1.75,1.54,1.52,1.49,1.44,1.38,1.30,1.20,1.19])
sonra = np.array([2.15,2.11,1.93,1.83,1.90,1.56,1.44,1.43,1.28,1.30,1.21,1.30])

    
print(two_wilcox(once, sonra))
print(two_wilcox(sonra, once))

print(st.wilcoxon(sonra,once,method='approx'))
print(st.wilcoxon(once,sonra,method='approx'))
print(st.wilcoxon(once,sonra))