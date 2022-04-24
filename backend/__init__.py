#  Endpoints          Attributes          Method        Description
#
#     /                  -                  GET         Returns the version and a list of available endpoints
#
#     /studenti             -               GET         List all students
#     /studenti             -               POST        Add a new student
#     /studenti/:id         -               POST        Complete student registration
#     /docenti             -                GET         List all teachers
#     /docenti             -                POST        Add a new teacher
#     /docenti/:id         -                POST        Complete teacher registration
#     /amministratori/:id  -                POST        Add a new administrator
#     /login             -                  POST        login an existing user, returning a JWT
#
#
# ------------------------------------------------------------------------------------

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

load_dotenv()

# inizializzo SQLAlchemy
db = SQLAlchemy()
mail = Mail()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # TODO: set to true
    app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER')

    db.init_app(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'pigeonline.project@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Chatta_Con_Piccioni'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)

    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
