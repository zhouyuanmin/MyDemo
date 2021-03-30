import pymysql
from pymysql import MySQLError
import json

sql_1 = """SELECT
id
FROM
com_school 
WHERE
`name` LIKE '%小学%';"""
sql_2 = """INSERT INTO `pt_edu3`.`com_school_series` ( `school_id`, `series_id`, `desc`, `dead_line`, `student_nums`, `try_type`, `status`, `create_time`, `update_time` ) VALUES (%s, 32, NULL, NULL, 500, NULL, 1, NOW(), NOW() );"""


class MysqlDemo(object):
    def __init__(self):
        self.db = pymysql.connect(
            host="cd-cdb-nz5meleu.sql.tencentcdb.com",
            user="root",
            passwd="zsyl@2018db",
            database="pt_edu3",
            port=62234
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()


mysql_db = MysqlDemo()

mysql_db.cursor.execute(sql_1)
results = mysql_db.cursor.fetchall()
ids = [row[0] for row in results]
# print(ids)
ids = [129, 368, 501, 589, 632, 852, 1274, 1321, 1869, 2517]
for i in ids:
    print(sql_2 % i)
