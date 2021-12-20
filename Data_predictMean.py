#!/usr/bin/env python
# coding: utf-8


# In[4]:


import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np

home = pd.read_csv("train.csv")
home.describe()
home["SalePrice"].mean()


# Mean value of the sales prices have found in the train set and applied to the test set.

# In[29]:


home_test = pd.read_csv("test.csv")
home_test
home_test.insert(80, "SalePrice",home["SalePrice"].mean())
home_test.head()
home_pred = pd.DataFrame(home_test, columns=['Id', 'SalePrice'])
home_pred.to_csv (r'C:\Users\omer.saldiran\Desktop\AI\Mining_Hw_3\export_dataframe.csv', index = False, header=True)


# In[ ]:




