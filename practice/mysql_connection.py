import MySQLdb


def connection():
    conn = MySQLdb.connect(host='localhost',
                           user = 'bisalgt',
                           password = 'password',
                           db = 'flask_db'
                        )
    c = conn.cursor()
    return c, conn
