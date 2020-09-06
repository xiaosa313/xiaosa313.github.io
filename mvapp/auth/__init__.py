'''创建身份验证蓝本'''
from flask import Blueprint

#身份验证蓝本通过实例化Blueprint类对象来创建
auth = Blueprint('auth',__name__)

#在实例化身份验证蓝本之后导入是为了避免循环导入
from . import views