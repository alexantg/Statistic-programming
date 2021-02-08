import numpy as np
import scipy.stats as stats

n = 6
p= 0.1

#P(X = x )
sanns1 = stats.binom.pmf(1,n,p)
print ("Sannsynlighet " , sanns1)

#F(X)
x = 3
sanns2 = stats.binom.cdf(x,n,p)
print ("Sannsynlighet " , sanns2)

#Simulere et binomisk forsøk
r = stats.binom.rvs(n, p , size = 10000)

snitt = np.mean(r)

#Standardavvik

#Varians