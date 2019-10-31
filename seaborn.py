# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:12:56 2019

@author: sai teja
"""

"""
SEABORN
 in seaborn we have Continous plots &
Distribution plots..
   .distplot         f1}----Univarient analysis
   .joint plot    f1,f2}---Bivariant analysis
   .pairplot
"""

import seaborn as sns
df=sns.load_dataset("tips")
df.head()
df.dtypes
df.corr()
sns.heatmap(df.corr())

##jointplot
sns.jointplot(x="tip",y="total_bill",data=df,kind="hex")
sns.jointplot(x="tip",y="total_bill",data=df,kind="reg")

##pairplot
sns.pairplot(df)
sns.pairplot(df,hue="sex")
sns.pairplot(df,hue="smoker")

##distplot
sns.distplot(df["tip"])
sns.distplot(df["tip"],kde=False,bins=10)



