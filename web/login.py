# @Project : pythonwork
# @File    : login.py
# @Author  : zhangjing
# @Time    : 2022/9/27 14:09
# @Software : Pycharm
# @Description :
import os

from flask import Flask, redirect, render_template, request, url_for, session
from werkzeug.utils import secure_filename






app = Flask(__name__)
app.secret_key="sdfsafsdfdsfsdfsdfsf"
app.config['UPLOAD_PATH']='image/'

@app.route("/to_login")
def for_login():
    return render_template("login.html")

@app.route("/to_login/<name>")
def to_login(name):
    return render_template("login.html",name=name)

@app.route("/login",methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username']=request.form['name']
        return render_template("index.html")
    return redirect(url_for('to_login',name=request.form['name']))

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/loginout")
def loginout():

    session.pop("username")
    return '<h1>退出登录成功</h1>'

@app.route("/upload",methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        # 上传照片
        basepath = os.path.dirname(__file__)
        savepath = os.path.join(basepath,'static\images',secure_filename(f.filename))#注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(savepath)
        return 'file uploaded successfully'

    else:
        return render_template("upload.html")




if __name__ == '__main__':
    app.run(debug=True)