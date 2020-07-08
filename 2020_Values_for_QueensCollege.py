#!/usr/bin/env python
# coding: utf-8

# In[10]:


# code for a typical timeseries (via PANDAS)
#importing packages
import pandas as pa
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog as fd
import matplotlib.pyplot as plt


# In[11]:


#importing an example file (PM 2.5 Concentrations)
test_file = fd.askopenfilename()
with open(test_file) as FID:
    df = pa.read_csv(FID, delim_whitespace = False, dtype = 'str')


# In[12]:


df


# In[37]:


#finding the important parameters
Mean = df['Arithmetic Mean']
Date = df['Date (Local)']
MaxV = df['First Maximum Value']


# In[38]:


# setting the max value and mean to a float value
MaxV = MaxV.astype('float16')
Mean = Mean.astype('float16')


# In[43]:


# making the graph a bit nicer
import seaborn
seaborn.set()


# In[48]:


# make the date into datetime objects
Date_format = pa.to_datetime(Date, format = '%Y-%m-%d')
Date_format


# In[75]:


#plot the graph
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(Date_format, Mean, color = 'red' )
ax.set_title('PM2.5 Concentrations for Site: Queens College')
ax.set_xlabel('Date')
ax.set_ylabel('Mean PM2.5')
fig.savefig('PM2.5(QC).png')
#what's causing these trends? (try smoothing out the data, look at past years(seasonal trend?))


# In[67]:


#importing an example file (NO2 Concentrations)
test_file = fd.askopenfilename()
with open(test_file) as FID:
    df_2 = pa.read_csv(FID, delim_whitespace = False, dtype = 'str')


# In[69]:


df_2


# In[71]:


#finding the important parameters
Mean_1 = df_2['Arithmetic Mean']
Date_1 = df_2['Date (Local)']
MaxV_1 = df_2['First Maximum Value']


# In[72]:


#changing to float value
Mean_1 = Mean_1.astype('float16')
MaxV_1 = MaxV_1.astype('float16')


# In[73]:


Date_NO2 = pa.to_datetime(Date_1, format = "%Y-%m-%d")
Date_NO2


# In[74]:


#plot the graph
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(Date_NO2, Mean_1, color = 'blue' )
ax.set_title('NO2 Concentrations for Site: Queens College')
ax.set_xlabel('Date')
ax.set_ylabel('Mean NO2')
fig.savefig('NO2(QC).png')


# In[78]:


#importing an example file (Ozone Concentrations)
test_file = fd.askopenfilename()
with open(test_file) as FID:
    df_3 = pa.read_csv(FID, delim_whitespace = False, dtype = 'str')


# In[79]:


df_3


# In[80]:


#important parameters
Mean_2 = df_3['Arithmetic Mean']
Date_2 = df_3['Date (Local)']
MaxV_2 = df_3['First Maximum Value']


# In[81]:


#changing to float value
Mean_2 = Mean_2.astype('float16')
MaxV_2 = MaxV_2.astype('float16')


# In[83]:


#changing str to datetime objects
Date_O = pa.to_datetime(Date_2, format = '%Y-%m-%d')
Date_O


# In[89]:


#creating a graph for ozone concentrations for Queens College
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(Date_O, Mean_2, color = 'green' )
ax.set_title('Ozone Concentrations for Site: Queens College')
ax.set_xlabel('Date')
ax.set_ylabel('Mean Ozone(O3)')
fig.savefig('O(QC).png')


# In[90]:


#importing an example file (SO2 Concentrations)
test_file = fd.askopenfilename()
with open(test_file) as FID:
    df_4 = pa.read_csv(FID, delim_whitespace = False, dtype = 'str')


# In[91]:


df_4


# In[93]:


#important parameters
Mean_3 = df_4['Arithmetic Mean']
Date_3 = df_4['Date (Local)']
MaxV_3 = df_4['First Maximum Value']


# In[94]:


#changing to float value
Mean_3 = Mean_3.astype('float16')
MaxV_3 = MaxV_3.astype('float16')


# In[95]:


#changing to datetime objects
Date_SO2 = pa.to_datetime(Date_3, format ='%Y-%m-%d')
Date_SO2


# In[96]:


#creating a graph for ozone concentrations for Queens College
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(Date_SO2, Mean_3, color = 'black' )
ax.set_title('SO2 Concentrations for Site: Queens College')
ax.set_xlabel('Date')
ax.set_ylabel('Mean SO2')
fig.savefig('SO2(QC).png')

