#!usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import datetime
from calendar import isleap

data = 'data_insurance.xlsx'


def get_data_from_source(source):
    start_d = datetime.date(2017, 1, 1)
    series17 = list()
    series18 = list()
    series19 = list()
    workbook = pd.read_excel(source, 'Лист1')
    year17 = workbook['Январь 2017 года'].to_list()
    year18 = workbook['Январь 2018 года'].to_list()
    year19 = workbook['Январь 2019 года'].to_list()
    for i in range(0, len(year17), 2):
        series17.append(year17[i])
    for j in range(0, len(year18), 2):
        series18.append(year18[j])
    for k in range(0, len(year19), 2):
        series19.append(year19[k])
    return get_dates_list(series19, 2019)


def get_dates_list(series, year):
    dates = set()
    start = datetime.date(year, 12, 31)
    if isleap(year):
        period = 366
    else:
        period = 365
    for i in range(0, period):
        dates.add((start-datetime.timedelta(days=i)).__format__('%m.%Y'))
    return visualisation(series, sorted(dates))


def visualisation(series, dates):
    plt.plot(dates, series, color='red', linestyle='solid', label='2019')
    #plt.plot(dat18, ser18, color='green', linestyle='solid', label='2018')
    # plt.plot(dat19, ser19, color='yellow', linestyle='solid', label='2019')
    plt.legend(loc=9)
    return plt.show()


get_data_from_source(data)
