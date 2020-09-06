'''身份验证蓝本中的路由和视图函数'''
from flask import render_template, redirect, request, url_for, flash
from . import auth
from flasky.mvapp.models import User
import re

@auth.route('/register',methods=['POST','GET'])
def register():
    error=None
    if request.method == 'POST':
        if request.form['password1']!=request.form['password2']:
            error="两次输入的密码不一致"
        else:
            if re.match(r'^(\w*|\d*)@\w*.(com|cn)$',request.form['username']):
                if User.verify_username(request.form['username'], request.form['password1']):
                    flash('注册成功，请登录')
                    return redirect(url_for('auth.login'))
                else:
                    error = "用户名已存在"
            else:
                error = "用户名格式不正确"

    return render_template("auth/register.html",error=error)


@auth.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method == 'POST':
        if User.verify_password(request.form.get('username'),request.form.get('password')):
            return redirect(url_for('main.home'))
        else:
            error = "wrong"
    return render_template('auth/login.html',error=error)


# @auth.route('/logout',methods=['POST','GET'])
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('home'))

