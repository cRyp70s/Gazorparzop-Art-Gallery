from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
cors = CORS(app, origins="*")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# admin.add_view(ModelView(Post, db.session))
