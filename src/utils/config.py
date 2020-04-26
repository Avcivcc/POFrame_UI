"""
读取配置文件
"""
import configparser


class Config:

    def __init__(self):
        # 配置文件路径
        # self.file = './config/config.ini'
        self.file = 'D:/PycharmProjects/project_objcet_end/config/config.ini'
        print(self.file)


    # 获取配置
    def get_config(self, scetion, name):
        # configparser中的一个方法，实例化一个对象
        config = configparser.ConfigParser()
        # 读文件
        config.read(self.file)
        # config.read(self.path)
        # get方法,Section下的key对应的value
        value = config.get(scetion, name)
        # 返回value
        return value


# 测试
# ww = Config()
# rr = ww.get_config('system', 'log_path')
# print(rr)

