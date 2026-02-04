"""
Shopping Cart Example: Before and After Naming Improvements
This example demonstrates how descriptive names improve code readability
in a real-world scenario.
"""

from typing import List, Dict
from dataclasses import dataclass


# ==========================================
# ❌ BAD: Poor Naming Example
# ==========================================

class Cart:
    def __init__(self):
        self.i = []
        self.t = 0
    
    def add(self, p, q, pr):
        """Add item to cart"""
        item = {"p": p, "q": q, "pr": pr}
        self.i.append(item)
        self.calc()
    
    def calc(self):
        """Calculate total"""
        self.t = sum(item["q"] * item["pr"] for item in self.i)
    
    def get(self):
        """Get total"""
        return self.t
    
    def check(self, c):
        """Check if coupon valid"""
        return c in ["SAVE10", "SAVE20"]
    
    def apply(self, c):
        """Apply discount"""
        if self.check(c):
            if c == "SAVE10":
                self.t *= 0.9
            elif c == "SAVE20":
                self.t *= 0.8


# ==========================================
# ✅ GOOD: Descriptive Naming Example
# ==========================================

@dataclass
class CartItem:
    """Represents a single item in the shopping cart"""
    product_name: str
    quantity: int
    unit_price: float
    
    def calculate_line_total(self) -> float:
        """Calculate the total price for this line item"""
        return self.quantity * self.unit_price


class ShoppingCart:
    """Manages shopping cart operations including items and pricing"""
    
    VALID_COUPON_CODES = {
        "SAVE10": 0.10,  # 10% discount
        "SAVE20": 0.20,  # 20% discount
        "SAVE30": 0.30   # 30% discount
    }
    
    def __init__(self):
        self.cart_items: List[CartItem] = []
        self.subtotal: float = 0.0
        self.discount_amount: float = 0.0
        self.applied_coupon_code: str = None
    
    def add_item_to_cart(self, product_name: str, quantity: int, unit_price: float) -> None:
        """
        Add a new item to the shopping cart
        
        Args:
            product_name: Name of the product being added
            quantity: Number of units to add
            unit_price: Price per unit
        """
        new_item = CartItem(
            product_name=product_name,
            quantity=quantity,
            unit_price=unit_price
        )
        self.cart_items.append(new_item)
        self._recalculate_cart_totals()
    
    def remove_item_from_cart(self, product_name: str) -> bool:
        """
        Remove an item from the cart by product name
        
        Args:
            product_name: Name of the product to remove
            
        Returns:
            True if item was removed, False if not found
        """
        for index, item in enumerate(self.cart_items):
            if item.product_name == product_name:
                self.cart_items.pop(index)
                self._recalculate_cart_totals()
                return True
        return False
    
    def update_item_quantity(self, product_name: str, new_quantity: int) -> bool:
        """
        Update the quantity of an existing cart item
        
        Args:
            product_name: Name of the product to update
            new_quantity: New quantity for the item
            
        Returns:
            True if updated successfully, False if item not found
        """
        for item in self.cart_items:
            if item.product_name == product_name:
                item.quantity = new_quantity
                self._recalculate_cart_totals()
                return True
        return False
    
    def _recalculate_cart_totals(self) -> None:
        """
        Recalculate the subtotal and apply any discounts
        This is a private method called after cart modifications
        """
        self.subtotal = sum(
            item.calculate_line_total() 
            for item in self.cart_items
        )
        
        # Reapply coupon if one was already applied
        if self.applied_coupon_code:
            self._apply_discount_from_coupon(self.applied_coupon_code)
    
    def is_valid_coupon_code(self, coupon_code: str) -> bool:
        """
        Check if a coupon code is valid
        
        Args:
            coupon_code: The coupon code to validate
            
        Returns:
            True if the coupon code exists and is valid
        """
        return coupon_code in self.VALID_COUPON_CODES
    
    def apply_coupon_code(self, coupon_code: str) -> bool:
        """
        Apply a coupon code to get a discount
        
        Args:
            coupon_code: The coupon code to apply
            
        Returns:
            True if coupon was applied successfully, False otherwise
        """
        if self.is_valid_coupon_code(coupon_code):
            self.applied_coupon_code = coupon_code
            self._apply_discount_from_coupon(coupon_code)
            return True
        return False
    
    def _apply_discount_from_coupon(self, coupon_code: str) -> None:
        """
        Calculate and apply the discount for a given coupon
        This is a private method called by apply_coupon_code
        
        Args:
            coupon_code: The coupon code to use for discount calculation
        """
        discount_percentage = self.VALID_COUPON_CODES[coupon_code]
        self.discount_amount = self.subtotal * discount_percentage
    
    def get_subtotal(self) -> float:
        """Get the cart subtotal before any discounts"""
        return self.subtotal
    
    def get_discount_amount(self) -> float:
        """Get the discount amount from applied coupons"""
        return self.discount_amount
    
    def get_total_amount_due(self) -> float:
        """
        Get the final total amount after all discounts
        
        Returns:
            The final amount the customer needs to pay
        """
        return self.subtotal - self.discount_amount
    
    def get_item_count(self) -> int:
        """Get the total number of unique items in the cart"""
        return len(self.cart_items)
    
    def get_total_quantity(self) -> int:
        """Get the total quantity of all items combined"""
        return sum(item.quantity for item in self.cart_items)
    
    def clear_cart(self) -> None:
        """Remove all items from the cart and reset totals"""
        self.cart_items.clear()
        self.subtotal = 0.0
        self.discount_amount = 0.0
        self.applied_coupon_code = None
    
    def get_cart_summary(self) -> Dict:
        """
        Get a complete summary of the cart
        
        Returns:
            Dictionary containing cart details and totals
        """
        return {
            "items": [
                {
                    "product_name": item.product_name,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "line_total": item.calculate_line_total()
                }
                for item in self.cart_items
            ],
            "subtotal": self.subtotal,
            "discount_amount": self.discount_amount,
            "applied_coupon": self.applied_coupon_code,
            "total_amount_due": self.get_total_amount_due(),
            "item_count": self.get_item_count(),
            "total_quantity": self.get_total_quantity()
        }


# ==========================================
# Demo Usage
# ==========================================

if __name__ == "__main__":
    print("🛒 Shopping Cart Demo - Descriptive Naming Example")
    print("=" * 60)
    
    # Create a new shopping cart
    customer_cart = ShoppingCart()
    
    # Add items to cart
    print("\n📦 Adding items to cart...")
    customer_cart.add_item_to_cart("Laptop", 1, 999.99)
    customer_cart.add_item_to_cart("Mouse", 2, 29.99)
    customer_cart.add_item_to_cart("Keyboard", 1, 79.99)
    
    # Display cart summary
    print("\n📋 Cart Summary:")
    cart_summary = customer_cart.get_cart_summary()
    for item in cart_summary["items"]:
        print(f"  - {item['product_name']}: "
              f"{item['quantity']} x ${item['unit_price']:.2f} = "
              f"${item['line_total']:.2f}")
    
    print(f"\nSubtotal: ${cart_summary['subtotal']:.2f}")
    print(f"Total items: {cart_summary['item_count']}")
    print(f"Total quantity: {cart_summary['total_quantity']}")
    
    # Apply coupon code
    print("\n💰 Applying coupon code 'SAVE20'...")
    coupon_applied = customer_cart.apply_coupon_code("SAVE20")
    
    if coupon_applied:
        print("✅ Coupon applied successfully!")
        updated_summary = customer_cart.get_cart_summary()
        print(f"Discount: -${updated_summary['discount_amount']:.2f}")
        print(f"Total due: ${updated_summary['total_amount_due']:.2f}")
    else:
        print("❌ Invalid coupon code")
    
    # Update quantity
    print("\n🔄 Updating mouse quantity from 2 to 3...")
    customer_cart.update_item_quantity("Mouse", 3)
    
    final_summary = customer_cart.get_cart_summary()
    print(f"New total due: ${final_summary['total_amount_due']:.2f}")
    
    print("\n" + "=" * 60)
    print("✅ Notice how descriptive names make the code self-documenting!")
    print("   - Functions clearly state what they do")
    print("   - Variables reveal their purpose")
    print("   - No need to guess what 'i', 't', or 'calc' mean")
