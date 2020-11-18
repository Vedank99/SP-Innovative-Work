#!/usr/bin/env python
# coding: utf-8

# # Black Scholes Equation
# #### by
# <ul>
#     <li>Vedank Goyal 2K18/MC/122</li>
#     <li>Sarthak Singh 2K18/MC/103</li>
# </ul>

# ### Importing the necessary libraries

# In[15]:


import numpy as np
import scipy.stats as si


# ### Defining the equation

# In[16]:


def BlackScholes(S, K, T, r, sigma, option = 'call'):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result


# ### Defining the option
# <ul>
#     <li>Strike Price (S) = 50 U.S.D</li>
#     <li>Spot Price (K) = 100 U.S.D</li>
#     <li>Time to maturity (T) = 1 year</li>
#     <li>Interest Rate (r) = 0.05</li>
#     <li>Volatility (sigma) = 0.25</li>
# </ul>

# In[17]:


S = 50
K = 100
T = 1
r = 0.05
sigma = 0.25


# ### Calculating the price of Call Option

# In[18]:


call_option_price = BlackScholes(S, K, T, r, sigma, option = 'call')
call_option_price


# ### Calculating the price of Put Option

# In[19]:


put_option_price = BlackScholes(S, K, T, r, sigma, option = 'put')
put_option_price

