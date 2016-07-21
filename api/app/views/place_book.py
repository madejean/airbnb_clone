from app.models.place_book import PlaceBook
from app.models.place import Place
from app.models.user import User
from flask_json import as_json
from flask import request, jsonify
from app import app
from datetime import datetime

@app.route('/places/<int:place_id>/books', methods=['GET'])
def get_place_books(place_id):
    try:
        query = PlaceBook.select().where(PlaceBook.place == place_id)
    except:
        return {"code":404, "msg":"not found"}, 404
    place_books = []
    for place_book in query:
        place_books.append(place_book.to_hash())
    return jsonify(place_books)

@app.route('/places/<int:place_id>/books', methods=['POST'])
@as_json
def book_place(place_id):
    try:    
        data = request.values
        new = PlaceBook.create(
            place = place_id,
            user = data['user_id'],
            date_start = datetime.strptime(data['date_start'], "%Y/%m/%d %H:%M:%S")
        )
        if 'is_validated' in data:
            if data['is_validated'].lower() == 'true':
                new.is_validated = True
            elif data['is_validated'].lower() == 'false':
                new.is_validated = False
        if 'number_nights' in data:
            new.number_nights = int(data['number_nights'])
        new.save()
        return new.to_hash()
    except:
        return {"code":404, "msg":"not found"}, 404

@app.route('/places/<int:place_id>/books/<book_id>', methods=['GET'])
@as_json
def get_books(place_id, book_id):
    try:
        get_booking = PlaceBook.get(PlaceBook.id == book_id)
        return get_booking.to_hash()
    except:
        return {"code":404, "msg":"not found"}, 404

@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['DELETE'])
@as_json
def del_book(place_id, book_id):
    try:
        query = PlaceBook.get(PlaceBook.id == book_id)
    except:
        return {"code":404, "msg":"not found"}, 404
    out_json = query.to_hash()
    query.delete_instance()
    return out_json

@app.route('/places/<int:place_id>/books/<int:book_id>', methods=['PUT'])
@as_json
def change_book(place_id, book_id):
    try:
        query = PlaceBook.get(PlaceBook.id == book_id)
    except:
        return {"code":404, "msg":"not found"}, 404
    data = request.values
    for key in data:
        if key == 'is_validated':
            if data[key].lower() == 'true':
                query.is_validated = True
            elif data[key].lower() == 'false':
                query.is_validated = False
        if key == 'date_start':
            query.date_start = datetime.strptime(data[key], "%Y/%m/%d %H:%M:%S")
        if key == 'number_nights':
            query.number_nights = int(data[key])
    query.save()
    return query.to_hash()
