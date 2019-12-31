import pymysql
from readConfig import ReadConfig
from common.log import MyLog as Mylog

class DB():
    def __init__(self):
        self.log = Mylog.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def _config_(self):
        self.host = ReadConfig.get_db("192.168.100.245")
        self.port = ReadConfig.get_db("3306")
        self.username = ReadConfig.get_db("xycdb")
        self.password = ReadConfig.get_db("xycdb123")
        self.database = ReadConfig.get_db("zkbc")
        self.charset = ReadConfig.get_db("utf8")
        self.config = {
            'host': str(self.host),
            'port': self.int(self.port),
            'user': self.username,
            'passwd': self.password,
            'db': self.database,
            'charset': self.charset
        }
    @staticmethod
    def connectDB(self):
        try:
            # 链接数据库
            self.db = pymysql.connect(**self.config)
            # 创建游标对象：用于执行查询，并获取结果
            self.cursor = self.db.cursor()

            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    #  执行sql
    @staticmethod
    def executeSql(self):
        self.connectDB()
        self.cursor.execute("SELECT * from  user_main ORDER BY userId desc  limit 100")

        self.db.commit()

        return self.cursor

    @staticmethod
    def get_all(self, cursor):
        """
      注：将返回所有sql结果
      关于fetchall()的使用:
      cursor.execute(select * from user)
      result=cursor.fetchall();
      此时select得到的可能是多行记录,那么我们通过fetchall得到的就是多行记录,是一个二维元组
     ((username1,password1,nickname1),(username2,password2,nickname2),(username3,password3,nickname))
        """
        value = cursor.fetchall()

        return value
    @staticmethod
    def get_one(self, cursor):
        """
        注：将只取最上面的第一条sql,如果没有结果,那就会返回nul
       关于fetchone()的使用:
       cursor.execute(select username,password,nickname from user where id='%s'  %(input)
       result=cursor.fetchone(); 
       通过result[0],result[1],result[2]可以得到username,password,nickname
        """
        value = cursor.fetchone()

        return value




    def closeDB(self):
        """
        关闭数据库

        """
        self.db.close()
        print("Database closed!")



