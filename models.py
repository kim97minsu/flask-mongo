from app import app, mongo 
from flask import jsonify
from werkzeug.security import generate_password_hash

class Users:
    def create(data):
        hashed_password = generate_password_hash(data['password'])
        mongo.db.user.insert_one({
            'name': data['name'],
            'email': data['email'],
            'password': hashed_password
        })
        resp = jsonify({ 'msg': 'User created successfully' })
        resp.status_code = 200
        return resp