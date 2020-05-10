"""输出测试报告"""
import xlrd, os, time, datetime
from xlwt import *
from xlutils.copy import copy
# from openpyxl import Workbook
from src.utils import config
from src.utils import constants
from src.utils import constants


class Report:
    def __init__(self):
        conf = config.Config()
        constants._init()
        self.now_time = datetime.datetime.now()
        # 设置当此测试excel报告输出的文件
        excel_report_path = conf.get_config('system', 'excel_report_path')
        excel_report_folder = excel_report_path + self.now_time.strftime('%Y-%m-%d')
        excel_report_file = self.now_time.strftime('%H_%M_%S')
        constants.set_value('excel_report_folder', excel_report_folder)
        constants.set_value('excel_report_file',excel_report_file)

        # 创建到处excel报告的文件夹
        if not os.path.exists(excel_report_folder):
            os.makedirs(excel_report_folder)

        # 导出excel报告
        excel_file = Workbook(encoding='utf-8')
        excel_sheet = excel_file.add_sheet('测试报告')
        for i in range(0, 4):
            excel_sheet.col(i).width = 256 * 40

        excel_sheet.write(0, 0, label='测试业务')
        excel_sheet.write(0, 1, label='测试行为')
        excel_sheet.write(0, 2, label='描述')
        excel_sheet.write(0, 3, label='测试时间')
        excel_file.save(excel_report_folder + '/' + excel_report_file + '.xlsx')
        # 初始化报告保存的文件
        self.output_file = constants.get_value('excel_report_folder') \
                           + '/' + constants.get_value('excel_report_file') + '.xlsx'
        # self.output_file = constants.get_value('excel_report_folder')+'/'+constants.get_value('excel_report_file')+'.xls'


    def add_excel_report(self, story, action, des):
        # self.now_time = datetime.datetime.now()
        # 打开数据表，进行数据提取
        rexcel = xlrd.open_workbook(self.output_file, formatting_info=True)
        # 返回工作表内容，把内容存到row中
        row = rexcel.sheets()[0].nrows
        # 将xlrd.Book复制到xlwt.Workbook中
        addexcel = copy(rexcel)
        addsheet = addexcel.get_sheet(0)
        addsheet.write(row, 0, story)
        addsheet.write(row, 1, action)
        addsheet.write(row, 2, des)
        addsheet.write(row, 3, self.now_time.strftime('%Y-%m-%d %H:%M:%S'))
        addexcel.save(self.output_file)

if __name__ == '__main__':
    ww = Report()
    ww.add_excel_report('11', '22', '33')