from flask_script import Manager
from myapp import create_app

app = create_app()
# app = Flask(__name__)
manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()