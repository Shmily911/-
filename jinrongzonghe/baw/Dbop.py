from jinrongzonghe.caw.Mysql import Mysql


class  Dbop:
    def delete_user(self,db,mobilephone):
        conn = Mysql().connect(db)
        mysql = Mysql()
        print(conn)
        mysql.execute(conn, f"UPDATE `apple`.`loan` SET `Title` = 'cehdai' WHERE `Id` = '1'; ")
        mysql.disconnect(conn)