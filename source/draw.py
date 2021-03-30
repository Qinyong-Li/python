import matplotlib.pyplot as plt
import os
import pygal


class Draw():
    # the length of data should be even
    def __init__(self, data={}, labels=[], title=[]):
        self.data = data
        self.len = len(data)
        self.labels = labels
        self.title = title

    def draw_hist(self, output="../img/out.svg"):
        hist = pygal.Bar()
        if len(self.labels) != 0:
            hist.x_labels = self.labels[0]
        if len(self.title) != 0:
            try:
                hist.title = self.title[0]
                hist.x_title = self.title[1]
                hist.y_title = self.title[2]
            except:
                a = 1
        keys = self.data.keys()
        for key in keys:
            hist.add(key, self.data[key])
        hist.render_to_file(output)


def readProfitFile():
    with open("res/lanchou_profit.txt") as file:
        lines = file.readlines()
        data = {}
        data['rise'] = []
        data['lose'] = []
        for line in lines:
            profit = line.split()
            data['rise'].append(int(profit[1]))
            data['lose'].append(int(profit[2]))
        d = Draw(data=data, title=['rise and loss --lanchou', 'weekday', 'num'], labels=[
                 [i for i in range(1, 6)]])
        d.draw_hist("img/riseAndLoss.svg")
        os.system('sh move.sh')
        file.close()

r
