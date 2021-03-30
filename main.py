import xlrd
from datetime import datetime
import sys


def count():
    workbook = xlrd.open_workbook("lanchou.xls")
    table = workbook.sheets()[0]
    row_num = table.nrows
    res = {}
    min_day = 5
    now = 5
    min_price = sys.maxsize
    for i in range(1, 6):
        res[i] = 0
    for i in range(1, row_num):
        date = table.cell(i, 2).value
        price = float(table.cell(i, 3).value)
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()+1
        if now == weekday:
            if min_price >= price:
                min_day = weekday
                min_price = price
        else:
            now = 5
            min_day = now
            min_price = sys.maxsize
            continue
        if now == 1:
            res[min_day] = res[min_day]+1
            min_price = sys.maxsize
            now = 5
        else:
            now = now-1
    with open("res/lanchou_min.txt", "w") as file:
        for i in range(1, 6):
            s = str(i)+"\t"+str(res[i])+"\n"
            file.write(s)
        file.close()


def profit():
    workbook = xlrd.open_workbook("lanchou.xls")
    table = workbook.sheets()[0]
    nrows = table.nrows
    nowday = 5
    last_price = float(table.cell(1, 3).value)
    res_profit = {}
    res_loss = {}
    for i in range(1, 6):
        res_profit[i] = 0
        res_loss[i] = 0
    for i in range(1, nrows):
        date = table.cell(i, 2).value
        price = float(table.cell(i, 3).value)
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()+1
        if nowday == weekday:
            if last_price > price:
                res_profit[weekday] = res_profit[weekday]+1
            elif last_price < price:
                res_loss[weekday] = res_loss[weekday]+1
            if nowday == 5:
                last_price = price
        else:
            last_price = price
            nowday = 5
            continue
        if nowday == 1:
            nowday = 5
        else:
            nowday = nowday-1
    with open("res/lanchou_profit.txt", "w") as file:
        for i in range(1, 6):
            s = str(i)+"\t"+str(res_profit[i])+"\t"+str(res_loss[i])+"\n"
            print(s)
            file.write(s)
        file.close()


def riseOrLost():
    workbook = xlrd.open_workbook("lanchou.xls")
    table = workbook.sheets()[0]
    nrows = table.nrows
    res_rise = {}
    res_loss = {}
    for i in range(1, 6):
        res_rise[i] = 0
        res_loss[i] = 0
    for i in range(1, nrows):
        date = table.cell(i, 2).value
        profit = table.cell(i, 4).value
        try:
            profit=float(profit)
        except:
            continue
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()+1
        if weekday > 5:
            continue
        if profit > 0:
            res_rise[weekday] = res_rise[weekday]+1
        elif profit < 0:
            res_loss[weekday] = res_loss[weekday]+1
    with open("res/lanchou_rise.txt", "w") as file:
        for i in range(1, 6):
            s = str(i)+"\t"+str(res_rise[i])+"\t"+str(res_loss[i])+"\n"
            file.write(s)
            print(s)
        file.close()


riseOrLost()
