import pymysql

database = pymysql.connect('127.0.0.1', 'root', 'asd12345', 'reinforce_test', charset='utf8')
# database = pymysql.connect('服务器地址', '用户名', '密码', '数据库名', 字符集)

# 初始化指针
cursor = database.cursor()

# 添加
sql = "INSERT INTO data (data, company, province, price, weight) VALUES ('2020-1-10', '河北粮食', '河北', '2200', '45.1'); "
cursor.execute(sql)
database.commit()   # 对数据进行修改后需要commit

# 查找
# sql = "SELECT company, COUNT(company), SUM(weight*price), FROM data GROUP BY company"
sql = "SELECT * FROM data"
cursor.execute(sql)
res = cursor.fetchall()     # 获得结果
for datacell in res:
    print(datacell)

database.close()