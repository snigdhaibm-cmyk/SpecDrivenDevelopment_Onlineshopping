#!/usr/bin/env python3
"""
Quick API test script to verify the Shopping Cart API is working
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_api():
    print("Testing Shopping Cart API...\n")
    
    # Test 1: Get all products
    print("1. Getting all products...")
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()['products']
        print(f"   ✓ Found {len(products)} products")
        print(f"   Sample: {products[0]['name']}")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    # Test 2: Get specific product
    print("\n2. Getting product by ID...")
    product_id = products[0]['id']
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    if response.status_code == 200:
        product = response.json()['product']
        print(f"   ✓ Product: {product['name']} - ${product['price']}")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    # Test 3: Add item to cart
    print("\n3. Adding item to cart...")
    user_id = "user1"
    response = requests.post(
        f"{BASE_URL}/carts/{user_id}/items",
        json={"productId": product_id, "quantity": 2}
    )
    if response.status_code == 200:
        cart = response.json()
        print(f"   ✓ Cart total: ${cart['total']}")
        print(f"   Items in cart: {len(cart['cart']['items'])}")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    # Test 4: Get cart
    print("\n4. Getting cart...")
    response = requests.get(f"{BASE_URL}/carts/{user_id}")
    if response.status_code == 200:
        cart = response.json()
        print(f"   ✓ Cart has {len(cart['cart']['items'])} items")
        print(f"   Total: ${cart['total']}")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    # Test 5: Checkout
    print("\n5. Processing checkout...")
    response = requests.post(f"{BASE_URL}/orders/{user_id}/checkout")
    if response.status_code == 200:
        order = response.json()['order']
        print(f"   ✓ Order created: {order['id']}")
        print(f"   Order total: ${order['total']}")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    # Test 6: Get orders
    print("\n6. Getting order history...")
    response = requests.get(f"{BASE_URL}/orders/{user_id}")
    if response.status_code == 200:
        orders = response.json()['orders']
        print(f"   ✓ User has {len(orders)} orders")
    else:
        print(f"   ✗ Failed: {response.status_code}")
        return
    
    print("\n✓ All tests passed! API is working correctly.")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to API. Make sure the server is running on http://localhost:5000")
    except Exception as e:
        print(f"✗ Error: {e}")
