from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.auth import routes_auth


app = Flask(__name__)
app.register_blueprint(routes_auth, url_prefix="/api")
CORS(app)
app.config["DEBUG"] = True
passDb = "ADMINu5"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{passDb}@localhost/shopping"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
load_dotenv()
db = SQLAlchemy(app)

from app.routes import auth, routes