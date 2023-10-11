#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('/Users/anastasiabuglakova/Documents/GEEK/Итоговая контрольная работа по блоку специализация аналитика/Копия Премиум авто - Маркетинговые данные.csv')
new_df = df[['Client ID', 'Device Category', 'Date', 'Medium']] 
new_df.sample(10)


# In[2]:


new_df=new_df.sort_values(by = "Date")
new_df.sample(10)
print(type(new_df["Date"][0]))


# In[3]:


for i in range(len(new_df["Date"])):
    new_df["Date"][i] = new_df["Date"][i].replace(" февраля ", '.02.').replace(" января ", '.01.').replace(" г.", '')
print((new_df["Date"][10]))
print(type(new_df["Date"][10]))
new_df["Date"].sample(10)


# In[4]:


new_df.sample(10)


# In[5]:


from datetime import date
for i in range(len(new_df["Date"])):
    new_df["Date"][i] = date(int(new_df["Date"][i].split(".")[2]), 
                             int(new_df["Date"][i].split(".")[1]), 
                             int(new_df["Date"][i].split(".")[0]))
    


# In[6]:


new_df.sample(10)


# In[7]:


for i in range(len(new_df["Device Category"])):
    new_df["Device Category"][i] = new_df["Device Category"][i] + "=>"
    new_df["Medium"][i] = new_df["Medium"][i] + "=>"


# In[8]:


new_df = new_df .sort_values(["Client ID","Date"], ascending=[True, True])
new_df.head(10)


# In[9]:


table = new_df.pivot_table(index = 'Client ID',
            
            values = ['Device Category', 'Medium'],
            aggfunc = 'sum',
            fill_value = 0).reset_index()
table


# In[10]:


def my_count(s):
    return s.count("=>")- s.count("none")
table['q_medium'] = table['Medium'].apply(my_count)
table['q_devise'] = table['Device Category'].apply(my_count)
table.sample(12)


# In[11]:


table.head(12)
table.to_csv (r'/Users/anastasiabuglakova/Documents/GEEK/Итоговая контрольная работа по блоку специализация аналитика/my_data2.csv', index= False )


# In[ ]:




