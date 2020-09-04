#!usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from calendar import isleap
import datetime
from sklearn.linear_model import LinearRegression, Ridge
from random import random, choice

data = 'data_insurance.xlsx'


def get_shape(source):
    d = pd.read_excel(source)
    count = d.shape[0]
    # jan2017 = d.Series_2017
    return print(count)


# get_shape(data)

# формирование списков сумм продаж и списки месяцев
def get_data_from_source(source):
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
    return date_prepend(wb, list(series17+series18+series19), list(dates17+dates18+dates19))


def date_prepend(source, series, dates):
    window = 12
    horizon = 2
    count = source.shape[0]
    count_tr = count-horizon
    mas_x = list()
    mas_y = list()
    for i in range(0, count_tr-window+1):
        mas_x.append(series[i:(i+window)])
        mas_y.append(series[i+window])
    x = np.array(mas_x)
    y = np.array(mas_y)
    # return ridge_object(x, y)
    # return ridge_alpha_value(arr_x=x, arr_y=y)
    return ridge_object(x, y)


def linear_regression_object(arr_x, arr_y):
    """Функция тестового создания и обучения объекта алгоритмом Линейной регрессии"""
    regression_obj = LinearRegression().fit(arr_x, arr_y)
    return print(regression_obj.score(arr_x, arr_y))


def ridge_alpha_value(arr_x, arr_y):
    """Функция для формирования тестового массива коэффициентов"""
    score_lst = list()
    alpha_lst = [random().__round__(2) for i in range(10)]
    for j in alpha_lst:
        reg = Ridge(normalize=True, alpha=j)
        reg.fit(arr_x, arr_y)
        score_lst.append(reg.score(arr_x, arr_y))
    return print(alpha_lst)


def ridge_object(arr_x, arr_y):
    alpha_lst = [random().__round__(2) for i in range(10)]
    obj = Ridge(normalize=True, alpha=choice(alpha_lst))
    obj.fit(arr_x, arr_y)
    return print(obj.score(arr_x, arr_y))


def predict_data_get(pre_fit_obj, horizon, window, count_tr, series):
    # j = 0
    rez_m = list()
    for j in range(horizon):
        s = np.copy(series[count_tr-window + j:count_tr])
        if len(rez_m) > 0:
            for i in range(j):
                s = np.append(s, rez_m[i])
        ss = list()
        ss.append(np.array(s))
        rez = pre_fit_obj.predict(ss)
        rez_m.append(rez[0])
    return print(rez_m)


def get_dates_list(series, year):
    dates = set()
    start = datetime.date(year, 12, 31)
    if isleap(year):
        period = 366
    else:
        period = 365
    for i in range(0, period):
        dates.add((start-datetime.timedelta(days=i)).__format__('%m.%Y'))
    return visualisation(series, sorted(dates), year)


def visualisation(series, dates, year):
    """Функция отрисовки графика"""
    plt.plot(dates, series, color='red', linestyle='solid', label=year)
    plt.legend(loc=9)
    return plt.show()


get_data_from_source(data)
