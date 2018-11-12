# 导包
from flask import Flask, render_template
from flask_script import Manager

from myapp import create_app

app = create_app()
# 实例化Flask
# app = Flask(__name__)

manager = Manager(app=app)

# 注册路由
# @app.route('/')
# # 处理函数
# def hello_world():
#     # return 'Hello World!'
#     return '<h1>Hello World</h1>'
#
# @app.route('/index')
# def index():
#     return render_template('one.html', Title='sb', msg='甘霖娘', data='草泥马')
#

# 主函数
if __name__ == '__main__':
    # 启动Flask服务
    # app.run(
    #     host='0.0.0.0',
    #     port=8000,
    #     debug=True
    # )
    manager.run()
