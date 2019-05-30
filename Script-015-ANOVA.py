#!/usr/bin/env python
# coding: utf-8

# In[112]:


# Libraries
from __future__ import print_function
import scipy
import os

from statsmodels.compat import urlopen
import numpy as np
import statsmodels.api as sm
import pandas as pd
pd.set_option("display.width", 100)
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm

os.chdir('/Users/pauline/Documents/Python')

# Loading data
df = pd.read_csv("Tab-Morph.csv")
#print(df.head)
E = df.sedim_thick
M = df.plate_pacif
X = df.igneous_volc
S = df.slope_angle
                                     
#formula = 'E ~ C(M) + X'
#lm = ols(formula, df).fit()
#print(lm.summary())

cw_lm=ols('M ~ S + C(E)', data=df).fit() #Specify C for Categorical
print(sm.stats.anova_lm(cw_lm, typ=2))
print(cw_lm.summary())

cw_lm=ols('M ~ E + C(X)', data=df).fit() #Specify C for Categorical
print(sm.stats.anova_lm(cw_lm, typ=2))
print(cw_lm.summary())

#lm.model.exog[:5]

#lm.model.data.frame[:5]

#interX_lm = ols("S ~ C(E) * X + C(M)", df).fit()
#print(interX_lm.summary())

#interM_lm.model.exog
#interM_lm.model.exog_names

#rehab_lm = ols('S ~ C(E)', data=df).fit()
#table9 = anova_lm(rehab_lm)
#print(table9)
#print(rehab_lm.model.data.orig_exog)

#print(rehab_lm.summary())


# In[ ]:





# In[ ]:




