# @Project : pythonwork
# @File    : stuvo.py
# @Author  : zhangjing
# @Time    : 2022/9/28 15:52
# @Software : Pycharm
# @Description :
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, url_for,flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = "adsfdsafewfsvdgvwefdsfsdfasfsda"


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


@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all())

@app.route('/delete/<int:no>')
def delete(no):
    ss = students.query.filter_by(id=no).all()[0]
    db.session.delete(ss)
    db.session.commit()
    return render_template('show_all.html', students = students.query.all())


@app.route("/new",methods=['POST','get'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city']:
            flash('Please enter all fields','error')
        else:
            student = students(request.form['name'],request.form['city'],request.form['addr'],request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)




