# coding:utf-8
import csv
import os

dir = './csv/out'


print('打开要写入的文件...')
f3 = open('./csv/allout.csv', 'w', newline='', encoding='UTF-8')
writer = csv.writer(f3)

for root, dirs, files in os.walk(dir):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    files.sort()
    fileCount = 1
    for fil in files:
        fi = os.path.join(root, fil)
        print(fi)
        f = csv.reader(open(fi, 'r', encoding='UTF-8'))
        rowCount = 1
        for i in f:
            # if (fileCount > 1 and rowCount == 1) :
            #     print(i)
            # else:
            writer.writerow(i)
            rowCount += 1
        fileCount += 1

f3.close()


print('合并完成！')
