#!/usr/bin/env python3
"""
Verify the shopping cart application setup
"""
import os
import sys

def verify_setup():
    print("Verifying Shopping Cart Application Setup...")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # Check if we're in the right directory
    if not os.path.exists('src'):
        errors.append("❌ 'src' directory not found. Run this from python-backend/")
    else:
        print("✓ Found src directory")
    
    # Check for static folder
    if not os.path.exists('src/static'):
        errors.append("❌ 'src/static' directory not found")
    else:
        print("✓ Found src/static directory")
    
    # Check for index.html
    if not os.path.exists('src/static/index.html'):
        errors.append("❌ 'src/static/index.html' not found")
    else:
        print("✓ Found src/static/index.html")
    
    # Check for data files
    data_files = ['data/products.json', 'data/users.json', 'data/carts.json', 'data/orders.json']
    for file in data_files:
        if not os.path.exists(file):
            errors.append(f"❌ '{file}' not found")
        else:
            print(f"✓ Found {file}")
    
    # Check for Python modules
    modules = ['src/app.py', 'src/models', 'src/services', 'src/repositories', 'src/api']
    for module in modules:
        if not os.path.exists(module):
            errors.append(f"❌ '{module}' not found")
        else:
            print(f"✓ Found {module}")
    
    # Check for virtual environment
    if not os.path.exists('venv'):
        warnings.append("⚠️  Virtual environment not found. Run './run.sh' to create it")
    else:
        print("✓ Found virtual environment")
    
    print("=" * 60)
    
    if errors:
        print("\n❌ ERRORS FOUND:")
        for error in errors:
            print(f"  {error}")
        print("\nPlease fix these errors before running the application.")
        return False
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
    
    print("\n✅ Setup verification complete!")
    print("\nTo start the application, run:")
    print("  ./run.sh")
    print("\nThen open your browser to:")
    print("  http://localhost:8000")
    
    return True

if __name__ == '__main__':
    success = verify_setup()
    sys.exit(0 if success else 1)
