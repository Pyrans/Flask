from flask import Blueprint, url_for, redirect, render_template, request, make_response, abort, session

blue = Blueprint('hello', __name__)

@blue.route('/myblue')
def hello_blue_print():
    return '我是蓝图，规划URL'


@blue.route('/param/<int:id>')
def param(id):
    print(id)
    print(type(id))
    return str(id)


@blue.route('/param/<path:my_path>')
def param_path(my_path):
    print(my_path)
    print(type(my_path))
    import uuid
    uuid_val = uuid.uuid4()
    return str(uuid_val)

@blue.route('/params/<uuid:my_uuid>')
def param_uuid(my_uuid):
    print(my_uuid)
    print(type(my_uuid))
    return 'ok'


@blue.route('/my_any/<any(a,b,c,"20"):p>', methods=['GET', 'POST'])
def my_any(p):
    # print(p)
    # print(type(p))
    # url_for('蓝图名.函数名')
    # res = url_for('hello.hello_blue_print')
    res = url_for('hello.param', id=1, name='aha', age=20)
    return redirect(res)

@blue.route('/index')
def index():
    return render_template('one.html')

@blue.route('/req', methods=['GET', 'POST', 'PUT', 'DELETE'])
def look_req():
    req = request
    # print('method', req.method)
    # print('path', req.path)
    # print('url', req.url)
    # print('args', req.args)
    print('form', req.form)
    # print('base_url', req.base_url)
    # # print(dir(req))
    # print('name', req.args.get('name'))
    print('files', req.files)
    print('ip', req.remote_addr)
    return 'ok'

@blue.route('/response')
def my_response():
    # response = make_response('<h1>呵呵</h1>')
    # return response
    abort(403)   # 主动终止， 括号中为状态码
    return '呵呵', 500


@blue.errorhandler(403)
def handle_403(e):
    print(e)
    return '<h1><font color="skyblue" size="100px">没权限啊，辣鸡</font></h1>'


@blue.route('/home')
def home():
    # 通过cookie获取
    uname = request.cookies.get('name')
    # 在session中获取数据
    session_name = session.get('name')
    sname = session_name if session_name else '游客'
    print(sname)
    # 不确定是否能拿到
    uname = uname if uname else '游客'
    return render_template('home.html', uname=uname, sname=sname)


@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # pass
        # 解析post请求的参数
        name = request.form.get('name')

        # 设置session
        session['name'] = name

        # 设置cookie
        response = redirect(url_for('hello.home'))
        response.set_cookie('name', name, max_age=30)
        # 重定向到home
        return response
    else:
        abort(405)

@blue.route('/logout')
def logout():
    # 删除session
    session.pop('name')
    # 跳转到home
    response = redirect(url_for('hello.home'))
    # 删除cookie
    response.delete_cookie('name')
    return response

