from flask import Flask, jsonify, request
from app import app
from app.models.user import User
from flask_json import as_json

app.config['JSON_ADD_STATUS'] = False

@app.route('/users', methods=['GET'])
def users():
    all_users = []
    query = User.select()
    for user in query:
        all_users.append(user.to_hash())
    return jsonify(all_users)

@app.route('/users', methods=['POST'])
@as_json
def create_new_user():
    data = request.values
    email_query = User.select().where(User.email == data['email'])
    if email_query.exists():
        out = {
            'code': 1000, 
            'msg': 'Email already exists'
        }
        return out, 409
    try:
        user_row = User.create(
            password = "default",
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
        )
        user_row.password = user_row.set_password(data['password'])
        if 'is_admin' in data:
            if data['is_admin'].lower() == "true":
                user_row.is_admin = True
            elif data['is_admin'].lower() == "false":
                user_row.is_admin = False
        user_row.save()
        return user_row.to_hash()
    except:
        return {"code":404, "msg":"incorrect parameters"}, 404

@app.route('/users/<int:number>', methods=['GET', 'PUT', 'DELETE'])
@as_json
def user(number):
    if request.method == 'GET':
        try:
            query = User.get(User.id == number)
            return query.to_hash()
        except:
            return {'error':'user does not exist'}
    elif request.method == 'PUT':
        data = request.values
        query = User.get(User.id == number)
        if 'first_name' in data:
            query.first_name = data['first_name']
        if 'last_name' in data:
            query.last_name = data['last_name']
        if 'is_admin' in data:
            if post_data['is_admin'].lower() == "true":
                query.is_admin = True
            elif post_data['is_admin'].lower() == "false":
                query.is_admin = False
        if 'password' in data:
            query.set_password(data['password'])
        query.save()
        return query.to_hash()
    else:
        query = User.select().where(User.id == number)
        if query.exists():
            query = query.get()
            out_json = query.to_hash()
            query.delete_instance()
            return out_json
        else:
            return {"code":404, "msg":"not found"}, 404
