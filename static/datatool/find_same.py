# coding:utf-8
import csv

print('正在读取今天数据...')
f = csv.reader(open('E:/wuhan/tel202/loudi.csv', 'r', encoding='UTF-8'))

print('正在读取历史数据...')
f2 = csv.reader(open('E:/wuhan/tel202/comp.csv', 'r', encoding='UTF-8'))
dat = []
for i in f2:
    dat.append(i[1])

print('正在比较写入统计结果...')
f3 = open('E:/wuhan/tel202/same.csv', 'w', newline='', encoding='UTF-8')
writer = csv.writer(f3)

for i in f:
    if i[0] in dat:
        writer.writerow(i)
        # print(i)
    else:
        # writer.writerow(i)
        print(i)

f3.close()

print('比较完成！')
