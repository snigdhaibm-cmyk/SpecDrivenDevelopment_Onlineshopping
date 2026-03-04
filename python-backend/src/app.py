from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from api.product_routes import product_bp
from api.cart_routes import cart_bp
from api.order_routes import order_bp
import os


def create_app():
    # Get the absolute path to the static folder
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app = Flask(__name__, static_folder=static_folder, static_url_path='')
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(cart_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')
    
    # Serve frontend
    @app.route('/')
    def index():
        return send_from_directory(static_folder, 'index.html')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        # Check if this is an API request
        from flask import request
        if request.path.startswith('/api'):
            return jsonify({
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Resource not found"
                }
            }), 404
        # Otherwise serve the index page (for SPA routing)
        return send_from_directory(static_folder, 'index.html')
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": {
                "code": "BAD_REQUEST",
                "message": str(error)
            }
        }), 400
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "An internal error occurred"
            }
        }), 500
    
    return app


if __name__ == '__main__':
    app = create_app()
    print("Starting Shopping Cart API on http://localhost:5000")
    print("API Documentation:")
    print("  Products: GET /api/products")
    print("  Cart: GET /api/carts/<userId>")
    print("  Orders: POST /api/orders/<userId>/checkout")
    app.run(debug=True, host='0.0.0.0', port=5000)
