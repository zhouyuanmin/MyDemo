import pymysql
from pymysql import MySQLError
import json

# 配置 start_time
tables = ['VIEW_HOME_PAGE', 'CLICK_COURSE', 'REGISTER_NOW', 'CLICK_PAY', 'PAY_SUCCESS', 'SECOND_PAY']
start_time = '2020-01-01 11:26:53'

# sql语句
sql_0 = """SELECT
batch_code,
create_time,
body
FROM
pt_hadoop.buried 
WHERE
app_name = 'ddc-hadoop' 
AND `event` = '%s'
AND body IS NOT NULL
AND body != '{}'
AND create_time > '%s';"""

sql_1 = """INSERT INTO `pt_hadoop`.`study_dws_view_home_page` 
(`batch_code`, `nickname`, `avatar`, `userid`, `create_time`) 
VALUES ( '%s', '%s', '%s', %s, '%s' );"""

sql_2 = """INSERT INTO `pt_hadoop`.`study_dws_click_course` 
( `batch_code`, `nickname`, `avatar`, `user_id`, `goods_id`, `create_time` ) 
VALUES ( '%s', '%s', '%s', % s,% s, '%s' );"""

sql_3 = """INSERT INTO `pt_hadoop`.`study_dws_register_now` 
( `batch_code`, `nickname`, `avatar`, `user_id`, `goods_id`, `create_time` ) 
VALUES ( '%s', '%s', '%s', % s,% s, '%s' );"""

sql_4 = """INSERT INTO `pt_hadoop`.`study_dws_click_pay` 
( `batch_code`, `nickname`, `avatar`, `user_id`, `goods_id`, `create_time` ) 
VALUES ( '%s', '%s', '%s', % s,% s, '%s' );"""

sql_5 = """INSERT INTO `pt_hadoop`.`study_dws_pay_success` 
( `batch_code`, `nickname`, `avatar`, `user_id`, `goods_id`, `create_time`,`order_no` ) 
VALUES ( '%s', '%s', '%s', % s,% s, '%s', '%s');"""

sql_6 = """INSERT INTO `pt_hadoop`.`study_dws_second_pay` 
( `batch_code`, `nickname`, `avatar`, `user_id`, `goods_id`, `create_time`,`order_no` ) 
VALUES ( '%s', '%s', '%s', % s,% s, '%s', '%s');"""


class MysqlDemo(object):
    def __init__(self):
        self.db = pymysql.connect(
            host="cd-cdb-nz5meleu.sql.tencentcdb.com",
            user="root",
            passwd="******",
            database="pt_hadoop",
            port=62234
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()


mysql_db = MysqlDemo()

for i in tables:
    mysql_db.cursor.execute(sql_0 % (i, start_time))
    results = mysql_db.cursor.fetchall()
    for row in results:
        batch_code = row[0]
        create_time = row[1]
        body: dict = json.loads(row[2])  #
        nickname = body.get('nickname', '')
        avatar = body.get('avatar', '')
        user_id = body.get('userid', 'NULL')
        goods_id = body.get('goodsid', 'NULL')
        order_no = body.get('orderNo', '')
        if i == 'VIEW_HOME_PAGE':
            sql = sql_1 % (batch_code, nickname, avatar, user_id, create_time)
        elif i == 'CLICK_COURSE':
            sql = sql_2 % (batch_code, nickname, avatar, user_id, goods_id, create_time)
        elif i == 'REGISTER_NOW':
            sql = sql_3 % (batch_code, nickname, avatar, user_id, goods_id, create_time)
        elif i == 'CLICK_PAY':
            sql = sql_4 % (batch_code, nickname, avatar, user_id, goods_id, create_time)
        elif i == 'PAY_SUCCESS':
            sql = sql_5 % (batch_code, nickname, avatar, user_id, goods_id, create_time, order_no)
        elif i == 'SECOND_PAY':
            sql = sql_6 % (batch_code, nickname, avatar, user_id, goods_id, create_time, order_no)
        else:
            sql = ''

        # 执行sql
        if sql:
            # 记录执行的sql脚本，便于追踪异常
            with open('do_sql.sql', 'a+') as f:
                f.write(sql + '\n')
            try:
                mysql_db.cursor.execute(sql)
                mysql_db.db.commit()
            except MySQLError as e:
                print(e.args)
                with open('do_sql_error.log', 'a+') as f2:
                    f2.write(str(e.args) + '\n')
                    f2.write('error_sql:' + sql + '\n')
                mysql_db.db.rollback()
