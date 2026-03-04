# Shopping Cart Application

A REST API backend system providing e-commerce shopping cart functionality with dual implementations in Python and Node.js.

## Features

- Product catalog browsing and search
- Shopping cart management (add, update, remove items)
- Inventory validation
- Checkout processing
- Order history tracking
- Persistent data storage

## Project Structure

```
shopping-cart-app/
├── python-backend/          # Python implementation
│   ├── data/               # JSON data files
│   ├── src/                # Source code
│   │   ├── models/         # Data models
│   │   ├── repositories/   # Data access layer
│   │   ├── services/       # Business logic
│   │   └── api/            # REST API endpoints
│   ├── tests/              # Test suites
│   └── requirements.txt    # Python dependencies
│
├── nodejs-backend/         # Node.js implementation
│   ├── data/              # JSON data files
│   ├── src/               # Source code
│   │   ├── models/        # Data models
│   │   ├── repositories/  # Data access layer
│   │   ├── services/      # Business logic
│   │   └── api/           # REST API endpoints
│   ├── tests/             # Test suites
│   └── package.json       # Node.js dependencies
│
└── README.md              # This file
```

## Sample Data

Both backends include sample data:
- **25 products** across 5 categories (Electronics, Clothing, Books, Home & Garden, Sports)
- **3 sample users** for testing
- Price range: $12.99 - $299.99
- Varying inventory levels (including out-of-stock items)

## Getting Started

### Python Backend

**Quick Start (Recommended):**

On macOS/Linux:
```bash
cd python-backend
chmod +x run.sh
./run.sh
```

On Windows:
```bash
cd python-backend
run.bat
```

**Manual Setup:**
```bash
cd python-backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

The server will start on `http://localhost:5000`

### Node.js Backend

```bash
cd nodejs-backend
npm install
npm start
```

## API Endpoints

### Products
- `GET /api/products` - Get all products
- `GET /api/products/:id` - Get product by ID
- `GET /api/products/search?q=<query>&category=<category>` - Search products

### Cart
- `GET /api/carts/:userId` - Get user's cart
- `POST /api/carts/:userId/items` - Add item to cart
- `PUT /api/carts/:userId/items/:productId` - Update item quantity
- `DELETE /api/carts/:userId/items/:productId` - Remove item from cart
- `DELETE /api/carts/:userId` - Clear cart

### Orders
- `POST /api/orders/:userId/checkout` - Checkout cart
- `GET /api/orders/:userId` - Get user's orders
- `GET /api/orders/:userId/:orderId` - Get specific order

## Testing

### Python
```bash
cd python-backend
pytest
```

### Node.js
```bash
cd nodejs-backend
npm test
```

## Technology Stack

**Python Backend:**
- Flask (Web framework)
- Pydantic (Data validation)
- Hypothesis (Property-based testing)

**Node.js Backend:**
- Express (Web framework)
- Zod (Data validation)
- fast-check (Property-based testing)

## License

MIT
