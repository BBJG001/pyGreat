import pymysql

class DBHandler():
    def __init__(self):
        self.database = pymysql.connect(host='127.0.0.1', user='root', password='asd12345', database='image_diff',
                                   charset='utf8')
        # database = pymysql.connect('服务器地址', '用户名', '密码', '数据库名', 字符集)

        # 初始化指针
        self.cursor = self.database.cursor()

    def crateTable(self):
        sql_create_table = 'create table if not exists tasks(test_name varchar(50),test_state varchar(20),ctime datetime, mtime datetime, etime datetime, primary key (test_name));'
        self.cursor.execute(sql_create_table)

    def insert(self):
        # 添加
        # sql = "INSERT INTO data (data, company, province, price, weight) VALUES ('2020-1-10', '河北粮食', '河北', '2200', '45.1'); "
        sql = "INSERT INTO tasks VALUES (0, 'test_name002', 'ready', NULL, NULL, NULL); "
        self.cursor.execute(sql)
        self.database.commit()   # 对数据进行修改后需要commit


    def search(self):
        # 查找
        # sql = "SELECT company, COUNT(company), SUM(weight*price), FROM data GROUP BY company"
        sql = "SELECT * FROM data"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()     # 获得结果
        for datacell in res:
            print(datacell)

        self.database.close()


def test():
    handler = DBHandler()
    # handler.crateTable()
    handler.insert()

if __name__ == '__main__':
    test()