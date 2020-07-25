from flask import Flask

from mysql_connection import connection

app = Flask(__name__)


@app.route('/')
def users():
    c, conn = connection()
    c.execute('SELECT * FROM my_user')
    counts = c.rowcount
    u1 = c.fetchone()
    u2 = c.fetchall()

    return f'{counts}----{u1}---{u2}'
