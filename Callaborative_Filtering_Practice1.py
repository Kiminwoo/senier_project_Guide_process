#!/usr/bin/env python
# coding: utf-8

# In[13]:


critics={
    'hhd':{'guardians of the galaxy 2':5,'christmas in august':4,'boss baby':1.5},
    'chs':{'christmas in august':5,'boss baby':2},
    'kmh':{'guardians of the galaxy 2':2.5,'christmas in august':2,'boss baby':1},
    'leb':{'guardians of the galaxy 2':3.5,'christmas in august':4,'boss baby':5}
}


# In[3]:


critics.get('hhd')


# In[4]:


critics.get('hhd').get('boss baby')


# In[5]:


from math import sqrt


# In[6]:


sqrt(pow(1,2)+pow(3,2))


# In[7]:


def sim(i,j):
    return sqrt(pow(i,2)+pow(j,2))


# In[9]:


var1 = critics['chs']['christmas in august']-critics['leb']['christmas in august']
var2 = critics['chs']['boss baby']-critics['leb']['boss baby']
sim(var1,var2)


# In[14]:


for i in critics:
    if i!='chs':
        num1 = critics.get('chs').get('christmas in august')- critics.get(i).get('christmas in august')
        num2 = critics.get('chs').get('boss baby')- critics.get(i).get('boss baby')
        print(i," : ", sim(num1,num2))
        


# In[15]:


for i in critics:
    if i != 'chs':
        num1 = critics.get('chs').get('christmas in august')- critics.get(i).get('christmas in august')
        num2 = critics.get('chs').get('boss baby')- critics.get(i).get('boss baby')
        print(i," : ", 1/(1+sim(num1,num2)))


# In[ ]:




