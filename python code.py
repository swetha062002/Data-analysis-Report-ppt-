# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
MAGGI=pd.read_excel("C:/Users/happy/Downloads/MAGGI.xlsx")
MAGGI.head()


from scipy import stats
stats.shapiro(MAGGI.YEAR)
stats.shapiro(MAGGI.VEGATTA)
stats.shapiro(MAGGI.MAGGI)
stats.ttest_ind(MAGGI.VEGATTA,MAGGI.MAGGI)


