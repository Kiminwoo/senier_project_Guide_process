#!/usr/bin/env python
# coding: utf-8

# In[18]:


critics = {
    '김인우': {
        '택시운전사': 2.5,
        '남한산성': 3.5,
        '킹스맨:골든서클': 3.0,
        '범죄도시': 3.5,
        '아이 캔 스피크': 2.5,
        'The Night Listener': 3.0,
    },
    '김인우1': {
        '택시운전사': 1.0,
        '남한산성': 4.5,
        '킹스맨:골든서클': 0.5,
        '범죄도시': 1.5,
        '아이 캔 스피크': 4.5,
        'The Night Listener': 5.0,
    },
    '김인우2': {
        '택시운전사': 3.0,
        '남한산성': 3.5,
        '킹스맨:골든서클': 1.5,
        '범죄도시': 5.0,
        'The Night Listener': 3.0,
        '아이 캔 스피크': 3.5,
    },
    '김인우3': {
        '택시운전사': 2.5,
        '남한산성': 3.0,
        '범죄도시': 3.5,
        'The Night Listener': 4.0,
    },
    '김인우4': {
        '남한산성': 3.5,
        '킹스맨:골든서클': 3.0,
        'The Night Listener': 4.5,
        '범죄도시': 4.0,
        '아이 캔 스피크': 2.5,
    },
    '김인우5': {
        '택시운전사': 3.0,
        '남한산성': 4.0,
        '킹스맨:골든서클': 2.0,
        '범죄도시': 3.0,
        'The Night Listener': 3.5,
        '아이 캔 스피크': 2.0,
    },
    '김인우6': {
        '택시운전사': 3.0,
        '남한산성': 4.0,
        'The Night Listener': 3.0,
        '범죄도시': 5.0,
        '아이 캔 스피크': 3.5,
    },
    '김인우7': {'남한산성': 4.5, '아이 캔 스피크': 1.0,
             '범죄도시': 4.0},
}


# In[2]:


from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/HYSUPB.TTF").get_name()
rc('font', family=font_name)


# In[44]:


plt.figure(figsize=(14,8))
plt.plot([1,2,3],[1,2,3],'g^') # 각각의 값과 점의 모양설정
plt.text(1,1,'a') #텍스트 찍기
plt.text(2,2,'b')
plt.text(3,3,'c')
# 각 축의 크기 설정

plt.axis([0,6,0,6])
# 그래프의 x축,y축 크기설정
plt.show()


# In[4]:


import matplotlib.pyplot as plt


# In[6]:


def drawGraph(data,name1,name2): # critics data 이용해 scatter plot 그리기 
    plt.figure(figsize=(14,8)) # plot 크기설정 
    
    # plot 좌표를 위한 list 선언 
    li = []
    li2 =[]
    
    for i in critics[name1]: # i = 키 값 
        if i in data[name2]: # 같은 영화를 평가했을 때만 
            li.append(critics[name1][i]) # name1의 평점 li[]에 추가 
            li2.append(critics[name2][i]) # name2의 평점 li2[]에 추가 
            plt.text(critics[name1][i],critics[name2][i],i) # 영화 제목 text 찍기
    
    plt.plot(li,li2,'ro') # plot그리기
    
    #각 축의 크기 설정 (0~6까지)
    plt.axis([0,6,0,6])
    
    # x축과 y축 이름 설정 
    plt.xlabel(name1)
    plt.ylabel(name2)
    
    #그리기
    plt.show()
            


# In[7]:


drawGraph(critics,'김인우','김인우1')


# In[11]:


def pearson(data,name1,name2):
    sumX=0
    sumY=0
    sumPowX=0
    sumPowY=0
    sumXY=0
    count=0
    
    for i in data[name1]: # i = key 
        if i in data[name2]: # 같은 영화를 평가했을 때만
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
    
    return ( sumXY- ((sumX*sumY)/count) )/ sqrt( (sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2)/count)))


# In[48]:


pearson(critics,'김인우','김인우7')


# In[10]:


from math import sqrt


# In[45]:


drawGraph(critics,'김인우','김인우7')


# In[22]:


drawGraph(critics,'김인우','김인우6')


# In[15]:


pearson(critics,'김인우','김인우3')


# In[16]:


pearson(critics,'김인우','김인우5')


# In[20]:


pearson(critics,'김인우','김인우7')


# In[23]:


pearson(critics,'김인우','김인우6')


# In[34]:


def match(data, name, index=3, function=pearson):
    li=[]    
        
    for i in data: #딕셔너리를 돌고
        if name != i: #자기 자신이 아닐때만 
            li.append((function(data,name,i),i))
            # function을 통해 상관계수를 구하고 li[]에 추가 
    li.reverse() # 내림차순
    
    return li[:index]


# In[49]:


match(critics,'김인우',6)


# In[61]:


def getRecommendation(data,person,function=pearson):
    result = match(critics,person,len(data))
    
    simsum=0  #유사도 합을 위한 변수 
    score=0  # 평점 합을 위한 변수 
    li=[]  #리턴을 위한 리스트 
    score_dic={}  #유사도 총합을 위한 dic 
    sim_dic={}  #평점 총합을 위한 dic 
    
    for sim,name in result: # 튜플이기 때문에 한번에 처리 
        if sim<0 : continue # 유사도가 양수인 사람만 
        for movie in data[name]:
            if movie not in data[person]: #name이 평가를 내리지 않은 영화 
                score += sim*data[name][movie] # 그사람의 영화평점 * 유사도
                score_dic.setdefault(movie,0) # 기본값 설정
                score_dic[movie] +=score # 합계
                
                #조건에 맞는 사람의 유사도의 누적합을 구함 
                sim_dic.setdefault(movie,0)
                sim_dic[movie] += sim
            
            score = 0 # 영화가 바뀌었으니 초기화한다 . 
    
    for key in score_dic:
        score_dic[key]=score_dic[key]/sim_dic[key] # 평점 총합/ 유사도 총합 
        li.append((score_dic[key],key)) # list((tuple)) 의 리턴을 위해서 
    
    li.sort() # 내림차순 
    
    return li 
                
            


# In[62]:


getRecommendation(critics, '김인우7')


# In[ ]:




