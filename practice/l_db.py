from flask import Flask

app = Flask(__name__)

from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bisalgt'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_db'

mysql = MySQL(app)


@app.route('/')
def index():
    name = 'bishal'
    age = 24
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO my_user (name, age) values(%s, %s)', (name, age))
    mysql.connection.commit()
    cur.close()
    return 'success'


@app.route('/users')
def list_user():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM my_user')
    users = cur.fetchall()
    return str(users)
