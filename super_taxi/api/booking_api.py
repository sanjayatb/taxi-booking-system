from flask import Flask, jsonify, request, abort
from super_taxi.controllers.booking import book_controller
from super_taxi.model.generics import ResponseEncoder

app = Flask(__name__)
app.json_encoder = ResponseEncoder


@app.route('/api/book', methods=['POST'])
def book_task():
    data = request.json
    if not data or not 'source' in data or not 'destination' in data:
        abort(400)

    response = jsonify(book_controller.create_booking(data))
    print(response)
    return response, 200


@app.route('/api/tick', methods=['POST'])
def tick_task():
    book_controller.tick()
    return jsonify({}),200


@app.route('/api/reset', methods=['PUT'])
def reset_task():
    # book_controller.reset()
    return jsonify({}), 200
