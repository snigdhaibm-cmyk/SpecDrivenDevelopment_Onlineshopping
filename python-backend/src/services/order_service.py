import uuid
from datetime import datetime
from typing import List, Optional
from models.order import Order, OrderItem
from repositories.order_repository import OrderRepository
from services.cart_service import CartService
from services.product_service import ProductService


class OrderService:
    def __init__(self, order_repository: OrderRepository = None, 
                 cart_service: CartService = None, 
                 product_service: ProductService = None):
        self.order_repository = order_repository or OrderRepository()
        self.cart_service = cart_service or CartService()
        self.product_service = product_service or ProductService()

    def checkout(self, user_id: str) -> Order:
        """Process checkout and create order"""
        cart = self.cart_service.get_cart(user_id)
        
        if not cart.items:
            raise ValueError("Cannot checkout with empty cart")
        
        # Validate inventory for all items
        for item in cart.items:
            if not self.product_service.check_inventory(item.product_id, item.quantity):
                product = self.product_service.get_product_by_id(item.product_id)
                raise ValueError(f"Insufficient inventory for product {product.name if product else item.product_id}")
        
        # Create order items with product snapshots
        order_items = []
        for item in cart.items:
            product = self.product_service.get_product_by_id(item.product_id)
            if not product:
                raise ValueError(f"Product {item.product_id} not found")
            
            order_items.append(OrderItem(
                product_id=item.product_id,
                product_name=product.name,
                quantity=item.quantity,
                price_at_purchase=item.price_at_add
            ))
        
        # Calculate total
        total = self.cart_service.calculate_total(cart)
        
        # Create order
        order = Order(
            id=f"order-{uuid.uuid4().hex[:8]}",
            user_id=user_id,
            items=order_items,
            total=total,
            created_at=datetime.utcnow().isoformat() + 'Z',
            status="completed"
        )
        
        # Reduce inventory
        for item in cart.items:
            self.product_service.reduce_inventory(item.product_id, item.quantity)
        
        # Save order
        self.order_repository.save(order)
        
        # Clear cart
        self.cart_service.clear_cart(user_id)
        
        return order

    def get_user_orders(self, user_id: str) -> List[Order]:
        """Retrieve all orders for a user"""
        return self.order_repository.find_by_user_id(user_id)

    def get_order_by_id(self, user_id: str, order_id: str) -> Optional[Order]:
        """Retrieve a specific order"""
        order = self.order_repository.find_by_id(order_id)
        if order and order.user_id == user_id:
            return order
        return None
