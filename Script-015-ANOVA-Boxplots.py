#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import os
import scipy
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.compat import urlopen
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.api import interaction_plot, abline_plot
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
pd.set_option("display.width", 100)

os.chdir('/Users/pauline/Documents/Python')

df = pd.read_csv("Tab-Morph.csv")

fig = plt.figure(figsize=(16.0, 12.0), dpi=300)
fig.suptitle('ANOVA boxplots of the observation sample distribution',
             fontsize=10, fontweight='bold', x=0.5, y=0.99
             )

# subplot 1
ax = fig.add_subplot(221)
plt.subplots(figsize=(8,6))
df.boxplot('slope_angle', 'slope_class', ax=ax, grid=False)

# subplot 2
ax = fig.add_subplot(222)
plt.subplots(figsize=(8,6))
df.boxplot('sedim_thick', 'slope_class', ax=ax, grid=False)

# subplot 3
ax = fig.add_subplot(223)
plt.subplots(figsize=(8,6))
df.boxplot('igneous_volc', 'slope_class', ax=ax, grid=False)

# subplot 4
ax = fig.add_subplot(224)
plt.subplots(figsize=(8,6))
df.boxplot('tg_angle', 'slope_class', ax=ax, grid=False)

# visualize
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.25, wspace=0.35
                    )
plt.savefig('plot_ANOVAbox.png', dpi=300)
plt.show()
