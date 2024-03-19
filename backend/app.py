from flask import Flask, make_response, jsonify, request, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from flask_bcrypt import Bcrypt
from models import db,Match,Fighter,Event

import json

# config = dotenv_values(".env")

app = Flask(__name__)
app.debug = True
# app.secret_key = config['FLASK_SECRET_KEY']
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.get('/fighters')
def get_fighters():
    fighters=Fighter.query.all()
    return [f.to_dict() for f in fighters],200

@app.get('/matches')
def get_matches():
    matches = Match.query.all()
    return [m.to_dict() for m in matches]

@app.get('/events')
def get_events():
    events = Event.query.all()
    return [e.to_dict() for e in events]

if __name__ == "__main__":
    app.run(port=5555, debug=True)