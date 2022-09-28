#!/usr/bin/env python
# coding: utf-8

# In[8]:


# My first app
"""
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:





# In[9]:


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


# In[ ]:





# In[10]:


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


# In[11]:


dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


# In[12]:



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


# In[13]:


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




