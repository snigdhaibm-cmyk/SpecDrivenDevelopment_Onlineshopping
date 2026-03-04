# Quick Start Guide

## Running the Python Backend Locally

### Step 1: Navigate to the Python backend directory
```bash
cd shopping-cart-app/python-backend
```

### Step 2: Run the application

**On macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**On Windows:**
```bash
run.bat
```

**Or manually:**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

### Step 3: Test the API

The server will start on `http://localhost:5000`

**Option 1: Use the test script (in a new terminal):**
```bash
cd shopping-cart-app/python-backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python test_api.py
```

**Option 2: Use curl:**
```bash
# Get all products
curl http://localhost:5000/api/products

# Get specific product
curl http://localhost:5000/api/products/prod-001

# Add item to cart
curl -X POST http://localhost:5000/api/carts/user1/items \
  -H "Content-Type: application/json" \
  -d '{"productId": "prod-001", "quantity": 2}'

# Get cart
curl http://localhost:5000/api/carts/user1

# Checkout
curl -X POST http://localhost:5000/api/orders/user1/checkout

# Get orders
curl http://localhost:5000/api/orders/user1
```

**Option 3: Use your browser:**
- Products: http://localhost:5000/api/products
- Specific product: http://localhost:5000/api/products/prod-001
- User cart: http://localhost:5000/api/carts/user1

## API Endpoints

### Products
- `GET /api/products` - Get all products
- `GET /api/products/:id` - Get product by ID
- `GET /api/products/search?q=<query>&category=<category>` - Search products

### Cart
- `GET /api/carts/:userId` - Get user's cart
- `POST /api/carts/:userId/items` - Add item to cart
  ```json
  {"productId": "prod-001", "quantity": 2}
  ```
- `PUT /api/carts/:userId/items/:productId` - Update item quantity
  ```json
  {"quantity": 3}
  ```
- `DELETE /api/carts/:userId/items/:productId` - Remove item from cart
- `DELETE /api/carts/:userId` - Clear cart

### Orders
- `POST /api/orders/:userId/checkout` - Checkout cart
- `GET /api/orders/:userId` - Get user's orders
- `GET /api/orders/:userId/:orderId` - Get specific order

## Sample Users

- `user1` - Alice Johnson
- `user2` - Bob Smith
- `user3` - Carol Williams

## Sample Products

25 products across 5 categories:
- Electronics (5 products)
- Clothing (5 products)
- Books (5 products)
- Home & Garden (5 products)
- Sports (5 products)

Price range: $12.99 - $299.99

## Troubleshooting

**Port already in use:**
Edit `src/app.py` and change the port number:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

**Module not found errors:**
Make sure you activated the virtual environment:
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**Data not persisting:**
Check that the `data/` directory exists and has write permissions.
