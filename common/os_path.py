# -*- coding: utf-8 -*-
# @File    : os_path.PY
# @Date    : 2019/7/2-10:28
# @Author  : leihuijuan
# @Emali   : huijuan_lei@163.com


import os

AP_dir=os.path.dirname(os.path.dirname(__file__))

#start_file_path文件夹的路径
start_dir=os.path.join(AP_dir,"start_file_path")

#end_file_path文件夹的路径
end_dir=os.path.join(AP_dir,"end_file_path")

#配置文件开关项的路径
global_path=os.path.join(AP_dir,"test_conf","global.config")
print(global_path)

#线上环境配置文件的路径
on_line_path=os.path.join(AP_dir,"test_conf","on_line.config")

#测试环境配置文件的路径
test_path=os.path.join(AP_dir,"test_conf","test.config")


