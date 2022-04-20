import numpy as np
def KnowPgetF(P,i,n):
    result = P*((1+i)**n)
    return result;
def KnowAgetF(A,i,n):
    result = A*((((1+i)**n)-1)/i)
    return result;
def KnowAGetP(A,i,n):
    up = ((1+i)**n)-1
    down = i*((1+i)**n)
    full = up/down
    result = A*full
    return result;
def KnowFGetP(F,i,n):
    result = F/((1+i)**n)
    return result;
def KnowPgetA(P,i,n):
    up = i*((1+i)**n)
    down = ((1+i)**n)-1
    full = up/down
    result = full*P
    return result;
def ggs(A,i,g,n):
    up = 1-((1+g)**n)*((1+i)**(-n))
    down = i-g
    full = up/down
    result = A*full
    return result;
def ggs1(A,i,n):
    result = A*(n*((1+i)**(-1)))
    return result;
i = 0.07
n = 10
pwc1 = (345000 + KnowAGetP(60000, i, n))
pwc2 = (170000 + KnowAGetP(21000, i, n)+KnowFGetP(170000, i, n))
pwb1 = (KnowAGetP(150000, i, n))
pwb2 = (KnowAGetP(110000, i, n))
deltac = pwc1-pwc2
deltab = pwb1-pwb2
delta = deltab/deltac
print(deltac)