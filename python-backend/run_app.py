#!/usr/bin/env python3
"""
Entry point for the Shopping Cart Application
Run this file from the python-backend directory
"""
import sys
import os

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

# Change working directory to src so Flask can find static folder
os.chdir(src_path)

from app import create_app

if __name__ == '__main__':
    app = create_app()
    PORT = 8000
    print("=" * 60)
    print("Shopping Cart Application")
    print("=" * 60)
    print(f"🌐 Web Interface: http://localhost:{PORT}")
    print(f"📡 API Endpoint:  http://localhost:{PORT}/api")
    print("\nAvailable API endpoints:")
    print("  GET  /api/products              - Get all products")
    print("  GET  /api/products/<id>         - Get product by ID")
    print("  GET  /api/products/search       - Search products")
    print("  GET  /api/carts/<userId>        - Get user's cart")
    print("  POST /api/carts/<userId>/items  - Add item to cart")
    print("  POST /api/orders/<userId>/checkout - Checkout")
    print("\nSample users: user1, user2, user3")
    print("=" * 60)
    print(f"\n👉 Open your browser to: http://localhost:{PORT}\n")
    app.run(debug=True, host='0.0.0.0', port=PORT)
