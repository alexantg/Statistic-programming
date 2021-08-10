# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:32:04 2021

@author: alexa
"""

import numpy as np
import scipy.stats as sp
import math as m


data = np.genfromtxt("data/maalinger.csv", delimiter=(','));

konfInn = int (input("Vennligst oppgi konfidensintervall i prosent: "));

alphaHalve = round(((1 - (konfInn/100))/2),3);
enMinusAlphaHalve = 1- alphaHalve;

frihetsGrader = len(data) - 1;

punktEst = round(sp.tstd(data),1)
sKvadr = m.pow(punktEst, 2)

kjiNedre = sp.chi2.isf(alphaHalve,frihetsGrader);
kjiOvre = sp.chi2.isf(enMinusAlphaHalve, frihetsGrader);

nedre = round(m.sqrt((frihetsGrader*sKvadr)/kjiNedre), 1 )
ovre = round(m.sqrt((frihetsGrader*sKvadr)/kjiOvre), 1 )


print("Et punkt estimat for standardavviket er: ", punktEst);
print("Et ", konfInn, "% konfidens intervall for sigma er: [", nedre,",", ovre,"]")