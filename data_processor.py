"""
Data processing module with duplicated code patterns.
This module demonstrates common code duplication issues.
"""

def process_user_data(user_data):
    """Process user data from API."""
    if not user_data:
        print("Error: No data provided")
        return None
    
    if not isinstance(user_data, dict):
        print("Error: Invalid data format")
        return None
    
    # Validate required fields
    if 'name' not in user_data:
        print("Error: Missing required field 'name'")
        return None
    
    if 'email' not in user_data:
        print("Error: Missing required field 'email'")
        return None
    
    # Process the data
    processed = {
        'name': user_data['name'].strip().title(),
        'email': user_data['email'].strip().lower(),
        'status': 'active'
    }
    
    print(f"Successfully processed user: {processed['name']}")
    return processed


def process_product_data(product_data):
    """Process product data from API."""
    if not product_data:
        print("Error: No data provided")
        return None
    
    if not isinstance(product_data, dict):
        print("Error: Invalid data format")
        return None
    
    # Validate required fields
    if 'name' not in product_data:
        print("Error: Missing required field 'name'")
        return None
    
    if 'price' not in product_data:
        print("Error: Missing required field 'price'")
        return None
    
    # Process the data
    processed = {
        'name': product_data['name'].strip().title(),
        'price': float(product_data['price']),
        'status': 'available'
    }
    
    print(f"Successfully processed product: {processed['name']}")
    return processed


def process_order_data(order_data):
    """Process order data from API."""
    if not order_data:
        print("Error: No data provided")
        return None
    
    if not isinstance(order_data, dict):
        print("Error: Invalid data format")
        return None
    
    # Validate required fields
    if 'order_id' not in order_data:
        print("Error: Missing required field 'order_id'")
        return None
    
    if 'amount' not in order_data:
        print("Error: Missing required field 'amount'")
        return None
    
    # Process the data
    processed = {
        'order_id': str(order_data['order_id']).strip(),
        'amount': float(order_data['amount']),
        'status': 'pending'
    }
    
    print(f"Successfully processed order: {processed['order_id']}")
    return processed


def calculate_user_discount(user_type, base_price):
    """Calculate discount for users."""
    if user_type == 'premium':
        discount = base_price * 0.20
        final_price = base_price - discount
        print(f"Premium user discount applied: {discount}")
        return final_price
    elif user_type == 'standard':
        discount = base_price * 0.10
        final_price = base_price - discount
        print(f"Standard user discount applied: {discount}")
        return final_price
    else:
        print("No discount applied")
        return base_price


def calculate_product_discount(product_category, base_price):
    """Calculate discount for products."""
    if product_category == 'electronics':
        discount = base_price * 0.15
        final_price = base_price - discount
        print(f"Electronics discount applied: {discount}")
        return final_price
    elif product_category == 'clothing':
        discount = base_price * 0.25
        final_price = base_price - discount
        print(f"Clothing discount applied: {discount}")
        return final_price
    else:
        print("No discount applied")
        return base_price


def calculate_seasonal_discount(season, base_price):
    """Calculate seasonal discount."""
    if season == 'holiday':
        discount = base_price * 0.30
        final_price = base_price - discount
        print(f"Holiday discount applied: {discount}")
        return final_price
    elif season == 'summer':
        discount = base_price * 0.20
        final_price = base_price - discount
        print(f"Summer discount applied: {discount}")
        return final_price
    else:
        print("No discount applied")
        return base_price
