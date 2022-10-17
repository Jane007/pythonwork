# @Project : pythonwork
# @File    : studentBo.py
# @Author  : zhangjing
# @Time    : 2022/9/28 15:38
# @Software : Pycharm
# @Description :
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

db.create_all()
