import scipy.stats as stats
import numpy as np

import matplotlib.pyplot as plt 


n = int(input("Input n-value: "))
p = float(input("Input p-value: "))


#print(n)
#print (p)

x1 = np.arange(0,n,1)
y1 = stats.binom.pmf(x1,n,p)

x2 = np.arange(0,n,1)
y2 = stats.binom.cdf(x2,n,p)

plt.plot(x1,y1, label="P(X)=x")
plt.plot(x2,y2, label="F(X) = P(X <=x )")

plt.scatter(x1,y1)
plt.scatter(x2,y2)

plt.ylabel("P")
plt.xlabel("x")

plt.legend(loc="upper left")



