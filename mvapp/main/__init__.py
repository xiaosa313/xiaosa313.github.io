'''创建主蓝本'''
from flask import Blueprint

#主蓝本通过实例化一个Blueprint对象创建
main = Blueprint('main',__name__)

#在实例化主蓝本之后导入views和errors是为了避免循环导入
from . import views , errors

