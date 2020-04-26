"""日志输出配置文件"""
import logging, os
from src.utils.constants import get_value
from src.utils.config import Config
import datetime


class Log:

    def __init__(self):
        # 初始化日志写入的文件
        now_time = datetime.datetime.now()
        # 从配置文件中读取path目录
        # 这一步可有可无其实可以优化
        self.conf = Config()
        self.log_path = self.conf.get_config('system', 'log_path')
        # self.log_floder = now_time.strftime('%Y-%m-%d')
        # 日志文件夹名
        self.log_folder = self.log_path + now_time.strftime('%Y-%m-%d')
        self.log_file = now_time.strftime('%H-%M')
        # print(self.log_floder)
        # 判断当前是否有文件夹
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        # 配置日志输出参数
        logging.basicConfig(
            level=logging.INFO,
            # 时间，代码所在文件，代码行号，日志级别名字，日志信息
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            # 设置报错所显示的时间信息
            datefmt='%a, %d %b %Y %H:%M:%S',
            # 日志写入文件夹
            filename=self.log_folder + '/' + self.log_file + '.log',
            # 日志写入方式w覆盖写入，a追加，r只读，同时只能存在一种方式
            filemode='a'
        )

    # 写入日志
    def add_log(self, page, function, descrition):
        # 写入日志所需信息
        out_str = page + ':' + function + ":" + descrition
        logging.info(out_str)

# pp = Log()
# pp.add_log('aa', 'bb', 'cc')
