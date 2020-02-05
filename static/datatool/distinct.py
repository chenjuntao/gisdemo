# coding:utf-8
import csv

dir = '/media/cjt/data/wuhan/tel131/'
# dir = 'E:/wuhan/tel131/'

print('正在读取hn1数据...')
f = csv.reader(open(dir+'yd173.csv','r'))

print('正在比较写入统计结果...')
f3 = open(dir+'yd173out.csv','w',newline='')
writer = csv.writer(f3)

tmp = 0
for i in f:
    if i[0] != tmp:
        writer.writerow(i)
        tmp = i[0]
        
f3.close()

print('比较完成！')