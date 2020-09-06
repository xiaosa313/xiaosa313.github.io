from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask import session
from sqlalchemy import and_,or_
from . import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    #email = db.Column(db.String(64),unique=True, index=True)
    #password = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    # role=db.column(db.SmallInteger)#1为管理员，2为老师，3为u学生

    @classmethod
    def verify_username(self,username,password):
        user=User.query.filter_by(username=username).first()
        if user:
            return False
        else:
            #generate_password_hash函数根据传入的password生成加密后的password_hash
            new_user = User(username=username, password_hash=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return True


    @classmethod
    def verify_password(cls,username,password):
        user=User.query.filter_by(username=username).first()
        #check_password_hash函数用来判断加密前后的两个值是否相同，返回类型为bool
        if user and check_password_hash(user.password_hash,password):
            session['username'] = username
            return True
        else:
            return False


class Grade(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    create_time=db.Column(db.DateTime,default=datetime.now)
    #一对多关系
    students = db.relationship('Student',backref='grade')

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    sex = db.Column(db.Integer)
    chinese_grade=db.Column(db.Integer)
    #一对多关系，
    grade_id = db.Column(db.Integer,db.ForeignKey('grade.id'))