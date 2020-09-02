#!usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from calendar import isleap
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge

data = 'data_insurance.xlsx'


def get_shape(source):
    d = pd.read_excel(source)
    count = d.shape[0]
    # jan2017 = d.Series_2017
    return print(count)


# get_shape(data)

# формирование списков сумм продаж и списки месяцев
def get_data_from_source(source, year):
    dates17 = list()
    dates18 = list()
    dates19 = list()
    series17 = list()
    series18 = list()
    series19 = list()
    wb = pd.read_excel(source, 'Лист1')
    year17 = wb.Series_2017.to_list()
    year18 = wb.Series_2018.to_list()
    year19 = wb.Series_2019.to_list()
    for i in range(0, len(year17)):
        if i % 2 == 1:
            series17.append(year17[i])
        else:
            dates17.append(year17[i])
    for j in range(0, len(year18)):
        if j % 2 == 1:
            series18.append(year18[j])
        else:
            dates18.append(year18[j])
    for k in range(0, len(year19)):
        if k % 2 == 1:
            series19.append(year19[k])
        else:
            dates19.append(year19[k])
    # return visualisation(list(series17+series18+series19), list(dates17+dates18+dates19), year)
    return date_prepend(source, list(series17+series18+series19), list(dates17+dates18+dates19))


def date_prepend(source, series, dates):
    window = 365
    horizon = 365
    df = pd.read_excel(source)
    count = df.shape[0]
    count_tr = count-horizon
    mas_x = list()
    mas_y = list()
    for i in range(0, count_tr-window):
        mas_x.append(series[i:(i+window)])
        mas_y.append(series[i+window])
    x = np.array(mas_x)
    y = np.array(mas_y)
    return linear_regression_object(x, y)


def linear_regression_object(arr_x, arr_y):
    regression_obj = LinearRegression().fit(arr_x, arr_y)
    return ridge_object(regression_obj, arr_x, arr_y)


def ridge_object(obj, arr_x, arr_y):
    obj = Ridge(normalize=True, alpha=0.9)
    obj.fit(arr_x, arr_y)
    return obj

"""def get_dates_list(series, year):
    dates = set()
    start = datetime.date(year, 12, 31)
    if isleap(year):
        period = 366
    else:
        period = 365
    for i in range(0, period):
        dates.add((start-datetime.timedelta(days=i)).__format__('%m.%Y'))
    return visualisation(series, sorted(dates), year)
"""

# вывод графика
def visualisation(series, dates, year):
    plt.plot(dates, series, color='red', linestyle='solid', label=year)
    plt.legend(loc=9)
    return plt.show()


get_data_from_source(data, '2017-2019')
