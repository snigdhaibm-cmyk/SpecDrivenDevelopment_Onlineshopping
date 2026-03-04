from flask import Blueprint, jsonify, request
from services.product_service import ProductService

product_bp = Blueprint('products', __name__)
product_service = ProductService()


@product_bp.route('/products', methods=['GET'])
def get_all_products():
    """Get all products"""
    try:
        products = product_service.get_all_products()
        return jsonify({
            "products": [p.model_dump() for p in products]
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to retrieve products"
            }
        }), 500


@product_bp.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """Get product by ID"""
    try:
        product = product_service.get_product_by_id(product_id)
        if not product:
            return jsonify({
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Product {product_id} not found"
                }
            }), 404
        return jsonify({
            "product": product.model_dump()
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to retrieve product"
            }
        }), 500


@product_bp.route('/products/search', methods=['GET'])
def search_products():
    """Search products by name or category"""
    try:
        query = request.args.get('q', '')
        category = request.args.get('category', '')
        
        products = product_service.search_products(
            query=query if query else None,
            category=category if category else None
        )
        
        return jsonify({
            "products": [p.model_dump() for p in products]
        }), 200
    except Exception as e:
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Failed to search products"
            }
        }), 500
