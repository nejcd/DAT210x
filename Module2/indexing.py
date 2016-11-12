# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('D:/DAT210x/Module2/Datasets/direct_marketing.csv')
print df.columns
print df.loc[0:4,['recency','mens','womans']]