#!/usr/bin/env python
# coding: utf-8

# # Bank Account
# 
# 
# 

# In[4]:


class bankaccount():
    def __init__(self,ownername,balance):
        self.ownername = ownername
        self.balance = balance
        
    def methode(self):   
        if I == 1:
            d = int(input("the deposite amount: "))
            total_balance = d+v.balance
            print("your total account balance is: ",total_balance)
        else:
            w = int(input("the withdraw amount: "))
            if w <= v.balance:
                total_balance =  v.balance - w
                print("your available account balance is: ",total_balance)
            else:
                print("You have insufficient balance")   
    



    


# In[5]:


v=bankaccount('pradip',8000) 
print(v.ownername)
print(v.balance)
I = int(input("for deposit type 1, for withdraw type 2 "))
v.methode()


# In[ ]:




