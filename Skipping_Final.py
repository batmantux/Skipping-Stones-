#!/usr/bin/env python
# coding: utf-8

# In[128]:


import numpy as np
import math
class CriticalVelocity:
    """ Class of Critical Velocity """

    def __init__(self, o, M , a,N):
        self.o = o 
        self.g = 9.8
        self.M = M
        self.d = 1000
        self.a = a
        self.C = 1
        self.N = N
   
    def u(self):
        return (np.sin(np.radians(self.o)) + np.cos(np.radians(self.o))) / (np.cos(np.radians(self.o)) - np.sin(np.radians(self.o)))

    def L(self):
        return 2*3.14*np.sqrt((2*(self.M)*np.sin(np.radians(self.o))/(self.C*self.d*self.a)))
    
    def Vc(self):
        return np.sqrt(2*(self.u())*(self.g)*(self.L()))
    
    def Vin(self):
        return np.sqrt(((self.Vc())**2)*(self.N))
    
   
    
    
    


# In[169]:


for i in [0.1,0.2,0.3,0.4,0.5]:
    for j in [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]:
        for k in np.arange(0,45,1):
            Coef = CriticalVelocity(o=k, M=i,a=j,N=40)
            L=Coef.Vin()
            print(i,j,k)
            print(L<=11)
           


            
        


# In[ ]:




