from flask import current_app as app, request, jsonify, send_from_directory
import requests
from app.apod_parser import parse_apod_response

NASA_API_URL = "https://api.nasa.gov/planetary/apod"

@app.route('/<version>/apod', methods=['GET'])
def get_apod(version):
    params = {
        'api_key': request.args.get('api_key', 'DEMO_KEY'),
        'date': request.args.get('date'),
        'concept_tags': request.args.get('concept_tags', 'False'),
        'hd': request.args.get('hd', 'False'),
        'count': request.args.get('count'),
        'start_date': request.args.get('start_date'),
        'end_date': request.args.get('end_date'),
        'thumbs': request.args.get('thumbs', 'False')
    }

    response = requests.get(NASA_API_URL, params=params)
    data = response.json()

    return jsonify(parse_apod_response(data))

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')