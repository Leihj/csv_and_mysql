# -*- coding: utf-8 -*-
# @File    : do_mysql.PY
# @Date    : 2019/7/3-15:30
# @Author  : leihuijuan
# @Emali   : huijuan_lei@163.com

import pymysql
import csv
from common.test_config import conf

class DO_MYSQL:
    def __init__(self):
    #连接数据库，把信息放到配置文件，方便修改和管理
        self.host=conf.get_str("db","host")
        self.user=conf.get_str("db","user")
        self.password =conf.get_str("db","password")
        self.db = conf.get_str("db","db")
        self.port=conf.get_int("db","port")
        self.charset=conf.get_str("db","charset")
        #创建连接
        self.conn=pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db,port=self.port,charset=self.charset)
        print("已经连接到数据库")
        self.cursor=self.conn.cursor()    #获取游标

     #新建表
    def create_table(self):
        self.cursor.execute("drop table if exists sale;")    #执行sql语句：如果表存在就删除
        sql="create table sale(date DATE,paycount DECIMAL(10,2),reg VARCHAR(6));"   #执行sql语句，创建表
        self.cursor.execute(sql)
        sql="ALTER TABLE sale ADD unique (date,reg) ;"  #用date和reg两个字段确定唯一键
        self.cursor.execute(sql)
        print("CREATE TABLE OK")

    #插入数据
    def insert_data(self,file):
        self.create_table() #调用创建表格的方法
        with open(file,"r",encoding="utf-8") as  read_file: #使用上下文管理器
            csv_count_file=csv.reader(read_file)    #读取read_file这个csv文件
            try:
                for i, rows in enumerate(csv_count_file):   #循环最终的csv文件，行和列
                    if i >0:    #读取第一行的数据
                        #mysql数据的replace方法：有一眼的数据就覆盖，没有就插入
                        sql="replace into sale ({0},{1},{2}) values('{3}','{4}','{5}');".format('date','paycount','reg',rows[0],rows[1],rows[2])
                        self.cursor.execute(sql)    #执行sql语句
                    self.conn.commit()  #提交数据
                    print("插入数据成功")
            except:
                self.conn.rollback()    #提交不成功，则回滚到上一次的数据
                print("插入数据失败")
        self.mysql_close()

    def mysql_close(self):
        try:
            if self.cursor: #如果游标存在，就关闭游标
                self.cursor.close()
            if self.conn:
                self.conn.close()   #如果数据库有连接，就关闭数据库
        except Exception as e:
            print("数据库关闭失败")
            raise e



if __name__ == '__main__':
    pass