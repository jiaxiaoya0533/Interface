# -*- coding: utf-8 -*-
import  xlrd
import  encodings
import  xlwt
from  datetime import  date,datetime


class readcase():

        workbook = xlrd.open_workbook(r'D:\chonglianCase.xlsx')
        # 获取第一个sheet名字
        sheetnames = workbook.sheet_names()[0]
        # 根据sheet索引或者名称获取sheet内容
        sheet=workbook.sheet_by_index(0)
        # 获取sheet的列数
        nrows=sheet.nrows
        # 获取sheet的行数
        ncols=sheet.ncols
        # 获取第三行内容
        rows=sheet.row_values(3)
        # 获取第三列内容
        cols=sheet.col_values(3)
        #
        content=sheet.cell(3,6).value.encode('utf-8')


        print (content)











