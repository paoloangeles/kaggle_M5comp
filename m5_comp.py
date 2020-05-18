#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:51:01 2020

@author: paoloangeles
"""

# Import modules

import pandas as pd
import matplotlib.pyplot as plt


# Get data from csvs
calendar = pd.read_csv("calendar.csv")
sell_prices = pd.read_csv("sell_prices.csv")
sales_train = pd.read_csv("sales_train_validation.csv")

number_of_days = 1913
a = []

for product in range(len(sales_train)):
    for day in range(number_of_days):
        a.append(sales_train.at[product, 'd_'+str(day+1)])