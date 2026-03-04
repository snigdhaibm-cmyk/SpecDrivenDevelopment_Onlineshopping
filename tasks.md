# Implementation Plan: Shopping Cart Application

## Overview

This plan implements a Shopping Cart Application with dual backend implementations in Python and Node.js. Both backends provide identical REST API functionality for product catalog management, shopping cart operations, checkout processing, and order history. The implementation follows a layered architecture with clear separation between API, business logic, and data layers.

## Tasks

- [x] 1. Set up project structure and sample data
  - Create directory structure for both Python and Node.js backends
  - Create sample data files (products.json, users.json)
  - Initialize empty data files (carts.json, orders.json)
  - _Requirements: 8.2, 8.3, 8.4_

- [x] 2. Implement Python data models and repositories
  - [x] 2.1 Create Python data models (Product, Cart, CartItem, Order, OrderItem, User)
    - Define Pydantic models with validation
    - Include field constraints (positive prices, non-negative inventory)
    - _Requirements: 1.3, 2.4, 5.6, 7.2_
  
  - [x] 2.2 Implement Python repository classes
    - Create ProductRepository with JSON file operations
    - Create CartRepository with JSON file operations
    - Create OrderRepository with JSON file operations
    - Implement file locking for concurrent access
    - _Requirements: 11.1, 11.2, 11.3, 11.4_
  
  - [ ]* 2.3 Write property test for data persistence
    - **Property 32: Data Persistence Across Restarts**
    - **Validates: Requirements 11.1, 11.2, 11.3, 11.4, 11.5**

- [ ] 3. Implement Node.js data models and repositories
  - [ ] 3.1 Create Node.js data models with TypeScript interfaces
    - Define TypeScript interfaces for all models
    - Add Zod schemas for validation
    - _Requirements: 1.3, 2.4, 5.6, 7.2_
  
  - [ ] 3.2 Implement Node.js repository classes
    - Create ProductRepository with async file operations
    - Create CartRepository with async file operations
    - Create OrderRepository with async file operations
    - _Requirements: 11.1, 11.2, 11.3, 11.4_
  
  - [ ]* 3.3 Write property test for data persistence
    - **Property 32: Data Persistence Across Restarts**
    - **Validates: Requirements 11.1, 11.2, 11.3, 11.4, 11.5**

- [x] 4. Implement Python business logic services
  - [x] 4.1 Implement ProductService
    - Create methods for get_all, get_by_id, search, check_inventory, reduce_inventory
    - _Requirements: 1.2, 1.4, 4.1, 4.5_
  
  - [ ]* 4.2 Write property tests for ProductService
    - **Property 1: Product Retrieval by ID**
    - **Property 2: Product Response Completeness**
    - **Property 3: Product Search Accuracy**
    - **Validates: Requirements 1.2, 1.3, 1.4**
  
  - [x] 4.3 Implement CartService
    - Create methods for get_cart, add_item, update_item_quantity, remove_item, clear_cart, calculate_total
    - Implement inventory validation logic
    - _Requirements: 2.1, 2.2, 2.5, 3.1, 3.3, 3.5, 4.1, 4.3_
  
  - [ ]* 4.4 Write property tests for CartService
    - **Property 4: Adding Item to Cart**
    - **Property 5: Adding Existing Item Updates Quantity**
    - **Property 7: Cart Total Calculation**
    - **Property 8: Update Cart Item Quantity**
    - **Property 9: Remove Item from Cart**
    - **Property 10: Clear Cart**
    - **Property 11: Inventory Validation on Add**
    - **Property 12: Inventory Validation on Update**
    - **Property 19: Cart Isolation Between Users**
    - **Validates: Requirements 2.1, 2.2, 2.5, 3.1, 3.3, 3.5, 4.1, 4.3, 6.5**
  
  - [x] 4.5 Implement OrderService
    - Create methods for checkout, get_user_orders, get_order_by_id
    - Implement checkout validation and order creation logic
    - _Requirements: 5.2, 5.4, 5.5, 7.3, 7.4_
  
  - [ ]* 4.6 Write property tests for OrderService
    - **Property 13: Inventory Deduction After Checkout**
    - **Property 14: Checkout Inventory Validation**
    - **Property 15: Order Creation from Cart**
    - **Property 16: Cart Cleared After Checkout**
    - **Property 21: Order Retrieval by ID**
    - **Property 22: Order Persistence**
    - **Property 23: Order Item Price Snapshot**
    - **Validates: Requirements 4.5, 5.2, 5.4, 5.5, 7.3, 7.4, 7.5**

- [ ] 5. Checkpoint - Ensure Python business logic tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement Node.js business logic services
  - [ ] 6.1 Implement ProductService
    - Create methods for getAll, getById, search, checkInventory, reduceInventory
    - _Requirements: 1.2, 1.4, 4.1, 4.5_
  
  - [ ]* 6.2 Write property tests for ProductService
    - **Property 1: Product Retrieval by ID**
    - **Property 2: Product Response Completeness**
    - **Property 3: Product Search Accuracy**
    - **Validates: Requirements 1.2, 1.3, 1.4**
  
  - [ ] 6.3 Implement CartService
    - Create methods for getCart, addItem, updateItemQuantity, removeItem, clearCart, calculateTotal
    - Implement inventory validation logic
    - _Requirements: 2.1, 2.2, 2.5, 3.1, 3.3, 3.5, 4.1, 4.3_
  
  - [ ]* 6.4 Write property tests for CartService
    - **Property 4: Adding Item to Cart**
    - **Property 5: Adding Existing Item Updates Quantity**
    - **Property 7: Cart Total Calculation**
    - **Property 8: Update Cart Item Quantity**
    - **Property 9: Remove Item from Cart**
    - **Property 10: Clear Cart**
    - **Property 11: Inventory Validation on Add**
    - **Property 12: Inventory Validation on Update**
    - **Property 19: Cart Isolation Between Users**
    - **Validates: Requirements 2.1, 2.2, 2.5, 3.1, 3.3, 3.5, 4.1, 4.3, 6.5**
  
  - [ ] 6.5 Implement OrderService
    - Create methods for checkout, getUserOrders, getOrderById
    - Implement checkout validation and order creation logic
    - _Requirements: 5.2, 5.4, 5.5, 7.3, 7.4_
  
  - [ ]* 6.6 Write property tests for OrderService
    - **Property 13: Inventory Deduction After Checkout**
    - **Property 14: Checkout Inventory Validation**
    - **Property 15: Order Creation from Cart**
    - **Property 16: Cart Cleared After Checkout**
    - **Property 21: Order Retrieval by ID**
    - **Property 22: Order Persistence**
    - **Property 23: Order Item Price Snapshot**
    - **Validates: Requirements 4.5, 5.2, 5.4, 5.5, 7.3, 7.4, 7.5**

- [ ] 7. Checkpoint - Ensure Node.js business logic tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 8. Implement Python REST API endpoints
  - [x] 8.1 Set up Flask/FastAPI application with routing
    - Initialize web framework
    - Configure CORS and JSON serialization
    - Set up error handlers
    - _Requirements: 9.1, 10.1, 10.2_
  
  - [x] 8.2 Implement product endpoints
    - GET /api/products (get all products)
    - GET /api/products/:id (get product by ID)
    - GET /api/products/search (search products)
    - Wire to ProductService
    - _Requirements: 1.1, 1.2, 1.4_
  
  - [x] 8.3 Implement cart endpoints
    - GET /api/carts/:userId (get cart)
    - POST /api/carts/:userId/items (add item)
    - PUT /api/carts/:userId/items/:productId (update quantity)
    - DELETE /api/carts/:userId/items/:productId (remove item)
    - DELETE /api/carts/:userId (clear cart)
    - Wire to CartService
    - _Requirements: 2.1, 2.3, 3.1, 3.3, 3.5_
  
  - [x] 8.4 Implement order endpoints
    - POST /api/orders/:userId/checkout (checkout)
    - GET /api/orders/:userId (get user orders)
    - GET /api/orders/:userId/:orderId (get order by ID)
    - Wire to OrderService
    - _Requirements: 5.1, 7.1, 7.3_
  
  - [ ]* 8.5 Write unit tests for API error handling
    - Test 404 responses for non-existent resources
    - Test 400 responses for invalid inputs
    - Test 500 responses for internal errors
    - **Validates: Requirements 10.3, 10.4, 10.5**

- [ ] 9. Implement Node.js REST API endpoints
  - [ ] 9.1 Set up Express application with routing
    - Initialize Express framework
    - Configure CORS and JSON parsing middleware
    - Set up error handlers
    - _Requirements: 9.2, 10.1, 10.2_
  
  - [ ] 9.2 Implement product endpoints
    - GET /api/products (get all products)
    - GET /api/products/:id (get product by ID)
    - GET /api/products/search (search products)
    - Wire to ProductService
    - _Requirements: 1.1, 1.2, 1.4_
  
  - [ ] 9.3 Implement cart endpoints
    - GET /api/carts/:userId (get cart)
    - POST /api/carts/:userId/items (add item)
    - PUT /api/carts/:userId/items/:productId (update quantity)
    - DELETE /api/carts/:userId/items/:productId (remove item)
    - DELETE /api/carts/:userId (clear cart)
    - Wire to CartService
    - _Requirements: 2.1, 2.3, 3.1, 3.3, 3.5_
  
  - [ ] 9.4 Implement order endpoints
    - POST /api/orders/:userId/checkout (checkout)
    - GET /api/orders/:userId (get user orders)
    - GET /api/orders/:userId/:orderId (get order by ID)
    - Wire to OrderService
    - _Requirements: 5.1, 7.1, 7.3_
  
  - [ ]* 9.5 Write unit tests for API error handling
    - Test 404 responses for non-existent resources
    - Test 400 responses for invalid inputs
    - Test 500 responses for internal errors
    - **Validates: Requirements 10.3, 10.4, 10.5**

- [ ] 10. Implement data initialization and reset functionality
  - [ ] 10.1 Create Python data loader
    - Implement function to load sample data from JSON files
    - Implement function to reset data to initial state
    - _Requirements: 8.1, 8.5_
  
  - [ ] 10.2 Create Node.js data loader
    - Implement function to load sample data from JSON files
    - Implement function to reset data to initial state
    - _Requirements: 8.1, 8.5_
  
  - [ ]* 10.3 Write property test for data reset
    - **Property 24: Data Reset Idempotence**
    - **Validates: Requirements 8.5**

- [ ] 11. Checkpoint - Ensure all API tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ]* 12. Write cross-backend compatibility tests
  - [ ]* 12.1 Write property test for backend equivalence
    - **Property 26: Backend Behavioral Equivalence**
    - Generate random API requests
    - Execute against both Python and Node.js backends
    - Verify responses are equivalent
    - **Validates: Requirements 9.6**
  
  - [ ]* 12.2 Write property test for JSON response format
    - **Property 25: JSON Response Format**
    - Test all endpoints return valid JSON
    - **Validates: Requirements 9.3**

- [ ]* 13. Write comprehensive error handling property tests
  - [ ]* 13.1 Write property tests for error responses
    - **Property 27: Error Response Status Codes**
    - **Property 28: Error Response Format**
    - **Property 29: Not Found Returns 404**
    - **Property 30: Invalid Data Returns 400**
    - **Property 31: Internal Errors Return 500 Without Details**
    - **Validates: Requirements 10.1, 10.2, 10.3, 10.4, 10.5**

- [ ] 14. Create README and setup documentation
  - Document how to run Python backend
  - Document how to run Node.js backend
  - Document API endpoints and usage examples
  - Document how to load sample data
  - _Requirements: All_

- [ ] 15. Final checkpoint - Verify both backends work correctly
  - Ensure all tests pass for both implementations
  - Verify API contracts match between backends
  - Test with sample data
  - Ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Both backends are implemented in parallel to maintain consistency
- Property tests validate universal correctness across all inputs
- Each backend has its own test suite but tests verify the same properties
- Sample data enables immediate testing and demonstration
