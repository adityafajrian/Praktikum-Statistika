#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
# Membuat dataframe dari data yang disalin ke clipboard
df = pd.read_clipboard()

print(df)


# In[16]:


df


# In[14]:


rata_tinggi = df['Tinggi (cm)'].mean()
rata_tinggi


# In[15]:


mean(data_nama$Tinggi.Badan)


# In[17]:


print(df .dtypes)


# In[18]:


df['Angkatan'] = df['Angkatan'].astype(str)


# In[19]:


print(df.dtypes)


# In[7]:


import pandas as pd

# Menyediakan path lengkap ke file jika file berada di lokasi yang berbeda
df = pd.read_csv("C:\prakprob/Biodata2.csv")
df


# In[10]:


import pandas as pd

df = pd.read_excel("C:\prakprob/Biodata1.xlsx")
df


# In[13]:


import pandas as pd

data_nama = pd.read_csv("C:/prakprob/Biodata2.csv")


# In[ ]:




