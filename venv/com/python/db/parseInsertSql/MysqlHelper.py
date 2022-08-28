#!/usr/bin/python

import contextlib

import pymysql


class MysqlHelper:
    def __init__(self, host, port, user, passwd, db, charset='utf8mb4'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    # 定义上下文管理器，连接后自动关闭连接
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @contextlib.contextmanager
    # 定义上下文管理器，连接后自动关闭连接
    def getMySqlConnection(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield self.cursor
            self.conn.commit()
        finally:
            self.close()

    def close(self):
        print('关闭流...')
        self.cursor.close()
        self.conn.close()

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return res

    def insert(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def update(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def delete(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def queryAll(self, sql, param):
        with self.getMySqlConnection() as cur:
            cur.execute(sql, param)
            data = cur.fetchall()
            return data


if __name__ == '__main__':
    db = MysqlHelper('127.0.0.1', 5306, 'root', 'root', "promotion")
    data = db.get_all("select * from t_uptown_t")
    # print(data)
    print(db.queryAll("select * from t_uptown_t where id =%s", "1"))
