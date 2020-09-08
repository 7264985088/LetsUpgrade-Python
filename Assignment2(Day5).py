#!/usr/bin/env python
# coding: utf-8

# # Assignment2(Day5)

# #print prime number

# In[5]:


def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True
number = filter(prime, range(2500))
print(list(number))


# In[3]:





# In[ ]:




