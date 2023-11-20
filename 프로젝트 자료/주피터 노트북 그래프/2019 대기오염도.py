#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


dust = pd.read_csv("C:/Users/klose/Desktop/jupyter/seoul_dust(2019) 하루.csv", index_col=0)
dust


# In[3]:


dust.info()


# #### PM10 미세먼지 분포

# In[4]:


dust["PM10"].value_counts()


# In[5]:


dust.describe()


# #### 종류별 대기오염도

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
dust.hist(bins=50, figsize=(20,15))
plt.show()

