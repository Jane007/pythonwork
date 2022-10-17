# @Project : pythonwork
# @File    : mail.py
# @Author  : zhangjing
# @Time    : 2022/9/28 12:38
# @Software : Pycharm
# @Description :
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)


app.config['MAIL_SERVER']="smtp.163.com"
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="zhangjingvc@163.com"
app.config['MAIL_PASSWORD']="TFRHLDNGRFCOWNOF"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message("hello",sender="zhangjingvc@163.com",recipients=["1522673979@qq.com"])
    msg.body = "hello,this email from Flask-mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)