from flask import Flask, request, jsonify
from app import app
from app.models.base import db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.place_amenity import PlaceAmenities
from flask_json import FlaskJSON, as_json

app.config['JSON_ADD_STATUS'] = False

@app.route('/amenities', methods=['GET', 'POST'])
def get_amenties():
    amenities = []
    query = Amenity.select()
    for amenity in query:
            amenity.append(amenity.to_hash())
        return jsonify(amenities)

@app.route('/amenities', methods=['POST'])
@as_json
def create_amenity():
    data = request.values
    if 'name' in data:
        query = Amenity.select().where(Amenity.name == data['name'])
        if query.exists():
            out = {'code': 1003, 'msg': 'Name already exitst'}
            return out, 409
        new_amenity = Amenity.create(name = data['name'])
        if 'place_id' in data:
            query_place = Place.get(Place.id = int(data['place_id']))
            new_place = PlaceAmenities.create(place = query_place, amenity = new_amenity)
        return new_amenity.to_hash()
    else:
        return {'code': 404, 'msg': 'Not found'}, 404

@app.route('/amenities/<int:amenity_id>', methods=['DELETE'])
@as_json
def del_amenity(amenity_id):
    try:
        query = Amenity.select().where(Amenity.id == amenity_id).get()
    except:
        return {'code':404, 'msg':'Not found'}, 404
    out_json = query.to_hash()
    query.delete_instance()
    return out_json

@app.route('/amenities/<int:amenity_id>', methods=['GET'])
@as_json
def get_amenity_by_id(amenity_id):
    try:
        get_amenity = Amenity.get(Amenity.id == amenity_id)
        return get_amenity.to_hash()
    except:
        return {"code":404, "msg": "not found"}, 404
    
@app.route('/places/<int:place_id>/amenities', methods=['GET'])
def place_get_amenities(place_id):
    amenities = []
    query = PlaceAmenities.select().where(PlaceAmenities.place == place_id)
    for row in query:
        amenity = Amenity.get(Amenity.id == row.amenity)
        amenities.append(amenity.to_hash)
    return jsonify(amenities)
