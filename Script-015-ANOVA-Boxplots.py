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
from statsmodels.compat import urlopen
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.api import interaction_plot, abline_plot
#
os.chdir('/Users/pauline/Documents/Python')
#
# Load data
df = pd.read_csv("Tab-Morph.csv")
#
fig, ax = plt.subplots(figsize=(8,6))
fig = df.boxplot('slope_angle', 'slope_class', ax=ax, grid=False)
#
fig, ax = plt.subplots(figsize=(8,6))
fig = df.boxplot('sedim_thick', 'slope_class', ax=ax, grid=False)
#
fig, ax = plt.subplots(figsize=(8,6))
fig = df.boxplot('igneous_volc', 'slope_class', ax=ax, grid=False)
#
fig, ax = plt.subplots(figsize=(8,6))
fig = df.boxplot('tg_angle', 'slope_class', ax=ax, grid=False)
#
plt.show()
