# -*- coding:utf-8 -*-
# @Project: csv_file 
# File: 222
# Author: leihuijuan
# Date: 2019/7/1-21:46
# Email: huijuan_lei@163.com
import os
import csv
import time
from common import do_mysql
from common import os_path
class Read_CSV:
    def __init__(self,FilePath):
        self.FilePath=FilePath


    #写表头
    def writer_files(self,file):
        with open(file, 'a', newline="") as csvfile:    #用上下文管理器打开怎个文件，newline：去除空行
            fieldnames = [ "date", "paycount", "reg"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()    #写入这个文件的表头

    #循环读所有文件后写入
    def readAllFiles(self):
        mysql= do_mysql.DO_MYSQL()  #实例化DO_MYSQL()类
        #读出这个目录下的所有文件
        fileList = os.listdir(self.FilePath)
        self.count_file = os_path.end_dir+"/总销售表{}.csv".format(time.strftime('%H-%M-%S'))   #用路径拼接的方式定义最后要写入的文件
        self.writer_files(self.count_file)  #写入到最后的文件里面
        try:
            for file in fileList:   #循环目录下的所有文件
                path = os.path.join(self.FilePath, file)    #通过路径拼接，读取指定文件
                if os.path.isfile(path):    #如果这个路径下有这个文件，则打开这个文件
                    file = open(path, 'r', encoding='utf-8')
                    csv_file = csv.reader(file) #读取csv文件
                    reg ='未知'
                    for i,rows in enumerate(csv_file):  #每个表根据行和列来循环
                        if i == 1:  #当第二行存在reg_map里面
                            reg = self.reg_map(rows[1]) #就去reg_map的value值
                        if i > 5: #当i等于6行的时候
                            csv_list = [rows[0].replace('/', '-'), rows[1],reg] #将第一列的数据“/”符号替换成 “-”符号，第二轮，和第三列根据reg_map的vlaue值
                            with open(self.count_file, 'a+',newline='', encoding='utf-8') as writer_file:
                                csvwriter = csv.writer(writer_file) #写入这个csv文件
                                csvwriter.writerow(csv_list)    #将csv_list的数据一行一行的写入
        except:
            print("读取csv文件失败")
        mysql.insert_data(self.count_file)  #将最终csv文件数据插入数据库里面

    #添加国家
    def reg_map(self,reg):
        reg_dict={"澳大利亚":"AUS","日本":"JP","台湾":"TW","美国":"US","英国":"UK","中国大陆":"CN"}
        if reg in reg_dict.keys():
            print(reg_dict[reg])
            return reg_dict[reg]    #返回字典的value值





if __name__ == '__main__':
    pass
    # Read_CSV().readAllFiles()
