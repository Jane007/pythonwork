# @Project : pythonwork
# @File    : dbtool.py
# @Author  : zhangjing
# @Time    : 2022/9/2 16:39
# @Software : Pycharm
# @Description :


import pymysql

class DbConnection:
    def __init__(self,ip="192.168.1.223",port=3306,user='zeno_element',password='123456',database='zeno_element'):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def getConn(self):
        conn = pymysql.connect(host=self.ip,port=self.port,user=self.user,password=self.password,database=self.database)
        return conn

    def insert(self,sql):
        try:
            conn = self.getConn()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit();
        except pymysql.Error as e:
            conn.rollback()
            print(f'mysql error:{e}')
        finally:
            conn.close()
            cursor.close()

    def update(self,sql):
        try:
            conn = self.getConn()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit();
        except pymysql.Error as e:
            conn.rollback()
            print(f'mysql error:{e}')
        finally:
            conn.close()
            cursor.close()

    def query(self,sql):
        try:
            conn = self.getConn()
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except pymysql.Error as e:
            print(f'mysql error:{e}')
        finally:
            conn.close()
            cursor.close()

    def delete(self,sql):
        try:
            conn = self.getConn()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit();
        except pymysql.Error as e:
            conn.rollback()
            print(f'mysql error:{e}')
        finally:
            conn.close()
            cursor.close()



import datetime
dbconn = DbConnection(ip='192.168.1.223',port=3306,user='zeno_element',password='123456',database='zeno_element')
# queryData = dbconn.query("select * from test ")
# print(queryData)#{datetime.datetime(2019, 3, 28, 17, 39, 9)}
formatted_date = datetime.datetime.now()
st = formatted_date.strftime("%Y-%m-%d %H:%M:%S")
sf = st.format("%Y-%m-%d %H:%M:%S")
sq = st.format("%H:%M:%S")
print(sq)
sql = f"insert into test values (26,19,'{sq}','{sf}','jane')"
#dbconn.insert(sql)
dbconn.delete("delete from test where id=23 ")