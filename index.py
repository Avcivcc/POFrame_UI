"""入口函数"""
import datetime, os

from xlwt import Workbook
from src.utils import config
from src.utils import constants
from src.utils import driver
from src.utils import log
from src.utils import report
# from openpyxl import Workbook


# 入口函数定义要执行的store
class Index:

    def index(self):
        # 初始化模块
        conf = config.Config()
        constants._init()

        now_time = datetime.datetime.now()

        # 初始化驱动
        driver_class = driver.Driver()
        driver_Chrome = driver_class.get_chrome_driver()
        # 设置到全局变量中
        constants.set_value('driver_Chrome', driver_Chrome)

        # # 设置当此测试日志输出的文件夹于文件
        # log_path = conf.get_config('system', 'log_path')
        # log_folder = log_path + now_time.strftime('%Y-%m-%d')
        # log_file = now_time.strftime('%H_%M_%S')
        # # 把path添加到全局变量中
        # constants.set_value('log_folder', log_folder)
        # constants.set_value('log_file', log_file)

        # # 设置当此测试excel报告输出的文件
        # excel_report_path = conf.get_config('system', 'excel_report_path')
        # excel_report_folder = excel_report_path + now_time.strftime('%Y-%m-%d')
        # excel_report_file = now_time.strftime('%H_%M_%S')
        # constants.set_value('excel_report_folder',excel_report_folder)
        # constants.set_value('excel_report_file',excel_report_file)
        #
        # # 创建到处excel报告的文件夹
        # if not os.path.exists(excel_report_folder):
        #     os.makedirs(excel_report_folder)
        #
        # # 导出excel报告
        # excel_file = Workbook(encoding='utf-8')
        # excel_sheet = excel_file.add_sheet('测试报告')
        # for i in range(0, 4):
        #     excel_sheet.col(i).width = 256*40
        #
        # excel_sheet.write(0, 0, label='测试业务')
        # excel_sheet.write(0, 1, label='测试行为')
        # excel_sheet.write(0, 2, label='描述')
        # excel_sheet.write(0, 3, label='测试时间')
        # excel_file.save(excel_report_folder + '/' + excel_report_file + '.xlsx')


if __name__ == '__main__':
    ww = Index()
    ww.index()
    # print(constants.get_value('driver_Chrome'))
    # pp = log.Log()
    # pp.add_log('aa', 'bb', 'cc')
    ee = report.Report()
    ee.add_excel_report('11', '22', '33')
