"""
Data processing module - refactored to eliminate code duplication.
This module demonstrates best practices for avoiding code duplication.
"""


def validate_data(data, required_fields):
    """
    Generic validation function for data dictionaries.
    
    Args:
        data: The data dictionary to validate
        required_fields: List of required field names
        
    Returns:
        True if validation passes, False otherwise
    """
    if not data:
        print("Error: No data provided")
        return False
    
    if not isinstance(data, dict):
        print("Error: Invalid data format")
        return False
    
    # Validate required fields
    for field in required_fields:
        if field not in data:
            print(f"Error: Missing required field '{field}'")
            return False
    
    return True


def process_data(data, required_fields, processor_func, success_key):
    """
    Generic data processing function.
    
    Args:
        data: The data dictionary to process
        required_fields: List of required field names
        processor_func: Function to process the validated data
        success_key: Key to use in success message
        
    Returns:
        Processed data dictionary or None if validation fails
    """
    if not validate_data(data, required_fields):
        return None
    
    processed = processor_func(data)
    print(f"Successfully processed {success_key}: {processed[success_key]}")
    return processed


def process_user_data(user_data):
    """Process user data from API."""
    def processor(data):
        return {
            'name': data['name'].strip().title(),
            'email': data['email'].strip().lower(),
            'status': 'active'
        }
    
    return process_data(user_data, ['name', 'email'], processor, 'name')


def process_product_data(product_data):
    """Process product data from API."""
    def processor(data):
        return {
            'name': data['name'].strip().title(),
            'price': float(data['price']),
            'status': 'available'
        }
    
    return process_data(product_data, ['name', 'price'], processor, 'name')


def process_order_data(order_data):
    """Process order data from API."""
    def processor(data):
        return {
            'order_id': str(data['order_id']).strip(),
            'amount': float(data['amount']),
            'status': 'pending'
        }
    
    return process_data(order_data, ['order_id', 'amount'], processor, 'order_id')


def apply_discount(base_price, discount_rate, discount_name):
    """
    Generic discount calculation function.
    
    Args:
        base_price: The original price
        discount_rate: The discount rate (0.0 to 1.0)
        discount_name: Name of the discount for logging
        
    Returns:
        Final price after discount
    """
    if discount_rate > 0:
        discount = base_price * discount_rate
        final_price = base_price - discount
        print(f"{discount_name} discount applied: {discount}")
        return final_price
    else:
        print("No discount applied")
        return base_price


# Discount rate mappings
USER_DISCOUNTS = {
    'premium': 0.20,
    'standard': 0.10
}

PRODUCT_DISCOUNTS = {
    'electronics': 0.15,
    'clothing': 0.25
}

SEASONAL_DISCOUNTS = {
    'holiday': 0.30,
    'summer': 0.20
}


def calculate_user_discount(user_type, base_price):
    """Calculate discount for users."""
    discount_rate = USER_DISCOUNTS.get(user_type, 0)
    discount_name = f"{user_type.title()} user" if discount_rate > 0 else ""
    return apply_discount(base_price, discount_rate, discount_name)


def calculate_product_discount(product_category, base_price):
    """Calculate discount for products."""
    discount_rate = PRODUCT_DISCOUNTS.get(product_category, 0)
    discount_name = product_category.title() if discount_rate > 0 else ""
    return apply_discount(base_price, discount_rate, discount_name)


def calculate_seasonal_discount(season, base_price):
    """Calculate seasonal discount."""
    discount_rate = SEASONAL_DISCOUNTS.get(season, 0)
    discount_name = season.title() if discount_rate > 0 else ""
    return apply_discount(base_price, discount_rate, discount_name)
