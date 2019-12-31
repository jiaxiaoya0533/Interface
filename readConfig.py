import configparser
import codecs
import os

# 将路径和文件名分开
path = os.path.split(os.path.realpath(__file__))[0]
# 将路径和文件名拼接组成配置文件的绝对路径
configPath = os.path.join(path, "config.ini")


class ReadConfig():

    def __init__(self):
        # 实例化configparser对象
        self.cf = configparser.ConfigParser()
        # 通过配置文件的绝对路径读取里面的内容
        self.cf.read(configPath, encoding='utf-8')
        # 输出配置文件的节点，检验是否能正常读取到配置文件内容
        self.name = self.cf.sections()
        print(self.name)


    def get_db(self, name):
      value = self.cf.get("DATABASE", name)
      return value
    def get_http(self,name):
        value=self.cf.get("HTTP",name)
        return  value

if __name__ == '__main__':
       ReadConfig()
