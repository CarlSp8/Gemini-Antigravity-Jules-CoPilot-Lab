"""
E-Commerce Shopping Cart - Advanced Naming Example
===================================================

A realistic example demonstrating descriptive naming in a complete mini-application.
This module implements a simple shopping cart system with proper naming conventions.
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# Enums with Descriptive Names
# ============================================================================

class ProductCategory(Enum):
    """Product category enumeration with clear, descriptive names."""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"
    HOME_AND_GARDEN = "home_and_garden"
    SPORTS_AND_OUTDOORS = "sports_and_outdoors"


class OrderStatus(Enum):
    """Order status enumeration representing the order lifecycle."""
    PENDING_PAYMENT = "pending_payment"
    PAYMENT_CONFIRMED = "payment_confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# ============================================================================
# Data Classes with Descriptive Field Names
# ============================================================================

@dataclass
class Product:
    """Product information with descriptive field names."""
    product_id: str
    product_name: str
    product_description: str
    unit_price: float
    category: ProductCategory
    stock_quantity: int
    is_available: bool
    
    def has_sufficient_stock(self, requested_quantity: int) -> bool:
        """Check if there's enough stock to fulfill the requested quantity."""
        return self.stock_quantity >= requested_quantity


@dataclass
class CartItem:
    """Shopping cart item with clear field names."""
    product: Product
    quantity: int
    added_at_timestamp: datetime
    
    def calculate_item_subtotal(self) -> float:
        """Calculate the subtotal for this cart item (quantity × unit price)."""
        item_subtotal = self.product.unit_price * self.quantity
        return item_subtotal


@dataclass
class ShippingAddress:
    """Customer shipping address with descriptive fields."""
    street_address: str
    apartment_or_suite_number: Optional[str]
    city_name: str
    state_or_province: str
    postal_code: str
    country_code: str
    
    def format_complete_address(self) -> str:
        """Format the complete shipping address as a multi-line string."""
        address_lines = [self.street_address]
        
        if self.apartment_or_suite_number:
            address_lines.append(self.apartment_or_suite_number)
        
        city_state_zip = f"{self.city_name}, {self.state_or_province} {self.postal_code}"
        address_lines.append(city_state_zip)
        address_lines.append(self.country_code)
        
        complete_formatted_address = "\n".join(address_lines)
        return complete_formatted_address


# ============================================================================
# Shopping Cart Class with Descriptive Methods
# ============================================================================

class ShoppingCart:
    """
    Shopping cart with descriptive method and variable names.
    
    Demonstrates proper naming for a complete class with multiple operations.
    """
    
    def __init__(self, customer_id: str):
        """Initialize a shopping cart for a specific customer."""
        self.customer_id: str = customer_id
        self.cart_items: List[CartItem] = []
        self.cart_created_at: datetime = datetime.now()
        self.applied_discount_code: Optional[str] = None
        self.discount_percentage: float = 0.0
    
    def add_product_to_cart(self, product: Product, desired_quantity: int) -> bool:
        """
        Add a product to the cart with the specified quantity.
        
        Returns True if successful, False if insufficient stock.
        """
        # Check if product has sufficient stock
        if not product.has_sufficient_stock(desired_quantity):
            return False
        
        # Check if product already exists in cart
        existing_cart_item = self._find_cart_item_by_product_id(product.product_id)
        
        if existing_cart_item:
            # Update quantity of existing item
            existing_cart_item.quantity += desired_quantity
        else:
            # Create new cart item
            new_cart_item = CartItem(
                product=product,
                quantity=desired_quantity,
                added_at_timestamp=datetime.now()
            )
            self.cart_items.append(new_cart_item)
        
        return True
    
    def remove_product_from_cart(self, product_id: str) -> bool:
        """Remove a product completely from the cart."""
        cart_item_to_remove = self._find_cart_item_by_product_id(product_id)
        
        if cart_item_to_remove:
            self.cart_items.remove(cart_item_to_remove)
            return True
        
        return False
    
    def update_product_quantity(self, product_id: str, new_quantity: int) -> bool:
        """Update the quantity of a product in the cart."""
        cart_item_to_update = self._find_cart_item_by_product_id(product_id)
        
        if not cart_item_to_update:
            return False
        
        # Check if new quantity is available
        if not cart_item_to_update.product.has_sufficient_stock(new_quantity):
            return False
        
        cart_item_to_update.quantity = new_quantity
        return True
    
    def apply_discount_code(self, discount_code: str, discount_rate: float) -> bool:
        """Apply a discount code to the cart."""
        # Validate discount rate
        is_valid_discount_rate = 0.0 <= discount_rate <= 1.0
        
        if not is_valid_discount_rate:
            return False
        
        self.applied_discount_code = discount_code
        self.discount_percentage = discount_rate
        return True
    
    def calculate_subtotal_before_discount(self) -> float:
        """Calculate the total price before applying any discounts."""
        subtotal_amount = 0.0
        
        for cart_item in self.cart_items:
            item_subtotal = cart_item.calculate_item_subtotal()
            subtotal_amount += item_subtotal
        
        return subtotal_amount
    
    def calculate_discount_amount(self) -> float:
        """Calculate the discount amount based on applied discount code."""
        subtotal_before_discount = self.calculate_subtotal_before_discount()
        discount_amount = subtotal_before_discount * self.discount_percentage
        return discount_amount
    
    def calculate_total_after_discount(self) -> float:
        """Calculate the final total after applying discount."""
        subtotal = self.calculate_subtotal_before_discount()
        discount = self.calculate_discount_amount()
        final_total = subtotal - discount
        return final_total
    
    def get_total_item_count(self) -> int:
        """Get the total number of items in the cart (sum of all quantities)."""
        total_item_count = 0
        
        for cart_item in self.cart_items:
            total_item_count += cart_item.quantity
        
        return total_item_count
    
    def is_cart_empty(self) -> bool:
        """Check if the shopping cart is empty."""
        return len(self.cart_items) == 0
    
    def clear_entire_cart(self) -> None:
        """Remove all items from the cart."""
        self.cart_items.clear()
        self.applied_discount_code = None
        self.discount_percentage = 0.0
    
    def _find_cart_item_by_product_id(self, product_id: str) -> Optional[CartItem]:
        """
        Private helper method to find a cart item by product ID.
        
        Note: Private methods use underscore prefix in Python.
        """
        for cart_item in self.cart_items:
            if cart_item.product.product_id == product_id:
                return cart_item
        
        return None
    
    def generate_cart_summary(self) -> Dict[str, Any]:
        """Generate a comprehensive summary of the shopping cart."""
        cart_summary = {
            'customer_id': self.customer_id,
            'total_unique_products': len(self.cart_items),
            'total_item_count': self.get_total_item_count(),
            'subtotal_before_discount': self.calculate_subtotal_before_discount(),
            'discount_code': self.applied_discount_code,
            'discount_amount': self.calculate_discount_amount(),
            'final_total': self.calculate_total_after_discount(),
            'is_empty': self.is_cart_empty(),
            'created_at': self.cart_created_at.isoformat()
        }
        
        return cart_summary


# ============================================================================
# Order Processing Class
# ============================================================================

class OrderProcessor:
    """Process orders with clear, descriptive method names."""
    
    def __init__(self):
        """Initialize the order processor."""
        self.processed_orders: List[Dict] = []
    
    def create_order_from_cart(
        self,
        shopping_cart: ShoppingCart,
        shipping_address: ShippingAddress,
        payment_method: str
    ) -> Optional[str]:
        """
        Create an order from a shopping cart.
        
        Returns order ID if successful, None if cart is empty.
        """
        # Validate cart is not empty
        if shopping_cart.is_cart_empty():
            return None
        
        # Generate unique order ID
        order_timestamp = datetime.now()
        order_id = self._generate_unique_order_id(order_timestamp)
        
        # Create order record
        new_order = {
            'order_id': order_id,
            'customer_id': shopping_cart.customer_id,
            'order_items': [
                {
                    'product_id': item.product.product_id,
                    'product_name': item.product.product_name,
                    'quantity': item.quantity,
                    'unit_price': item.product.unit_price,
                    'subtotal': item.calculate_item_subtotal()
                }
                for item in shopping_cart.cart_items
            ],
            'shipping_address': shipping_address.format_complete_address(),
            'payment_method': payment_method,
            'subtotal_amount': shopping_cart.calculate_subtotal_before_discount(),
            'discount_amount': shopping_cart.calculate_discount_amount(),
            'total_amount': shopping_cart.calculate_total_after_discount(),
            'order_status': OrderStatus.PENDING_PAYMENT.value,
            'created_at': order_timestamp.isoformat()
        }
        
        self.processed_orders.append(new_order)
        return order_id
    
    def update_order_status(self, order_id: str, new_status: OrderStatus) -> bool:
        """Update the status of an existing order."""
        order_to_update = self._find_order_by_id(order_id)
        
        if order_to_update:
            order_to_update['order_status'] = new_status.value
            return True
        
        return False
    
    def _generate_unique_order_id(self, timestamp: datetime) -> str:
        """Generate a unique order ID based on timestamp."""
        timestamp_string = timestamp.strftime("%Y%m%d%H%M%S")
        order_count = len(self.processed_orders) + 1
        unique_order_id = f"ORD-{timestamp_string}-{order_count:05d}"
        return unique_order_id
    
    def _find_order_by_id(self, order_id: str) -> Optional[Dict]:
        """Find an order by its unique ID."""
        for order in self.processed_orders:
            if order['order_id'] == order_id:
                return order
        
        return None


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == "__main__":
    print("=== E-Commerce Shopping Cart Demo ===\n")
    
    # Create sample products with descriptive variable names
    laptop_product = Product(
        product_id="ELEC-001",
        product_name="Professional Laptop",
        product_description="High-performance laptop for professionals",
        unit_price=1299.99,
        category=ProductCategory.ELECTRONICS,
        stock_quantity=50,
        is_available=True
    )
    
    book_product = Product(
        product_id="BOOK-001",
        product_name="Clean Code",
        product_description="A handbook of agile software craftsmanship",
        unit_price=39.99,
        category=ProductCategory.BOOKS,
        stock_quantity=100,
        is_available=True
    )
    
    # Create shopping cart
    customer_cart = ShoppingCart(customer_id="CUST-12345")
    
    # Add products to cart
    print("Adding products to cart...")
    laptop_added_successfully = customer_cart.add_product_to_cart(laptop_product, 1)
    book_added_successfully = customer_cart.add_product_to_cart(book_product, 2)
    
    print(f"Laptop added: {laptop_added_successfully}")
    print(f"Books added: {book_added_successfully}")
    
    # Apply discount
    print("\nApplying discount code...")
    discount_applied = customer_cart.apply_discount_code("SAVE10", 0.10)
    print(f"Discount applied: {discount_applied}")
    
    # Display cart summary
    print("\n--- Cart Summary ---")
    cart_summary = customer_cart.generate_cart_summary()
    print(f"Customer ID: {cart_summary['customer_id']}")
    print(f"Total items: {cart_summary['total_item_count']}")
    print(f"Subtotal: ${cart_summary['subtotal_before_discount']:.2f}")
    print(f"Discount: -${cart_summary['discount_amount']:.2f}")
    print(f"Final total: ${cart_summary['final_total']:.2f}")
    
    # Create shipping address
    customer_shipping_address = ShippingAddress(
        street_address="123 Main Street",
        apartment_or_suite_number="Apt 4B",
        city_name="Springfield",
        state_or_province="IL",
        postal_code="62701",
        country_code="USA"
    )
    
    # Process order
    print("\n--- Processing Order ---")
    order_processor = OrderProcessor()
    new_order_id = order_processor.create_order_from_cart(
        shopping_cart=customer_cart,
        shipping_address=customer_shipping_address,
        payment_method="Credit Card"
    )
    
    print(f"Order created successfully!")
    print(f"Order ID: {new_order_id}")
    
    # Update order status
    status_updated = order_processor.update_order_status(
        new_order_id,
        OrderStatus.PAYMENT_CONFIRMED
    )
    print(f"Order status updated: {status_updated}")
    
    print("\n=== Demo Complete ===")
