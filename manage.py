# flask-demo/
#   ├ run.py           # 应用启动程序
#   ├ config.py        # 环境配置
#   ├ requirements.txt # 列出应用程序依赖的所有Python包
#   ├ tests/           # 测试代码包
#   │   ├ __init__.py
#   │   └ test_*.py    # 测试用例
#   └ myapp/
#       ├ admin/       # 蓝图目录
#       ├ static/
#       │   ├ css/     # css文件目录
#       │   ├ img/     # 图片文件目录
#       │   └ js/      # js文件目录
#       ├ templates/   # 模板文件目录
#       ├ __init__.py
#       ├ forms.py     # 存放所有表单，如果多，将其变为一个包
#       ├ models.py    # 存放所有数据模型，如果多，将其变为一个包
#       └ views.py     # 存放所有视图函数，如果多，将其变为一个包

from flask import Flask,url_for,request,render_template,redirect,session,make_response,flash
from flask_sqlalchemy import SQLAlchemy

import os
app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hisensewz313@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)
class Student(db.Model):
    __tablename__ = 'student'
    #__abstract__ = True

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    s_user = db.Column(db.String(64), unique=True)
    s_password = db.Column(db.String(15))

@app.before_first_request
def creat_db():
    db.drop_all()
    db.create_all()
    admin = Student(s_user='admin')
    db.session.add(admin)
    db.session.commit()

# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password')=='123456':
            session['username'] = request.form['username']#生成属于该用户的cookie
            #  flash('登录成功')
            return 'Admin login successfully!'
        else:
            return 'No such user!'

    response=make_response(render_template('index.html'),200)#构造响应头
    return response

@app.route('/logout')
def logout():
    session.pop('user', None)#将用户的cookie的清除
    return redirect(url_for('login'))#重定向到登录页面

# @app.route('/register')
# def register():
#     if request.method == 'POST':
#         user_temp=request.args.get('user')
#         '''数据库查重'''
#         if user_temp in database:
#             '''返回用户名已存在'''
#         else:
#             password1,password2=request.args.get('password1'),request.args.get('password2')
#             if password1 == password2:
#                 '''返回第二次输入的密码与第一次不一致'''
#             else:
#                '''存入数据库'''



if __name__ == "__main__":
    app.run(debug=True)
