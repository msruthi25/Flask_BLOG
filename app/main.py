# pyrefly: ignore [missing-import]
import os
import sys

# Enable absolute package imports when running this file directly as a script
if __name__ == "__main__" and not __package__:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from app.extensions import *

app=Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "BlogDB.db")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from app.routes import *

if __name__ == "__main__":
    app.run(debug=True,threaded=False)
