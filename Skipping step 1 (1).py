#!/usr/bin/env python
# coding: utf-8

# In[114]:


import numpy as np
import math
class CriticalVelocity:
    """ Class of Critical Velocity """

    def __init__(self, o=np.arange(0,45,1), g=9.8, M=0.1 , d=1000, a=0.1, C=1,N=10):
        self.o = o 
        self.g = g
        self.M = M
        self.d = d
        self.a = a
        self.C = C
        self.N = N
   
    def u(self):
        return (np.sin(np.radians(self.o)) + np.cos(np.radians(self.o))) / (np.cos(np.radians(self.o)) - np.sin(np.radians(self.o)))

    def L(self):
        return 2*3.14*np.sqrt((2*(self.M)*np.sin(np.radians(self.o))/(self.C*self.d*self.a)))
    
    def Vc(self):
        return np.sqrt(2*(self.u())*(self.g)*(self.L()))
    
    def Vin(self):
        return np.sqrt(((self.Vc())**2)*(self.N))
    
   
    
    
    


# In[115]:


Coef = CriticalVelocity()


# In[116]:


Coef.u()


# In[95]:


Coef.L()


# In[117]:


Coef.Vc()


# 

# In[118]:


Coef.Vin()


# In[120]:


import matplotlib.pyplot as plt 
  
x = [ 0.        ,  0.86778191,  1.05012794,  1.18262397,  1.29324247,
        1.39165823,  1.48248188,  1.56831775,  1.65080957,  1.73108322,
        1.80996228,  1.88808416,  1.96596781,  2.04405582,  2.12274233,
        2.20239254,  2.28335738,  2.36598512,  2.45063147,  2.53766885,
        2.62749564,  2.72054603,  2.81730098,  2.91830098,  3.02416142,
        3.13559156,  3.25341842,  3.37861751,  3.51235308,  3.65603163,
        3.81137456,  3.98051863,  4.16615797,  4.37174971,  4.60182008,
        4.86243486,  5.16194973,  5.51226196,  5.93101429,  6.44574617,
        7.10241982,  7.98507908,  9.26926293, 11.40957025, 16.21240486] 
# corresponding y axis values 
y = [np.arange(0,20,46)] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('lol') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 


# In[ ]:




