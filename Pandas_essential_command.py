#!/usr/bin/env python
# coding: utf-8

# In[11]:


#import useful library
import pandas as pd
import numpy as np


# In[12]:


#set workbook to show all columns (100 columns)
pd.set_option('display.max_columns', 100)


# In[97]:


#import dataset
df = pd.read_csv(r'C:\Users\Thaya\Downloads\ds_revenue_pandas.csv')
df


# In[99]:


#drop na
df.dropna(inplace=True, axis = 1)


# In[14]:


#show only first 10 columns
df.head(10)


# In[15]:


#show list of columns
df.columns


# In[16]:


#show data type
df.dtypes


# In[17]:


#show data type method 2
df.info(verbose=False)


# In[20]:


#show descriptive stats (for only the column with numnber)
df.describe()


# In[23]:


#show descriptive stats for non-numeric columns
df[['paid_type']].describe()


# In[24]:


#show number of row and column of dataset
df.shape


# In[25]:


#Subsetting Dataset


# In[26]:


#choose only some columns
#must use double [] becuz if use only [] you will get a serie of column name instead of dataframe
df[['paid_type','revenue']]


# In[27]:


#choose only some columns method 2 using .columsn function
#choose only first 2 columns
df[df.columns[:2]]


# In[29]:


#choose only last 2 columns
df[df.columns[-2:]]


# In[30]:


#chooose only columns with the text "type" using list comperehension
#list comprehension = shorten version of for loop
df[[i for i in df.columns if 'type' in i]]


# In[33]:


#choose column based on data types
df.select_dtypes('object')


# In[35]:


df.select_dtypes('float64')


# In[37]:


#select only some rows
#main functino for this are loc and iloc, which is a function to access the data by location 
#iloc = use index location
#loc = use the name as location (row and column number)
#can use boolean (true and false data) with loc
#use loc more than iloc


# In[41]:


#use iloc
#first number is row and second is column
df.iloc[0, 1]


# In[42]:


#pulll first 5 rows and first 2 columns using iloc
df.iloc[:5, :2]


# In[43]:


#pulll first 5 rows and last 2 columns using iloc
df.iloc[:5, -2:]


# In[44]:


#show only row 5 and show as dataframe (so need to use double [])
df.iloc[[5]]


# In[45]:


#select all rows but columns 1 and 2 only with iloc
df.iloc[:, [1,2]]


# In[50]:


#select all rows but last 2 columns only with iloc
df.iloc[:,[1,2]]


# In[51]:


df.iloc[:,[-2,-1]]


# In[52]:


#using loc instead of iloc
#select all row but only some columns
df.loc[:, ['paid_type', 'revenue']]


# In[53]:


#select columns based on boolean (true and false data)
#select only row with paid performance data
#step 1 boolean expressions
df['paid_type'] == 'Paid Performance'


# In[62]:


#step 2
df.loc[df['paid_type'] == 'Paid Performance']


# In[59]:


#multiple criteria for boolean expressions
df.loc[
    (df['paid_type'] == 'Paid Performance') & 
    (df['revenue'] > 200000)
]


# In[60]:


#select only the opposite value of the above using tilde
df.loc[~
       (df['paid_type'] == 'Paid Performance') & 
       (df['revenue'] > 200000)
      ]


# In[66]:


#using query function
#most common and similar to using loc[]
#it use string representation (writing word) of the boolean expression
df.query('revenue > 3000000')


# In[74]:


#two condition with query
df.query('(revenue > 3000000) & (paid_type == "Non Performance")')


# In[75]:


#summarize data (mean, min, max, var, std, count, sum, quantile)


# In[76]:


df['revenue'].mean()


# In[77]:


df['revenue'].min()


# In[78]:


df['revenue'].max()


# In[79]:


df['revenue'].var()


# In[80]:


df['revenue'].std()


# In[81]:


df['revenue'].count()


# In[82]:


df['revenue'].sum()


# In[83]:


df['revenue'].quantile(0.9)


# In[84]:


df['revenue'].quantile([0.25, 0.75])


# In[107]:


#summarize data for many columns
#step 1 create second numeric column
df['revenue2'] = df['revenue'] * 2
df


# In[108]:


#step 2
df[['revenue', 'revenue2']].mean()


# In[109]:


#run multiple stats on many columns using .agg()
df[['revenue', 'revenue2']].agg(['mean', 'min', 'max'])


# In[110]:


#show different stats for each columns
df[['revenue', 'revenue2']].agg(
    {'revenue':['min', 'max'],
    'revenue2':['mean']
    }
)


# In[111]:


#show sma estats for all columns
df[['revenue', 'revenue2']].agg(['mean', 'min', 'max', 'std', 'var'])


# In[112]:


#summarize non-numerical value


# In[113]:


#show all unique value
df['paid_type'].unique()


# In[114]:


#show number of unique value
df['paid_type'].nunique()


# In[115]:


#show all unique value with amount
df['paid_type'].value_counts()


# In[116]:


#show all unique value with amount as percentage
df['paid_type'].value_counts(normalize=True)


# In[118]:


#shift data which is sueful for time lagged data
df[['revenue']].shift(1)


# In[119]:


#shift data which is sueful for time lagged data
df[['revenue']].shift(-1)


# In[120]:


#shift with fillin missing value
df[['revenue']].shift(3, fill_value=0)


# In[121]:


#cumulative sum
df[['revenue']].cumsum()


# In[122]:


#cumulative min
df[['revenue']].cummin()


# In[123]:


#cumulative max
df[['revenue']].cummax()


# In[125]:


#calculate moving average of 5 values
df[['revenue']].rolling(windows=2).mean()


# In[126]:


#change minimum and maximum value to be within a range of 100000 and 2000000
df[['revenue']].clip(100000, 2000000)


# In[129]:


#Groupby = Pivot table in Pandas
df.groupby('paid_type')[['revenue']].mean()


# In[139]:


#pivot table with many stats
(
df
    .groupby('paid_type')[['revenue']]
    .agg(['mean', 'min', 'max', 'std', 'var'])
)


# In[140]:


#aggregate multiple column
(
df
    .groupby('paid_type')[['revenue', 'revenue2']]
    .agg(['mean', 'min', 'max', 'std', 'var'])
)


# In[141]:


#change the above from multi index columns to normal form
#step1 = recreate above table
df_pivot = (
df
    .groupby('paid_type')[['revenue', 'revenue2']]
    .agg(['mean', 'min', 'max', 'std', 'var'])
)


# In[142]:


#step2 reduce from multiindex to standard column
df_pivot.columns = ['_'.join(i) for i in df_pivot.columns]


# In[143]:


df_pivot


# In[144]:


#create new column


# In[145]:


df['average_revenue'] = df['revenue'].mean()
df


# In[146]:


#method 2 of creating new column using assign()
df = df.assign(average_revenue2 = df['revenue'].mean())
df


# In[147]:


#sorting data from min to max
df.sort_values('revenue')


# In[148]:


#sorting data from max to min
df.sort_values('revenue', ascending=False)


# In[149]:


#sorting column from only some columns
df[['captured_date', 'revenue', 'revenue2']].sort_values('revenue')


# In[151]:


#sort columns and reset index number
(
    df[['captured_date', 'revenue', 'revenue2']]
    .sort_values('revenue')
    .reset_index(drop=True)
)


# In[152]:


#handle missing values
#identify missing values as boolean
df.isna()


# In[154]:


#summarize totalcount of missing values in each column
df.isna().sum()
#can run sum() function on this as boolean value is actually 0 and 1 number


# In[155]:


#drop missing value
df.dropna()


# In[156]:


#drop missing value only in specific column (revenue column)
df.dropna(subset=['revenue'])


# In[157]:


#fill in missing value with 1
df.fillna(1)


# In[159]:


#fill in missing value with average value of that column
(
    df['revenue']
    .fillna(df['revenue']
            .mean())
)


# In[160]:


#combine 2 dataset


# In[163]:


#create 2 dataset
df1 = df.query('paid_type == "Non Performance"').copy()
df1

df2 = df.query('paid_type == "Paid Performance"').copy()
df2


# In[164]:


#stack 2 dataset on top of each other
pd.concat([df1, df2])


# In[165]:


#merge data on similar column
pd.merge(df1, df2, on=['captured_date'])


# In[168]:


#merge data on similar column and change new duplicate column name
pd.merge(df1, df2, on=['captured_date'], suffixes=('_organic','_paid'))


# In[167]:


#method 2
df1.merge(df2, how='left')


# In[ ]:




