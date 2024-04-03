#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Fungsi untuk menghitung kombinasi (n choose k)
def n_choose_k(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# Fungsi untuk menghitung probabilitas P(X=k) dalam distribusi binomial
def binomial_probability(n, k, p):
    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parameter distribusi binomial
n = 10  # jumlah percobaan
p = 0.5  # probabilitas keberhasilan dalam satu percobaan
k = 3  # jumlah keberhasilan yang diinginkan

# Menghitung probabilitas P(X=k) untuk distribusi binomial
prob_binomial = binomial_probability(n, k, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[5]:


from scipy.stats import binom

n = 10
p = 0.5
k = 3

prob_binomial = binom.pmf(k, n, p)
print("probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[ ]:




