from src.utils import config
import xml.dom.minidom


class Data:
    def __init__(self, path, file_name):
        # 初始化获取配置文件的方法
        conf = config.Config()
        # 从config.ini文件中获取data路径
        data_path = conf.get_config('system', 'data_path')
        # 拼出xml文件路径
        xml_file = xml.dom.minidom.parse(data_path + path + file_name)
        # 获取文本
        self.xml_doc = xml_file.documentElement

    # 读取数据
    # tag:标签
    def get_data_by_tag(self, tag):
        # 根据标签名获取值
        mtag = self.xml_doc.getElementsByTagName(tag)
        # 返回第一个子标签中的值
        return mtag[0].firstChild.data


qq = Data('/', 'demo.xml')
test = qq.get_data_by_tag('version')
print(test)
