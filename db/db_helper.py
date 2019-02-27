from DBUtils.PooledDB import PooledDB
import pymysql


class DBConfig:
    # MYSQL_HOST = '123.207.152.86'
    MYSQL_HOST = '123.207.152.86'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = '123546'
    MYSQL_DB = 'gongfudou'


POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令
    ping=0,  # ping MySQL服务端,检查服务是否可用
    host=DBConfig.MYSQL_HOST,
    port=DBConfig.MYSQL_PORT,
    user=DBConfig.MYSQL_USER,
    password=DBConfig.MYSQL_PWD,
    database=DBConfig.MYSQL_DB,
    charset='utf8mb4'
)


class SQLHelper(object):

    @staticmethod
    def execute(sql, args=None, is_many=False):
        if args is None:
            args = []
        conn = POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        if is_many:
            status = cursor.executemany(sql, args)
        else:
            status = cursor.execute(sql, args)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return status, result

    @staticmethod
    def fetch_one(sql, args=None):
        if args is None:
            args = []
        conn = POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def fetch_all(sql, args=None):
        if args is None:
            args = []
        conn = POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, args)
        result = cursor.fetchall()
        conn.close()
        return result
