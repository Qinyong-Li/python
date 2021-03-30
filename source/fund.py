import sys
import os
import xlrd
import re
import json
import requests as req
import pygal
from datetime import datetime as dt


class Fund():

    def __init__(self, data=[]):
        self.data = data

    def computeMinVaule(self, output: str):
        min_value = {}
        for i in range(1, 6):
            min_value[i] = 0
        length = len(self.data)
        nowday = 5
        target = 5
        min_v = sys.maxsize
        for i in range(length):
            weekday = dt.strptime(self.data[i][0], "%Y-%m-%d").weekday()+1
            if weekday == nowday:
                if(min_v >= float(self.data[i][1])):
                    min_v = float(self.data[i][1])
                    target = weekday
            else:
                nowday = 5
                target = 5
                min_v = sys.maxsize
                continue
            if nowday == 1:
                min_value[target] = min_value[target]+1
                nowday = 5
                target = 5
                min_v = sys.maxsize
            else:
                nowday = nowday-1

        with open(output, "w") as file:
            for i in range(1, 6):
                file.write(str(min_value[i])+"\n")
        return min_value

def draw_hist(data=[],title=[],output="img/output.svg"):
    length=len(data)
    if length==0:
        return
    hist=pygal.Bar()
    if len(title)!=0:
        try:
            hist.title=title[0]
            hist.x_title=title[1]
            hist.y_title=title[2]
        except:
            pass
    labels=[i for i in range(1,6)]
    hist.x_labels=labels
    hist.add('min_value',data)
    hist.render_to_file(output)


def requestFuGuoFund(url: str):
    json_data = req.get(url).content.decode()
    data = json.loads(json_data)["dataList"]
    length = len(data)
    print(length)
    with open("res/fuguotianhui.txt", "w") as file:
        for i in range(length):
            s = data[i]["date"]+"\t"+data[i]["netvalue"] + \
                "\t"+"%.2f" % (float(data[i]["dayinc"])/100)+"\n"
            file.write(s)
        file.close()


def readDateFromTxt(filename: str):
    data = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            data_line = []
            data_line.append(words[0])
            data_line.append(float(words[1]))
            data_line.append(float(words[2]))
            data.append(data_line)
        file.close()
    return data


# url='http://www.fullgoal.com.cn/chart-web/chart/fundnettable!getFundNetTableJson?fundcode=161005&from=2010-03-30&to=2021-03-30&pages=1-2100&siteId=ea9e215cce3342d3b40721461cd1572d'
# requestFuGuoFund(url)
filename = "res/fuguotianhui.txt"
data_str = readDateFromTxt(filename)
fund = Fund(data=data_str)
min_value=fund.computeMinVaule("res/fullgoal_min_value.txt")
draw_hist(min_value,["MIN_VALUE","weekday","count"],"img/fullgoal.svg")
os.system("sh move.sh")

