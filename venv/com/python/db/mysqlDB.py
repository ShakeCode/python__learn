import contextlib
import traceback
import pymysql as mysql

host = "127.0.0.1"
port = "3306"
userName = "root"
passward = "root"
dataBaseName = "student"

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def getMySqlConnection(host='127.0.0.1', port=3306, user='root', passwd='root', db='student', charset='utf8'):
    '''获取数据库连接'''
    conn = mysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=mysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def getConnection():
    '''获取msql连接'''
    try:
        con = mysql.connect(host=host, port=3306, user=userName, passwd=passward, db=dataBaseName, charset='utf8')
        # con = mysql.connect(host, userName, passward, dataBaseName)
    except Exception as e:
        traceback.print_exc()
        # raise RuntimeError("获取数据库连接失败")
    return con


def getTeacherList():
    '''获取歌手列表'''
    con = getConnection()
    # 获取游标
    cur = con.cursor()
    # cur.execute("select * from teacher")
    # 参数化构造sql
    cur.execute("select * from teacher where teacher_id=%s", ("1"))
    con.commit()
    # 获取所有数据
    data = cur.fetchall()
    '''
    data = cur.fetchone()
    print("获取一行数据:",data)
    '''
    for da in data:
        print(da)

    cur.close()
    con.close()


def getUserList():
    with getMySqlConnection() as cur:
        cur.execute("select * from user where id =%s", "1")
        data = cur.fetchall()
        print("获取用户列表:", data)


def insertUser(data):
    '''插入用户'''
    with getMySqlConnection() as cursor:
        cursor.execute("insert into user(id,name,sex) values(%s,%s,%s)", data)
        new_id = cursor.lastrowid
        print(new_id)


if __name__ == '__main__':
    print(getTeacherList.__doc__)
    # getTeacherList()
    # getUserList()
    insertUser(("4", "hello python", "1"))
