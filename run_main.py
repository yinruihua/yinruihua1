import unittest
import time
import HTMLTestRunner
import os
#当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName ='case',rule = 'test*.py'):
    #第一步，加载所有的测试用例
    case_path = os.path.join(cur_path,caseName)
    #如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(cur_path):os.mkdir(case_path)
    #定义discover方法的参数
    print("test case path:%s"%case_path)
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)

    print(discover)
    return discover
