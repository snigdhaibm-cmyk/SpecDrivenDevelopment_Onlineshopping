from flask import Blueprint, jsonify, request
from services.cart_service import CartService

cart_bp = Blueprint('carts', __name__)
cart_service = CartService()


@cart_bp.route('/carts/<user_id>', methods=['GET'])
def get_cart(user_id):
    """Get user's cart"""
    try:
        cart = cart_service.get_cart(user_id)
        total = cart_service.calculate_total(cart)
        return jsonify({
            "cart": cart.model_dump(),
            "total": total
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to retrieve cart"
            }
        }), 500


@cart_bp.route('/carts/<user_id>/items', methods=['POST'])
def add_item_to_cart(user_id):
    """Add item to cart"""
    try:
        data = request.get_json()
        
        if not data or 'productId' not in data or 'quantity' not in data:
            return jsonify({
                "error": {
                    "code": "BAD_REQUEST",
                    "message": "Missing required fields: productId, quantity"
                }
            }), 400
        
        product_id = data['productId']
        quantity = data['quantity']
        
        if quantity <= 0:
            return jsonify({
                "error": {
                    "code": "BAD_REQUEST",
                    "message": "Quantity must be positive"
                }
            }), 400
        
        cart = cart_service.add_item(user_id, product_id, quantity)
        total = cart_service.calculate_total(cart)
        
        return jsonify({
            "cart": cart.model_dump(),
            "total": total
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
                "message": "Failed to add item to cart"
            }
        }), 500


@cart_bp.route('/carts/<user_id>/items/<product_id>', methods=['PUT'])
def update_cart_item(user_id, product_id):
    """Update cart item quantity"""
    try:
        data = request.get_json()
        
        if not data or 'quantity' not in data:
            return jsonify({
                "error": {
                    "code": "BAD_REQUEST",
                    "message": "Missing required field: quantity"
                }
            }), 400
        
        quantity = data['quantity']
        
        cart = cart_service.update_item_quantity(user_id, product_id, quantity)
        total = cart_service.calculate_total(cart)
        
        return jsonify({
            "cart": cart.model_dump(),
            "total": total
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
                "message": "Failed to update cart item"
            }
        }), 500


@cart_bp.route('/carts/<user_id>/items/<product_id>', methods=['DELETE'])
def remove_cart_item(user_id, product_id):
    """Remove item from cart"""
    try:
        cart = cart_service.remove_item(user_id, product_id)
        total = cart_service.calculate_total(cart)
        
        return jsonify({
            "cart": cart.model_dump(),
            "total": total
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to remove cart item"
            }
        }), 500


@cart_bp.route('/carts/<user_id>', methods=['DELETE'])
def clear_cart(user_id):
    """Clear all items from cart"""
    try:
        cart_service.clear_cart(user_id)
        return jsonify({
            "message": "Cart cleared successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to clear cart"
            }
        }), 500
