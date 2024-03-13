#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, -5, 0.3, 6, -2, 4] # numeric vector
b = ["one", "two", "three"] # character vector
c = [True, True, True, False, True] # logical vector
print(a)
print(b)
print(c)


# In[12]:


#MATRIKS
import numpy as np
cells = [3,15,-27,38]
r_adit = ["R1","R2"]
c_adit = ["C1","C2"]
adit_matrix = np.matrix(cells).reshape(2,2)
print(adit_matrix)


# In[11]:


import pandas as pd
import numpy as np

adit1 = [1, 2, 3, 4]
adit2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
adit3 = [True, True, True, False]

dataku = pd.DataFrame({'ID': adit1, 'Color': adit2, 'Passed': adit3})
print(dataku)


# In[9]:


import pandas as pd

data_nama = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_nama)


# In[13]:


pip install mysql-connector-python


# In[42]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices1"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM adit_houseprices;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[43]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Brick'] == 'No']

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[44]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['Brick'] == 'No') | (df['Neighborhood'] == 'East')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:




