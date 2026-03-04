from datetime import datetime
from typing import Optional
from models.cart import Cart, CartItem
from repositories.cart_repository import CartRepository
from services.product_service import ProductService


class CartService:
    def __init__(self, cart_repository: CartRepository = None, product_service: ProductService = None):
        self.cart_repository = cart_repository or CartRepository()
        self.product_service = product_service or ProductService()

    def get_cart(self, user_id: str) -> Cart:
        """Retrieve user's cart"""
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            # Create new empty cart
            now = datetime.utcnow().isoformat() + 'Z'
            cart = Cart(user_id=user_id, items=[], created_at=now, updated_at=now)
            self.cart_repository.save(cart)
        return cart

    def add_item(self, user_id: str, product_id: str, quantity: int) -> Cart:
        """Add item to cart or update quantity if exists"""
        # Validate product exists and has sufficient inventory
        product = self.product_service.get_product_by_id(product_id)
        if not product:
            raise ValueError(f"Product {product_id} not found")
        
        if not self.product_service.check_inventory(product_id, quantity):
            raise ValueError(f"Insufficient inventory for product {product_id}")
        
        cart = self.get_cart(user_id)
        
        # Check if item already exists in cart
        existing_item = None
        for item in cart.items:
            if item.product_id == product_id:
                existing_item = item
                break
        
        if existing_item:
            # Update quantity
            new_quantity = existing_item.quantity + quantity
            if not self.product_service.check_inventory(product_id, new_quantity):
                raise ValueError(f"Insufficient inventory for product {product_id}")
            existing_item.quantity = new_quantity
        else:
            # Add new item
            cart.items.append(CartItem(
                product_id=product_id,
                quantity=quantity,
                price_at_add=product.price
            ))
        
        cart.updated_at = datetime.utcnow().isoformat() + 'Z'
        self.cart_repository.save(cart)
        return cart

    def update_item_quantity(self, user_id: str, product_id: str, quantity: int) -> Cart:
        """Update quantity of cart item"""
        cart = self.get_cart(user_id)
        
        if quantity <= 0:
            # Remove item if quantity is zero or negative
            return self.remove_item(user_id, product_id)
        
        # Validate inventory
        if not self.product_service.check_inventory(product_id, quantity):
            raise ValueError(f"Insufficient inventory for product {product_id}")
        
        # Find and update item
        found = False
        for item in cart.items:
            if item.product_id == product_id:
                item.quantity = quantity
                found = True
                break
        
        if not found:
            raise ValueError(f"Product {product_id} not found in cart")
        
        cart.updated_at = datetime.utcnow().isoformat() + 'Z'
        self.cart_repository.save(cart)
        return cart

    def remove_item(self, user_id: str, product_id: str) -> Cart:
        """Remove item from cart"""
        cart = self.get_cart(user_id)
        cart.items = [item for item in cart.items if item.product_id != product_id]
        cart.updated_at = datetime.utcnow().isoformat() + 'Z'
        self.cart_repository.save(cart)
        return cart

    def clear_cart(self, user_id: str) -> None:
        """Remove all items from cart"""
        self.cart_repository.delete(user_id)

    def calculate_total(self, cart: Cart) -> float:
        """Calculate total price for all cart items"""
        total = sum(item.quantity * item.price_at_add for item in cart.items)
        return round(total, 2)
