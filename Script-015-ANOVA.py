#!/usr/bin/env python
# coding: utf-8
#
from __future__ import print_function
import scipy
import os
import numpy as np
import pandas as pd
pd.set_option("display.width", 100)
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.compat import urlopen
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
#
os.chdir('/Users/pauline/Documents/Python')
#
# Load data
df = pd.read_csv("Tab-Morph.csv")
#
E = df.sedim_thick
M = df.plate_pacif
X = df.igneous_volc
S = df.slope_angle
#
cw_lm=ols('M ~ S + C(E)', data=df).fit() #Specify C for Categorical
print(sm.stats.anova_lm(cw_lm, typ=2))
print(cw_lm.summary())
#
cw_lm=ols('M ~ E + C(X)', data=df).fit() #Specify C for Categorical
print(sm.stats.anova_lm(cw_lm, typ=2))
print(cw_lm.summary())
