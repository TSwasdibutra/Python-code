#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


#set workbook to show all columns (100 columns)
pd.set_option('display.max_columns', 100)
#set all number in workbook to have 2 decimals with clean format
pd.set_option('display.float_format', '{:,.2f}'.format)


# In[11]:


df = pd.read_excel(r'C:\Users\Thaya\Downloads\ds_survey.xlsx')
df


# In[6]:


df.columns


# In[12]:


df.dtypes


# In[13]:


#pull out month from datetime
df['month'] = df['Start Date'].dt.month
df


# In[41]:


#pull only relevant columns
dfa = df[['month', 'orderamount','Based on your recent shopping experience, how likely are you to recommend Central to your friends and family? - Group']].copy()
dfa


# In[43]:


#rename
dfa = dfa.rename({'Based on your recent shopping experience, how likely are you to recommend Central to your friends and family? - Group' : 'nps'}, axis = 'columns')
dfa


# In[37]:


#do 2 subset 1. aprl-jul 2. aug-oct


# In[44]:


#subset1
df1 = dfa.query('month < 8').copy().reset_index(drop=True)
df1


# In[67]:


df1pivot = df1.groupby('nps')[['orderamount']].mean().reset_index()
df1pivot


# In[68]:


#add category for plotting later
df1pivot['timeline'] = 'pre'
df1pivot


# In[69]:


#subset2
df2 = dfa.query('month > 7').copy().reset_index(drop=True)
df2


# In[70]:


df2pivot = df2.groupby('nps')[['orderamount']].mean().reset_index()
df2pivot


# In[71]:


#add category for plotting later
df2pivot['timeline'] = 'post'
df2pivot


# In[73]:


dfall = pd.concat([df1pivot, df2pivot])
dfall2 = dfall.reset_index(drop=True)
dfall2


# In[76]:


#show grouped bar chart
sns.barplot(x='nps', y='orderamount', hue='timeline', data=dfall2, color='c')


# In[77]:


#insights
#1.replatform result in higher AOV for passive group, which is a positive for the business
#2.however, promoter group has reduce the AOV after replatforming >> strategy to do is to deepdive specificly on this group
#need to come up with strategy to bring back AOV of promoter group based on the root cause above


# In[110]:


#indentify root-cause of promoter group by analyzing improve area column
#rename
df = df.rename({'Based on your recent shopping experience, how likely are you to recommend Central to your friends and family? - Group' : 'nps'}, axis = 'columns')
df


# In[111]:


dfpromoter = df.query('nps == "Promoter"').copy().reset_index()
dfpromoter


# In[112]:


dfpromoter = dfpromoter[['month','Thinking about your overall shopping experience, please select which of the following areas is most important or would like us to improve the most (Please select maximum 3 choices)']]
dfpromoter


# In[113]:


dfpromoter = dfpromoter.rename({'Thinking about your overall shopping experience, please select which of the following areas is most important or would like us to improve the most (Please select maximum 3 choices)' : 'improvearea'}, axis = 'columns')
dfpromoter


# In[114]:


#separate column by delimiter , 
#https://www.youtube.com/watch?v=YrDqysvOtAg&t=3s
dfpromoter[['improve1','improve2','improve3']] = dfpromoter['improvearea'].str.split(",", expand=True)
dfpromoter


# In[115]:


#choose only after replatform month (aug onwards)
dfpromoter2 = dfpromoter.query('month > 7').reset_index(drop=True)
dfpromoter2


# In[116]:


#create 3 subset


# In[117]:


#subset 1
dfpromoter2['improve1cal'] = dfpromoter2['improve1']


# In[118]:


dfimprove1 = dfpromoter2.groupby('improve1')[['improve1cal']].count().reset_index()
dfimprove1


# In[119]:


dfimprove1 = dfimprove1.rename({'improve1' : 'category'}, axis = 'columns')
dfimprove1


# In[120]:


#subset 2
dfpromoter2['improve2cal'] = dfpromoter2['improve2']


# In[121]:


dfimprove2 = dfpromoter2.groupby('improve2')[['improve2cal']].count().reset_index()
dfimprove2


# In[122]:


dfimprove2 = dfimprove2.rename({'improve2' : 'category'}, axis = 'columns')
dfimprove2


# In[123]:


#subset 3
dfpromoter2['improve3cal'] = dfpromoter2['improve3']


# In[124]:


dfimprove3 = dfpromoter2.groupby('improve3')[['improve3cal']].count().reset_index()
dfimprove3


# In[125]:


dfimprove3 = dfimprove3.rename({'improve3' : 'category'}, axis = 'columns')
dfimprove3


# In[130]:


#merge data on similar column
dfimproveall = dfimprove1.merge(dfimprove2, left_on='category', right_on='category', how='left')
dfimproveall


# In[131]:


dfimproveall = dfimproveall.merge(dfimprove3, left_on='category', right_on='category', how='left')
dfimproveall


# In[136]:


#replace NaN with 0
dfimproveall = dfimproveall.fillna(0)
dfimproveall


# In[137]:


dfimproveall['summary'] = dfimproveall['improve1cal'] + dfimproveall['improve2cal'] + dfimproveall['improve3cal']
dfimproveall


# In[138]:


dfimproveall.sort_values('summary', ascending=False).reset_index(drop=True)


# In[139]:


#change order and show only t
sns.barplot(x='summary',y='category', data=dfimproveall, color='c', order=['Promos/Discounts','Ease of navigation','Availability of items I want','Product quality','Product variety']);


# In[144]:


#use only improve from the first comment only
sns.barplot(x='improve1cal', y='category', data=dfimprove1, color='c');


# In[ ]:


#insights summary
#to improve AOV of promoter group after replatforming, we should 
#1 simplify customer journey of the new web and app
#2 educate this info by using CRM tools to send out email containing video explaining the walk through to these specific customer 

