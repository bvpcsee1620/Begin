from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
    'user': 'aniket',
    'pw': 'aniket',
    'db': 'test',
    'host': 'localhost',
    'port': '5432',
}

socketio = SocketIO()
# initializing extenstion
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    socketio.init_app(app)
    CORS(app,resources={r"/*":{"origins":"*"}})
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(user=POSTGRES['user'],
                                                                                                 pw=POSTGRES['pw'],
                                                                                                 db=POSTGRES['db'],
                                                                                                 port=POSTGRES['port'],
                                                                                                 host=POSTGRES['host'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Flask-mail Configuration
    app.config['MAIL_SERVER'] = "smtp.gmail.com"
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = "bvcoe.erp@gmail.com"
    app.config['MAIL_PASSWORD'] = "bvp@1998"
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['SECRET_KEY'] = 'kufiasecrethahaha'
    app.config['MAIL_DEFAULT_SENDER'] = "bvcoe.erp@gmail.com"

    return app