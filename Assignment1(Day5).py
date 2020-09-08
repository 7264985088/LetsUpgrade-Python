#!/usr/bin/env python
# coding: utf-8

# # LIST
# Is sublist present in list

# In[1]:



lst1 =[1,4,6,7,3,7,1,2,4,5]
lst2 =[1,1,5]
check = all(item in lst1 for item in lst2)
if check is True:
    print("It's a match")
else:
    print("It's gone")


# In[ ]:





# In[ ]:




