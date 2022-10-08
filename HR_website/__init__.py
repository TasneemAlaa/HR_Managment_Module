from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlite3


db = SQLAlchemy()
DB_NAME = "empattenden.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Attendence
    with app.test_request_context():
        db.create_all()
        # db.drop_all()
    # user = User(email = 'admin@mail.com', first_name = 'admin', password = 'admin12', isAdmin = True) 
    # db.session.add(user)
    # db.session.commit()
    # create_database(app)

   
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app

# def create_database(app):
#     if not path.exists('HR_website/' + DB_NAME):
#         db.create_all()
#         # db.create_all(app=app)
#         print('Created Database!')
