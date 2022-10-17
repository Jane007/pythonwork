# @Project : pythonwork
# @File    : Hello.py
# @Author  : zhangjing
# @Time    : 2022/9/27 12:24
# @Software : Pycharm
# @Description :
from flask import Flask, redirect, url_for, render_template, request,make_response




app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    if name == 'admin':
        return redirect(app.url_for('hello_admin'))
    else:
        return redirect(app.url_for('hello_guest',guest=name))
@app.route("/admin")
def hello_admin():
    return "hello admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"hello {guest} as Gustes"

@app.route("/test/<int:score>")
def test_num(score):
    return render_template("hello.html",score=score)

@app.route("/result",methods=['POST','GET'])
def test_result():
    if request.method == 'POST':
        dict = request.form
        return render_template("result.html",result=dict)

@app.route("/test/<float:revNo>")
def test_floatNo(revNo):
    return f"输入的float数字是：{revNo}"

@app.route("/tologin")
def test_tologin():
    return redirect(app.url_for('to_login'))

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/setcookie",methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template("readcookie.html"))
        print(user)
        resp.set_cookie("userId",user)
        return resp


@app.route("/getCookie")
def getcookie():
    name = request.cookies.get("userId")
    print(name)
    return f"<h1>{name}</h1>"



if __name__ == '__main__':
    app.run(debug=True)