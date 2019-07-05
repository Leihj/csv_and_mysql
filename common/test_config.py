# -*- coding: utf-8 -*-
# @File    : test_config.PY
# @Date    : 2019/7/4-16:18
# @Author  : leihuijuan
# @Emali   : huijuan_lei@163.com

from configparser import ConfigParser
from common import os_path

class Read_Config:
    def __init__(self):
        self.config=ConfigParser()
        self.config.read(os_path.global_path,encoding="utf-8")
        switch=self.config.getboolean("switch","on_off")
        if switch:
            self.config.read(os_path.on_line_path,encoding="utf-8")
        else:
            self.config.read(os_path.test_path,encoding="utf-8")


    def get_section(self):
       return self.config.sections()

    def get_option(self,section):
        return self.config.options(section)

    def get_str(self,section,option):
        return self.config.get(section,option)

    def get_int(self,section, option):
        return self.config.getint(section, option)

conf=Read_Config()

if __name__ == '__main__':
    res=conf.get_int("db","port")
    print(type(res))

