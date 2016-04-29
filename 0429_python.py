
# coding: utf-8

# In[1]:

joke4 = '''老師今天出個功課叫我們問兄弟姊妹遇到壞人怎麼做。
小龍回家問弟弟遇到壞人怎麼做？
弟弟回答：我會狠狠的擊敗他，然後用獎金去吃大餐。
隔天小龍去上學。
老師問：功課有做嗎？
小龍：有！我會狠狠的擊敗他，然後用獎金去吃大餐。
老師當場昏倒'''
print(joke4)


# In[16]:

joke3 = ['笑話', '不好笑', '不用錢']
joke3_join = ','.join(joke3)
print('提示:',joke3_join)


# In[2]:

joke4[:2]


# In[12]:

print(joke4[::7])


# In[13]:

print(joke4[4:20:3])


# In[14]:

joke4.split(' ')


# In[15]:

joke4.split()


# In[3]:

len(joke4)


# In[19]:

joke4.startswith('老師')


# In[5]:

word = '擊敗'
joke4.find(word)


# In[6]:

joke4[51:53]


# In[7]:

joke4.rfind(word)


# In[8]:

joke4.count(word)


# In[9]:

import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding = "big5"
book1 = response.text


# In[10]:

word2 = "他"
book1.count(word2)


# In[11]:

book1 = 'cooking or cookery is the art of preparing food for consumption with the use of heat...'
book1.strip('.')


# In[20]:


book1.replace('of', '的')


# In[ ]:



