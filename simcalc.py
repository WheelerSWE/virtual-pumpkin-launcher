#!/usr/bin/env python
# coding: utf-8

# In[]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[]:


dt = .001
m = 10
k = 1
v = 50
theta = 50

g = 9.81


# In[]:


time_steps = np.arange(0, 5, dt)

x_pos = np.empty(shape=time_steps.shape)
y_pos = np.empty(shape=time_steps.shape)

x_x = 0
x_y = 0

v_x = v*math.cos(theta*math.pi/180)
v_y = v*math.sin(theta*math.pi/180)

for _ in time_steps:
    a_x = (-k*np.sqrt(v_x**2 + v_y**2)*v_x)/m
    a_y = (-k*np.sqrt(v_x**2 + v_y**2)*v_y - m*g)/m
    
    dv_x = a_x*dt
    dv_y = a_y*dt

    x_x = x_x+(v_x*dt)
    x_y = x_y+(v_y*dt)
    
    v_x = v_x+(dv_x)
    v_y = v_y+(dv_y)
    
    x_pos = np.append(x_pos, x_x)
    y_pos = np.append(y_pos, x_y)


# In[]:


plt.plot(x_pos, y_pos)
plt.xlim(0, 20)
plt.ylim(0, 12)
plt.show()

