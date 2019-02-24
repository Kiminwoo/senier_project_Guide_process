#!/usr/bin/env python
# coding: utf-8

# In[6]:


from math import sqrt


# In[3]:


def distance(data, name1, name2):
    sum=0
    for i in data[name1]: 
        if i in data[name2]:
            sum+=pow(data[name1][i]- data[name2][i],2)
    return 1/(1+sqrt(sum))


# In[4]:


critics={

    'hhd':{'guardians of the galaxy 2':5,'christmas in august':4,'boss baby':1.5},

    'chs':{'christmas in august':5,'boss baby':2},

    'kmh':{'guardians of the galaxy 2':2.5,'christmas in august':2,'boss baby':1},

    'leb':{'guardians of the galaxy 2':3.5,'christmas in august':4,'boss baby':5}

}


# In[7]:


distance(critics,'chs','leb')


# In[28]:


li=[]

def match(data,name,index=3,distance_function=distance):
    
  
    for i in data:
        if name != i: # 자기 자신은 제외
            li.append((distance_function(data,name,i),i)) 
            # 유사도 , 이름을 튜플에 묶어 리스트에 추가한다 .
    
    li.reverse() # 내림차순 정렬 

    
    return li[:index]


# In[29]:


match(critics,'chs')


# In[11]:


import matplotlib.pyplot as plt


# In[34]:


def barchart(data, labels): # data , labels 는 list 형태로 사용 
    positions = range(len(data))
    plt.barh(positions, data, height=0.5,color='r') #가로
    plt.yticks(positions, labels)
    plt.xlabel('similarity') #x축
    plt.ylabel('name') #y축
    plt.show #출력 


# In[30]:


score = []
names = []

for i in li:
    score.append(i[0]) #점수를 담는다.
    names.append(i[1]) #이름을 담는다.


# In[31]:


score


# In[32]:


names


# In[35]:


barchart(score,names)


# In[ ]:




