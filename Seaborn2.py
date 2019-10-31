# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:22:01 2019

@author: sai teja
"""

"""In this we will see about categorical data points

.Boxplot
.Violen plot
.Count plot
.Bar plot
"""

import pandas as pd
import seaborn as sns
data = pd.read_csv("B:\\data science\\Python\\datasets\\bankloan.csv")
len(data)
data.columns

#------------bar plot
sns.barplot(x='marital',y='balance',data=data)
sns.barplot(x='loan',y='day',data=data)
sns.barplot(x='education',y='balance',data=data)
#------------ count plot
sns.countplot(x='loan',data=data)
sns.countplot(x='education',data=data)
sns.countplot(x='job',data=data)
sns.countplot(x='marital',data=data)
sns.countplot(x='housing',data=data)
sns.countplot(x='month',data=data)
#------------boxplot
sns.boxplot(x='housing',y='balance',data=data,hue='loan')
sns.boxplot(x='education',y='age',data=data,hue='loan')
sns.boxplot(x='job',y='age',data=data,hue='loan')
sns.boxplot(x='loan',y='day',data=data,hue='month')
