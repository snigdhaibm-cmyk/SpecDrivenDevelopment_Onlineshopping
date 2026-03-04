from flask import Blueprint, jsonify
from services.order_service import OrderService

order_bp = Blueprint('orders', __name__)
order_service = OrderService()


@order_bp.route('/orders/<user_id>/checkout', methods=['POST'])
def checkout(user_id):
    """Process checkout and create order"""
    try:
        order = order_service.checkout(user_id)
        return jsonify({
            "order": order.model_dump()
        }), 200
    except ValueError as e:
        return jsonify({
            "error": {
                "code": "BAD_REQUEST",
                "message": str(e)
            }
        }), 400
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to process checkout"
            }
        }), 500


@order_bp.route('/orders/<user_id>', methods=['GET'])
def get_user_orders(user_id):
    """Get all orders for a user"""
    try:
        orders = order_service.get_user_orders(user_id)
        return jsonify({
            "orders": [o.model_dump() for o in orders]
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to retrieve orders"
            }
        }), 500


@order_bp.route('/orders/<user_id>/<order_id>', methods=['GET'])
def get_order_by_id(user_id, order_id):
    """Get specific order by ID"""
    try:
        order = order_service.get_order_by_id(user_id, order_id)
        if not order:
            return jsonify({
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Order {order_id} not found"
                }
            }), 404
        return jsonify({
            "order": order.model_dump()
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to retrieve order"
            }
        }), 500
