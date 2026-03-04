from typing import List, Optional
from models.product import Product
from repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository = None):
        self.repository = repository or ProductRepository()

    def get_all_products(self) -> List[Product]:
        """Retrieve all products from catalog"""
        return self.repository.find_all()

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Retrieve a single product by ID"""
        return self.repository.find_by_id(product_id)

    def search_products(self, query: str = None, category: str = None) -> List[Product]:
        """Search products by name or category"""
        products = self.repository.find_all()
        
        if query:
            query_lower = query.lower()
            products = [p for p in products if query_lower in p.name.lower()]
        
        if category:
            products = [p for p in products if p.category.lower() == category.lower()]
        
        return products

    def check_inventory(self, product_id: str, quantity: int) -> bool:
        """Verify if sufficient inventory exists"""
        product = self.repository.find_by_id(product_id)
        if not product:
            return False
        return product.inventory >= quantity

    def reduce_inventory(self, product_id: str, quantity: int) -> None:
        """Reduce inventory after order completion"""
        product = self.repository.find_by_id(product_id)
        if not product:
            raise ValueError(f"Product {product_id} not found")
        
        if product.inventory < quantity:
            raise ValueError(f"Insufficient inventory for product {product_id}")
        
        product.inventory -= quantity
        self.repository.update(product)
