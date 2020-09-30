import pymysql


class Mysql:
    def connect(self,db):


        ip=db['ip']
        port=int(db['port'])
        name=db['name']
        user=db['user']
        pwd=db['pwd']
        try:
            conn=pymysql.connect(host=ip,port=port,user=user,password=pwd,charset='utf8',database=name)
            print(f"连接数据库{ip}，{port}成功")
            return conn
        except Exception as e:
            print(f"连接数据库异常，异常信息为{e}")
    def execute(self,conn,sql):
        try:
            cursor=conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            print(f"执行sql语句{sql}")
        except Exception as e:
            print(f"执行sql语句异常。异常信息为{e}")

    def disconnect(self,conn):
        try:
            conn.close()
        except Exception as e:
            print(f"断开数据库异常。异常信息为{e}")



if __name__ == '__main__':
    db={"ip":"jy001","port":"4406","name":"future","user":"root","pwd":"123456"}
    conn = Mysql().connect(db)
    mysql=Mysql()
    print(conn)
    mysql.execute(conn,"UPDATE `future`.`loan` SET `Title` = 'cehdai' WHERE `Id` = '1'; ")
    mysql.disconnect(conn)
