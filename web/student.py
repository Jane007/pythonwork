# @Project : pythonwork
# @File    : student.py
# @Author  : zhangjing
# @Time    : 2022/9/28 14:58
# @Software : Pycharm
# @Description :
from flask import Flask, redirect, render_template, request, url_for, session
import sqlite3
app = Flask(__name__)

@app.route('/enternew')
def new_student():
    return render_template('student.html')




@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
       try:
          nm = request.form['nm']
          addr = request.form['add']
          city = request.form['city']
          pin = request.form['pin']

          with sqlite3.connect("sqlite/database.db") as con:
             cur = con.cursor()
             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )

             con.commit()
             msg = "Record successfully added"
       except:
          con.rollback()
          msg = "error in insert operation"

       finally:
          return render_template("addStudent.html",msg = msg)
          con.close()



@app.route('/list')
def list():
    con = sqlite3.connect("sqlite/database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list_student.html",rows = rows)


@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
   app.run(debug=True)
