import pymysql
import xlwt


db = pymysql.connect(host='175.178.45.139',
                     user='root',
                     password='123456',
                     database='lxb',
                     charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT *  from sfz ")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("数据库连接成功！", data)
# 关闭数据库连接
db.close()
