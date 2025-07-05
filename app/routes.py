from flask import request, jsonify
from . import db
from .models import User
from flask import current_app as app

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.json
        user = User(name=data['name'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created", "user": user.name}), 201

    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])
