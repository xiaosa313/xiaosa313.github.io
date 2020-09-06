'''配置文件'''
import os
class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hisensewz313@127.0.0.1:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465  # qq邮箱用端口465
    MAIL_USE_SSL = True  # SSL加密设置为True
    MAIL_USERNAME = '1352711762@qq.com'
    MAIL_PASSWORD = 'rygnbqyvcugzifdb'
    MAIL_DEFAULT_SENDER = ('XiaoSa', '1352711762@qq.com')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}