# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:18:26 2019

@author: sai teja
"""

import pandas as pd
import seaborn as sns
data = pd.read_csv("B:\\data science\\Python\\datasets\\bankloan.csv")
len(data)
data.columns
#--barplot
sns.barplot(x='marital',y='balance',data=data)
sns.barplot(x='loan',y='day',data=data)
sns.barplot(x='education',y='balance',data=data)
#---countplot
sns.countplot(x='loan',data=data)
sns.countplot(x='education',data=data)
sns.countplot(x='job',data=data)
sns.countplot(x='marital',data=data)
sns.countplot(x='housing',data=data)
sns.countplot(x='month',data=data)
#--boxplot
sns.boxplot(x='housing',y='balance',data=data,hue='loan')
sns.boxplot(x='housing',y='age',data=data,hue='loan')
sns.boxplot(x='education',y='age',data=data,hue='loan')
sns.boxplot(x='job',y='age',data=data,hue='loan')
sns.boxplot(x='loan',y='day',data=data,hue='month')
##voilen plot
sns.violinplot(x='loan',y='day',data=data,hue='month')
sns.violinplot(x='housing',y='balance',data=data,hue='loan')
sns.violinplot(x='education',y='age',data=data,hue='loan')





