# 🚀 Shopping Cart Application - Quick Start

## Start the Application

From the `python-backend` directory, run:

```bash
./run.sh
```

Or on Windows:
```bash
run.bat
```

Or manually:
```bash
python3 run_app.py
```

## Access the Application

Once the server starts, you'll see:

```
============================================================
Shopping Cart Application
============================================================
🌐 Web Interface: http://localhost:8000
📡 API Endpoint:  http://localhost:8000/api
...
============================================================

👉 Open your browser to: http://localhost:8000
```

## Open in Browser

**Copy and paste this URL into your browser:**
```
http://localhost:8000
```

Or click here if viewing in a terminal that supports links: http://localhost:8000

## Troubleshooting

### If you see "Resource not found" error:

1. Make sure the server is running (you should see the startup message above)
2. Check that you're accessing `http://localhost:8000` (not `http://localhost:8000/api`)
3. Try refreshing the page (Cmd+R on Mac, Ctrl+R on Windows)
4. Check the terminal for any error messages

### If the page doesn't load:

1. Verify the server is running on port 8000
2. Try accessing the API directly: http://localhost:8000/api/products
3. If that works, the backend is fine - try clearing your browser cache

### Port already in use:

Edit `run_app.py` and change:
```python
PORT = 8000  # Change to 8001 or another port
```

## Features

- Browse 25 products across 5 categories
- Add items to cart
- Update quantities
- Switch between 3 users
- Complete checkout
- Real-time inventory updates

Enjoy shopping! 🛒
