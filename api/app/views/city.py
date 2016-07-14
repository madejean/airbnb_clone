from datetime import datetime
from flask import Flask, request, jsonify
from app import app
from app.models.base import db
from app.models.city import City
from app.models.state import State
from flask_json import FlaskJSON, as_json
from index import before_request, after_request
from playhouse.shortcuts import model_to_dict
import json

app.config['JSON_ADD_STATUS'] = False

@app.route('/states/<int:state_id>/cities', methods=['GET', 'POST'])
def cities(state_id):
    if request.method == 'GET':
        before_request()
        arr = []
        query = (City.select(State, City).join(State).where(State.id == state_id))
        for i in query:
            arr.append({"name":i.name, "created at":str(i.created_at), "id":str(i.id), "updated_at": str(i.updated_at), "state": i.state.name})
        after_request()
        return jsonify(arr)
    else:
        before_request()
        cityName = request.form.get('name', type=str)
        city_query = City.select().where(City.name == cityName)
        state_query = State.select().where(State.id == state_id).get()
        if city_query.exists():
            out = {'code': 1002, 'msg': 'City already exists'}
            after_request()
            return jsonify(out), 409
        user_row = City.create(state=state_query, name=cityName)
        out_json = user_row.to_hash()
        after_request()
        return jsonify(out_json)

@app.route('/states/<int:state_id>/cities/<int:city_id>', methods=['GET', 'DELETE'])
def city(state_id, city_id):
    if request.method == 'GET':
        before_request()
        i = City.get(City.id == city_id, City.state == state_id)
        #for i in query:
        arr = {"name":i.name, "created at":str(i.created_at), "id":str(i.id), "updated_at": str(i.updated_at), "state": i.state.name}
        after_request()
        return jsonify(arr)
    else:
        before_request()
        query = City.get(City.id == city_id, City.state == state_id)
        #query = City.select().where(City.id == number).get()
        out_json = query.to_hash()
        query.delete_instance()
        after_request()
        return jsonify(out_json)from app import app
from app.models.state import State
from app.models.city import City
from flask import jsonify, request

@app.route("/states/<state_id>/cities", methods=["GET"])
def cities(state_id):
    cities = []
    for city in City.select().where(City.state.id == state_id):
        cities.append(city.to_hash())
    return jsonify({"cities": cities})

@app.route("/states/<state_id>/cities", methods=["POST"])
def create_city():
    query = request.get_json()
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        city = City()
        city.name = content["name"]
        city.state = state_id
        city.save()
    except Exception as e:
        return "Failed"
    return "Success"

@app.route("/states/<state_id>/cities/<city_id>", methods=["GET"])
@app.route("/states/<state_id>/cities/<city_id>/", methods=["GET"])
def get_state_by_id(state_id, city_id):
    if not isinstance(int(city_id), int):
        return "Failed"
    cities = Cities.select().where(city.id == int(city_id))
    city = None
    for u in cities:
        city = u
    if city == None:
        return "Failed"
    return jsonify(city.to_hash())


@app.route("/states/<state_id>/cities/<city_id>", methods=["POST"])
@app.route("/states/<state_id>/cities/<city_id>/", methods=["POST"])
def delete_state_by_id(state_id, city_id):
    try:
        cities = Cities.select().where(city.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return "Failed"
        city.delete_instance()
    except:
        return "Failed"
    return "success"
