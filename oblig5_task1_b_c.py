# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:06:41 2021

@author: alexa
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math as m



antallKast = int(input("Antall Terningskast: "));
antallOmganger = int(input("Antall Omganger: "));

meanArray = np.zeros(antallOmganger)

i =0; 
index=0;

for i in range(0,antallOmganger):
    sumOyne = 0
    for j in range(0,antallKast):
        kast = random.randint(1, 6);
        sumOyne = sumOyne + kast
    
    mean = round(sumOyne/antallKast,2);
    meanArray[index] = mean;
    index = index +1
    
    
plt.hist(meanArray, density=False, bins=30);
plt.title("Oversikt over gjennomsnitt")
plt.show();


#C-OPPGAVEN STARTER HER
summ = 0;
sumForVarians = 0;
gjsnt = 0;
length = len(meanArray);

for x in meanArray: 
    summ = summ + x
    sumForVarians = sumForVarians+ m.pow(x, 2);
    
gjsnt = round(summ/length,2)

print("Gjennomsnittet av gjennomsnittene er: ", gjsnt);

utvVarians = (1/(length-1)* (sumForVarians - (length * m.pow(gjsnt, 2))));

std = round((m.sqrt(utvVarians)),2)

print("Utvalgsvariansen er: ", std)


