"""
Examples of Improving Variable and Function Names
This file demonstrates how to transform poorly named variables and functions
into clear, descriptive names that improve code readability.
"""

# ==========================================
# Example 1: Single Letter Variables
# ==========================================

# ❌ BAD: Single letter variables
def calc(a, b, c):
    t = a * b
    r = t * (1 + c)
    return r

# ✅ GOOD: Descriptive variable names
def calculate_total_price_with_tax(price, quantity, tax_rate):
    subtotal = price * quantity
    total_with_tax = subtotal * (1 + tax_rate)
    return total_with_tax


# ==========================================
# Example 2: Vague Names
# ==========================================

# ❌ BAD: Vague, unclear names
def process(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

# ✅ GOOD: Clear, specific names
def double_positive_numbers(numbers):
    doubled_positive_numbers = []
    for number in numbers:
        if number > 0:
            doubled_positive_numbers.append(number * 2)
    return doubled_positive_numbers


# ==========================================
# Example 3: Abbreviations
# ==========================================

# ❌ BAD: Unclear abbreviations
def get_usr_info(usr_id):
    usr_data = {"id": usr_id, "nm": "John", "addr": "123 Main St"}
    return usr_data

# ✅ GOOD: Full, descriptive words
def get_user_information(user_id):
    user_data = {"id": user_id, "name": "John", "address": "123 Main St"}
    return user_data


# ==========================================
# Example 4: Function Names
# ==========================================

# ❌ BAD: Vague function name
def check(email):
    return "@" in email and "." in email

# ✅ GOOD: Function name describes what it does
def is_valid_email_format(email):
    return "@" in email and "." in email


# ❌ BAD: Unclear what function returns
def get(user_id):
    # ... database logic
    return True

# ✅ GOOD: Clear return value indication
def is_user_active(user_id):
    # ... database logic
    return True


# ==========================================
# Example 5: Loop Variables
# ==========================================

# ❌ BAD: Generic loop variables
def sum_prices(items):
    s = 0
    for i in items:
        s += i["p"]
    return s

# ✅ GOOD: Descriptive loop variables
def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product["price"]
    return total_price


# ==========================================
# Example 6: Boolean Variables
# ==========================================

# ❌ BAD: Unclear boolean names
def check_user(user):
    flag = user.get("age") >= 18
    status = user.get("verified")
    return flag and status

# ✅ GOOD: Clear boolean names with is/has/can prefix
def can_user_access_content(user):
    is_adult = user.get("age") >= 18
    is_verified = user.get("verified")
    return is_adult and is_verified


# ==========================================
# Example 7: Constants
# ==========================================

# ❌ BAD: Unclear constant purpose
MAX = 100
MIN = 0
RATE = 0.15

# ✅ GOOD: Clear constant purpose
MAX_LOGIN_ATTEMPTS = 100
MIN_PASSWORD_LENGTH = 0
DEFAULT_TAX_RATE = 0.15


# ==========================================
# Example 8: Class and Method Names
# ==========================================

# ❌ BAD: Vague class and method names
class Manager:
    def do(self, data):
        return data.upper()
    
    def handle(self, items):
        return sorted(items)

# ✅ GOOD: Descriptive class and method names
class UserAccountManager:
    def convert_username_to_uppercase(self, username):
        return username.upper()
    
    def sort_users_by_creation_date(self, users):
        return sorted(users)


# ==========================================
# Example 9: Temporary Variables
# ==========================================

# ❌ BAD: Generic temp variables
def process_order(order):
    temp1 = order["items"]
    temp2 = sum(item["price"] for item in temp1)
    temp3 = temp2 * 1.1
    return temp3

# ✅ GOOD: Meaningful temporary variables
def calculate_order_total_with_service_fee(order):
    order_items = order["items"]
    items_subtotal = sum(item["price"] for item in order_items)
    total_with_service_fee = items_subtotal * 1.1
    return total_with_service_fee


# ==========================================
# Example 10: Context-Specific Names
# ==========================================

# ❌ BAD: Names without context
def update(id, val):
    # What are we updating?
    database.update(id, val)

# ✅ GOOD: Context-specific names
def update_user_email_address(user_id, new_email_address):
    # Clear what we're updating
    database.update(user_id, new_email_address)


# ==========================================
# Example 11: Collection Names
# ==========================================

# ❌ BAD: Generic collection names
def filter_data(list1):
    list2 = []
    for x in list1:
        if x.active:
            list2.append(x)
    return list2

# ✅ GOOD: Descriptive collection names
def filter_active_users(all_users):
    active_users = []
    for user in all_users:
        if user.active:
            active_users.append(user)
    return active_users


# ==========================================
# Example 12: Time-Related Variables
# ==========================================

# ❌ BAD: Unclear time units
def wait(t):
    import time
    time.sleep(t)

# ✅ GOOD: Clear time units in name
def wait_for_seconds(duration_in_seconds):
    import time
    time.sleep(duration_in_seconds)


if __name__ == "__main__":
    print("✨ Variable and Function Naming Examples")
    print("=" * 50)
    
    # Test Example 1
    print("\nExample 1: Calculate Price with Tax")
    total = calculate_total_price_with_tax(100, 2, 0.08)
    print(f"Total: ${total:.2f}")
    
    # Test Example 2
    print("\nExample 2: Double Positive Numbers")
    numbers = [-5, 10, -3, 20, 15]
    result = double_positive_numbers(numbers)
    print(f"Doubled positive numbers: {result}")
    
    # Test Example 4
    print("\nExample 4: Email Validation")
    email = "test@example.com"
    is_valid = is_valid_email_format(email)
    print(f"Is '{email}' valid? {is_valid}")
    
    print("\n" + "=" * 50)
    print("✅ All examples demonstrate improved naming!")
