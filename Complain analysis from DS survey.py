#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import seaborn as sns


# In[6]:


#set workbook to show all columns (100 columns)
pd.set_option('display.max_columns', 100)
#set all number in workbook to have 2 decimals with clean format
pd.set_option('display.float_format', '{:,.2f}'.format)


# In[9]:


df = pd.read_excel(r'C:\Users\Thaya\Downloads\survey.xlsx')
df


# In[10]:


df.columns


# In[11]:


#only relevant columns
df_analysis = df[['improve1', 'improve2', 'improve3']].copy()
df_analysis


# In[12]:


#create 3 subset


# In[28]:


#subset 1
df_analysis['improve1cal'] = df_analysis['improve1']


# In[35]:


df1 = df_analysis.groupby('improve1')[['improve1cal']].count().reset_index()
df1


# In[41]:


df1 = df1.rename({'improve1' : 'category'}, axis = 'columns')
df1


# In[36]:


#subset 2
df_analysis['improve2cal'] = df_analysis['improve2']
df2 = df_analysis.groupby('improve2')[['improve2cal']].count().reset_index()
df2


# In[40]:


df2 = df2.rename({'improve2' : 'category'}, axis = 'columns')
df2


# In[37]:


#subset 3
df_analysis['improve3cal'] = df_analysis['improve3']
df3 = df_analysis.groupby('improve3')[['improve3cal']].count().reset_index()
df3


# In[42]:


df3 = df3.rename({'improve3' : 'category'}, axis = 'columns')
df3


# In[47]:


#merge data on similar column
dfall = pd.merge(df1, df2, on=['category'])
dfall


# In[48]:


dfall = pd.merge(dfall, df3, on=['category'])
dfall


# In[49]:


dfall['summary'] = dfall['improve1cal'] + dfall['improve2cal'] + dfall['improve3cal']
dfall


# In[53]:


dfall.sort_values('summary', ascending=False).reset_index(drop=True)


# In[60]:


#horizontal barplot
sns.barplot(x='summary',y='category', data=dfall);


# In[61]:


#with different color
sns.barplot(x='summary',y='category', data=dfall,color='c');


# In[64]:


#change order and show only t
sns.barplot(x='summary',y='category', data=dfall, color='c', order=['Promos/Discounts','Availability of items I want','Product quality','Home Delivery','Ease of check-out']);


# In[ ]:




