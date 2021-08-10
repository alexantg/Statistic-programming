# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:22:50 2021

@author: alexa
"""

import scipy.stats as stats

sanns = stats.hypergeom.pmf(5,12,7,6)

print(round(sanns,3))

#Kumulative (Til og med det første tallet)
sanns1 = stats.hypergeom.cdf(4,12,7,6)

print(round(sanns1,4))
