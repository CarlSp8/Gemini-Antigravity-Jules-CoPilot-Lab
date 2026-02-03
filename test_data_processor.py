"""
Tests for data_processor module.
"""

import unittest
from data_processor import (
    process_user_data,
    process_product_data,
    process_order_data,
    calculate_user_discount,
    calculate_product_discount,
    calculate_seasonal_discount,
    validate_data,
    apply_discount
)


class TestDataProcessor(unittest.TestCase):
    """Test cases for data processing functions."""
    
    def test_process_user_data_valid(self):
        """Test processing valid user data."""
        user_data = {'name': '  john doe  ', 'email': '  JOHN@EXAMPLE.COM  '}
        result = process_user_data(user_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'John Doe')
        self.assertEqual(result['email'], 'john@example.com')
        self.assertEqual(result['status'], 'active')
    
    def test_process_user_data_missing_field(self):
        """Test processing user data with missing field."""
        user_data = {'name': 'John Doe'}
        result = process_user_data(user_data)
        self.assertIsNone(result)
    
    def test_process_user_data_empty(self):
        """Test processing empty user data."""
        result = process_user_data(None)
        self.assertIsNone(result)
    
    def test_process_user_data_invalid_type(self):
        """Test processing user data with invalid type."""
        result = process_user_data("invalid")
        self.assertIsNone(result)
    
    def test_process_product_data_valid(self):
        """Test processing valid product data."""
        product_data = {'name': '  laptop  ', 'price': '999.99'}
        result = process_product_data(product_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Laptop')
        self.assertEqual(result['price'], 999.99)
        self.assertEqual(result['status'], 'available')
    
    def test_process_order_data_valid(self):
        """Test processing valid order data."""
        order_data = {'order_id': '  ORD123  ', 'amount': '150.50'}
        result = process_order_data(order_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['order_id'], 'ORD123')
        self.assertEqual(result['amount'], 150.50)
        self.assertEqual(result['status'], 'pending')
    
    def test_calculate_user_discount_premium(self):
        """Test premium user discount calculation."""
        result = calculate_user_discount('premium', 100)
        self.assertEqual(result, 80.0)
    
    def test_calculate_user_discount_standard(self):
        """Test standard user discount calculation."""
        result = calculate_user_discount('standard', 100)
        self.assertEqual(result, 90.0)
    
    def test_calculate_user_discount_none(self):
        """Test no user discount."""
        result = calculate_user_discount('guest', 100)
        self.assertEqual(result, 100)
    
    def test_calculate_product_discount_electronics(self):
        """Test electronics discount calculation."""
        result = calculate_product_discount('electronics', 100)
        self.assertEqual(result, 85.0)
    
    def test_calculate_product_discount_clothing(self):
        """Test clothing discount calculation."""
        result = calculate_product_discount('clothing', 100)
        self.assertEqual(result, 75.0)
    
    def test_calculate_product_discount_none(self):
        """Test no product discount."""
        result = calculate_product_discount('unknown', 100)
        self.assertEqual(result, 100)
    
    def test_calculate_seasonal_discount_holiday(self):
        """Test holiday discount calculation."""
        result = calculate_seasonal_discount('holiday', 100)
        self.assertEqual(result, 70.0)
    
    def test_calculate_seasonal_discount_summer(self):
        """Test summer discount calculation."""
        result = calculate_seasonal_discount('summer', 100)
        self.assertEqual(result, 80.0)
    
    def test_calculate_seasonal_discount_none(self):
        """Test no seasonal discount."""
        result = calculate_seasonal_discount('winter', 100)
        self.assertEqual(result, 100)


class TestHelperFunctions(unittest.TestCase):
    """Test cases for helper functions."""
    
    def test_validate_data_valid(self):
        """Test validation with valid data."""
        data = {'name': 'Test', 'email': 'test@example.com'}
        result = validate_data(data, ['name', 'email'])
        self.assertTrue(result)
    
    def test_validate_data_missing_field(self):
        """Test validation with missing field."""
        data = {'name': 'Test'}
        result = validate_data(data, ['name', 'email'])
        self.assertFalse(result)
    
    def test_validate_data_none(self):
        """Test validation with None data."""
        result = validate_data(None, ['name'])
        self.assertFalse(result)
    
    def test_validate_data_invalid_type(self):
        """Test validation with invalid type."""
        result = validate_data("string", ['name'])
        self.assertFalse(result)
    
    def test_apply_discount_with_rate(self):
        """Test discount application with rate."""
        result = apply_discount(100, 0.20, "Test")
        self.assertEqual(result, 80.0)
    
    def test_apply_discount_no_rate(self):
        """Test discount application without rate."""
        result = apply_discount(100, 0, "Test")
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
