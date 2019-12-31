import logging
import os
import threading
import readConfig  as readConfig
from datetime import datetime


class Log:
    def __init__(self):
        # 声明变量是全局变量
        global logPath, resultPath, path
        path = readConfig.path
        resultPath = os.path.join(path, "result")
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # * 在用join路径拼接函数时，其连接的各级目录必须首先存在
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        if not os.path.exists(logPath):
            os.mkdir(logPath)
            """
            关于loggers：
            是程序可以直接调用的一个日志接口，
            可以直接向logger写入日志信息,
            logger并不是直接实例化使用的，
            而是通过logging.getLogger(name)来获取对象.
            """
            self.logger = logging.getLogger()
            # defined log level
            self.logger.setLevel(logging.INFO)

            # defined handler
            handler = logging.FileHandler(os.path.join(logPath, "output.log"))
            # defined formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, case_no):
        """
        write start line
        :return:
        """
        self.logger.info("--------" + case_no + " START--------")

    def build_end_line(self, case_no):
        """
        write end line
        :return:
        """
        self.logger.info("--------" + case_no + " END--------")

    def build_case_line(self, case_name, code, msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """
        self.logger.info("%s - Code:%s - msg:%s" % (case_name, code, msg))
        #         self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    # 创建锁
    mutex = threading.Lock()

    def __init__(self):
        pass

    '''
   关于@staticmethod：
   要使用某个类的方法，需要先实例化一个对象再调用方法
   而使用@ staticmethod或 @ classmethod不需要实例化，直接类名.方法名()来调用。
   '''

    @staticmethod
    def get_log():
        if MyLog.log is None:
            # 锁定 mutex.acquire(blocking)里面可以加blocking(等待的时间)或者不加，不加就会一直等待（堵塞）
            MyLog.mutex.acquire()
            MyLog.log = Log()
            # 释放锁
            MyLog.mutex.release()
        return MyLog.log


if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
