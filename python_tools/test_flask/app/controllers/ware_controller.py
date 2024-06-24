from flask import Blueprint, request, jsonify
from app.services.ware_service import select_zero_inventory, shop_list_one_hundred

ware_bp = Blueprint('ware', __name__)

@ware_bp.route('/ware_zero_inventory', methods=['GET'])
def get_zero_inventory():
    name = request.args.get('name')
    print(name)
    if not name:
        return jsonify({'error': 'Missing name parameter'}), 400
    try:
        results = select_zero_inventory(name)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ware_bp.route('/ware_hundred_list', methods=['GET'])
def get_hundred_list():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    if not lat or not lng:
        return jsonify({'error': 'Missing lat,lng parameter'}), 400
    try:
        results = shop_list_one_hundred(lat, lng)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

