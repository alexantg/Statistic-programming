# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:01:13 2021

@author: alexa
"""

import scipy.stats as sp
import math as m

x = int(input("Skriv inn antall ganger hendelsen intreffer: "));
n = int(input("Skriv inn totalt antall forsøk:"));

konfInput = int(input("Vennligst skriv inn ønsket konfidensintervall i prosent: "));

pHatt = (x/n)


check = (n*pHatt)*(1-pHatt);


if (check>=5):
    print("Tallene oppfyller kravene for en tilnærmet normalfordeling");
    
else:
    print("Tallene oppfyller ikke kravene for en tilnærmet normalfordeling");
    

alphaHalve = round(((1 - (konfInput/100))/2),3);

z = round(sp.norm.ppf(1-alphaHalve),2)


lower = round(pHatt - (z*(m.sqrt((pHatt*(1-pHatt))/n))),4);
upper = round(pHatt + (z*(m.sqrt((pHatt*(1-pHatt))/n))),4);


print("Et 95% konfidensintervall for p er: [",lower,upper,"]");
         


    
    

