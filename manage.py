# flasky/
#   ├ migrations
#   ├ mvapp/
#   │    ├ auth/        # 身份验证蓝图目录
#   │    │   ├ __init__.py #
#   │    │   └ views.py    # 身份验证路由和视图函数
#   │    ├ main/        # 主蓝本目录
#   │    │   ├ __init__.py #
#   │    │   ├ errors.py   # 主蓝本中的错误处理程序
#   │    │   └ views.py    # 主蓝本中的路由和视图函数
#   │    ├ static/      # 静态文件目录
#   │    │   ├ css/        # css文件目录
#   │    │   ├ img/        # 图片文件目录
#   │    │   └ js/         # js文件目录
#   │    ├ templates/   # 模板文件目录
#   │    ├ __init__.py  #
#   │    ├ forms.py     # 存放所有表单
#   │    └ models.py    # 存放所有数据模型
#   ├ tests/           # 测试代码包
#   │   ├ __init__.py     #
#   │   └ test_*.py       # 测试用例
#   ├ venv/            # 虚拟环境目录
#   ├ config.py        # 环境配置
#   ├ manage.py        # 应用启动程序
#   ├ requirements.txt # 列出应用程序依赖的所有Python包

from flasky.mvapp import create_app

app = create_app('default')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)