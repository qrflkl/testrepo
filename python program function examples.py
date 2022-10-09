#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


def getAnswer(answerNumber):
    if answerNumber == 1:
           return 'It is certain'
    elif answerNumber == 2:
           return 'It is decidedly so'
    elif answerNumber == 3:
           return 'Yes'
    elif answerNumber == 4:
           return 'Reply hazy try again'
    elif answerNumber == 5:
           return 'Ask again later'
    elif answerNumber == 6:
           return 'Concentrate and ask again'
    elif answerNumber == 7:
           return 'My reply is no'
    elif answerNumber == 8:
           return 'Outlook not so good'
    elif answerNumber == 9:
           return 'Very doubtful'


# In[12]:


print(getAnswer(random.randint(1, 9)))


# In[6]:


r


# In[11]:


r = random.randint(1, 9)
print(r)
fortune = getAnswer(r) 
print(fortune)


# In[13]:


print('hello', end="")
print('sydney')


# In[15]:


print('dog','cat','mouse',sep='=')


# In[17]:


def spam():
    eggs =99
    bacon()
    print(eggs)


# In[19]:


def bacon():
    ham =101
    eggs=0
    
spam()


# In[22]:


def spam():
    print(eggs)


# In[23]:


eggs =42
spam()


# In[25]:


def spam():
    global eggs
    eggs = 'hello' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)


# In[35]:


def divby (num):
    try:
        return 42 / num
    except :
        print('Error: you try to divide by zero')
    
    


# In[36]:


print(divby(2))
print(divby(7))
print(divby(0))
print(divby(10))


# In[37]:


print('how many cats do you have')
numCats =input()
try:
    if int(numCats)>=4:
        print('that is a lot of cats')
    else:
        pirnt('that is not many cats')
except ValueError:
    print('you did not enter a number')


# In[38]:


list('Tuesday')


# In[39]:


cat=['fat','orange','loud']


# In[40]:


size, color, disposition =cat


# In[41]:


size


# In[42]:


color


# In[43]:


disposition


# In[44]:


size, color, disposition ='skinny','black','quiet'


# In[45]:


size


# In[46]:


color


# In[47]:


disposition


# In[48]:


a ='AAA'
b ='BBB'


# In[49]:


a, b = b, a


# In[51]:


a


# In[52]:


b


# In[53]:


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)


# In[54]:


print('4 scores and 7' +     ' years ago')


# In[55]:


eggs ={'name':'Zophie','species':'cat','age':8}


# In[57]:


list(eggs.keys())


# In[58]:


list(eggs.values())


# In[59]:


list(eggs.items())


# In[60]:


for k in eggs.keys():
    print(k)


# In[61]:


for v in eggs.values():
    print(v)


# In[62]:


for k, v in eggs.items():
    print(k,v)


# In[63]:


'cat' in eggs.values()


# In[64]:


eggs['color']


# In[67]:


if 'color' in eggs:
    print(eggs['color'])
else:
    print( 'color is unknwon')


# In[68]:


eggs


# In[69]:


eggs.get('age',0)


# In[70]:


eggs.get('color','')


# In[71]:


if 'color' not in eggs:
    eggs['color']='black'


# In[72]:


eggs


# In[74]:


eggs.setdefault('color','black')


# In[75]:


eggs


# In[76]:


eggs.setdefault('color','white')


# In[77]:


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message: #for each letter in the message
    count.setdefault(character, 0)  #set default count of each character as 0, e.g.
    #if 'I' not exist then default value is 0
    count[character] = count[character] + 1 #easch character key, calculate the value

print(count)


# In[78]:


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper(): #for each letter in the message
    count.setdefault(character, 0)  #set default count of each character as 0, e.g.
    #if 'I' not exist then default value is 0
    count[character] = count[character] + 1 #easch character key, calculate the value

print(count)


# In[ ]:




