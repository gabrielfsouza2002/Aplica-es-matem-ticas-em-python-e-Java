#!/usr/bin/env python
# coding: utf-8

# In[69]:


import numpy as np

a = np.array ([[3,2,4],
               [1,1, 2],
               [4,3,-2]], dtype=float)
            

b = [1,2,3]


def eliminação_gaussiana (a,b): # a = matriz quadrada principal; b = resultado
    n = np.size (b) #np.size, lê tamanho da matriz.
    for k in range (n-1): # Quantidade de vezes que teremos que realizar o processo de pivoteamento.
        for i in range (k+1, n):
            m = a[i,k]/a[k,k]
            a [i,:] = (a [i,:] - m*a[k,:])
            b [i] = float (b [i] - m*b[k])
            
    x =np.zeros(3) #{0,0,0}
    x [n-1] = b[n-1]/a[n-1][n-1]
    cont=np.linspace(0,1,2,dtype=int) #[0,1]
    cont=cont[::-1] #[1,0]
    for k in cont:
        s=0
        for i in range(k+1,3):
            s=s+a[k][i]*x[i]
        x[k] = (b[k]-s)/(a[k][k]) 
            
    return a,b,x

eliminação_gaussiana (a,b)


# %%
