# coding:utf-8
import csv
import os

dir = './csv/in'
page = 30000

print('打开要写入的文件...')
f = csv.reader(open('./csv/allin.csv', 'r', encoding='UTF-8'))

num = page
count = 0
f3 = None
writer = None
csvHeader = [] # 表头
for i in f:
    if len(csvHeader)==0:
        csvHeader = i
   
    if num < page:
        writer.writerow(i)
        num += 1
    else:
        if f3 is not None:
            writer.writerow(i)
            f3.close

        newFileName = dir+'/f'+str(count)+'.csv'
        print(newFileName)
        f3 = open(newFileName, 'w', newline='', encoding='UTF-8')
        writer = csv.writer(f3)
        writer.writerow(csvHeader)

        num = 0
        count += 1

print('拆分完成！')