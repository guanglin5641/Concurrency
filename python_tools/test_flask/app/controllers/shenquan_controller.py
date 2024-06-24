from flask import Blueprint, request, jsonify
from app.services.shenqun_service import bwc_order

shenqun_bp = Blueprint('shenquan', __name__)


@shenqun_bp.route('/bwc_order_create' , methods=['GET'])
def bwc_order_create() :
    params = {
        'order_no' : request.args.get('order_no') ,
        'shop_name' : request.args.get('shop_name') ,
        'order_time' : request.args.get('order_time') ,
        'price' : request.args.get('price') ,
        'order_state' : request.args.get('order_state') ,
        'name' : request.args.get('name') ,
        'open_user_id' : request.args.get('open_user_id'),
        'order_type' : request.args.get('order_type'),
        'is_cycle' : request.args.get('is_cycle'),
        'cycle_num':request.args.get('cycle_num')
        }
    # 移除值为 None 或 空字符串的参数
    params = { k : v for k , v in params.items() if v }
    # 调用业务逻辑函数 bwc_order 并传递参数
    results = bwc_order(**params)
    return jsonify(results)