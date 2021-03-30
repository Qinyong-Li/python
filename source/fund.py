import sys
import os
import xlrd

class Fund():

    def __init__(self,filename:str,index:int):
        self.filename=filename
        self.workbook=xlrd.open_workbook(filename)
        self.table=slef.workbook.sheets()[index]

    def 