"""
Descriptive Variable and Function Naming Examples
==================================================

This module demonstrates best practices for naming variables and functions
to make code more readable, maintainable, and self-documenting.
"""

# ============================================================================
# EXAMPLE 1: User Data Processing
# ============================================================================

# ❌ BAD: Non-descriptive names
def proc(d):
    x = d.get('n')
    y = d.get('a')
    return f"{x}, {y}"

# ✅ GOOD: Descriptive names
def format_user_address(user_data):
    """Format user's address into a readable string."""
    user_name = user_data.get('name')
    user_address = user_data.get('address')
    return f"{user_name}, {user_address}"


# ============================================================================
# EXAMPLE 2: Mathematical Calculations
# ============================================================================

# ❌ BAD: Single-letter variables that don't convey meaning
def calc(a, b, c):
    x = (a * b) / c
    return x

# ✅ GOOD: Clear variable names that explain purpose
def calculate_unit_price(total_cost, quantity, tax_rate):
    """Calculate the unit price including tax."""
    price_after_tax = (total_cost * tax_rate) / quantity
    return price_after_tax


# ============================================================================
# EXAMPLE 3: Date and Time Operations
# ============================================================================

# ❌ BAD: Abbreviated and unclear names
def dt_diff(dt1, dt2):
    d = dt2 - dt1
    return d.days

# ✅ GOOD: Full, descriptive names
def calculate_days_between_dates(start_date, end_date):
    """Calculate the number of days between two dates."""
    date_difference = end_date - start_date
    return date_difference.days


# ============================================================================
# EXAMPLE 4: String Validation
# ============================================================================

# ❌ BAD: Generic and vague names
def check(s):
    if len(s) > 0 and len(s) < 100:
        return True
    return False

# ✅ GOOD: Names that describe what is being checked
def is_valid_username_length(username):
    """Check if username length is within valid range (1-99 characters)."""
    minimum_username_length = 1
    maximum_username_length = 99
    
    username_length = len(username)
    is_within_valid_range = (
        username_length >= minimum_username_length and 
        username_length <= maximum_username_length
    )
    
    return is_within_valid_range


# ============================================================================
# EXAMPLE 5: List Processing
# ============================================================================

# ❌ BAD: Meaningless variable names
def proc_list(l):
    t = 0
    for i in l:
        if i > 0:
            t += i
    return t

# ✅ GOOD: Variables that explain their purpose
def calculate_sum_of_positive_numbers(number_list):
    """Calculate the sum of all positive numbers in a list."""
    sum_of_positive_numbers = 0
    
    for current_number in number_list:
        if current_number > 0:
            sum_of_positive_numbers += current_number
    
    return sum_of_positive_numbers


# ============================================================================
# EXAMPLE 6: File Operations
# ============================================================================

# ❌ BAD: Unclear abbreviations
def rd_f(p):
    with open(p, 'r') as f:
        c = f.read()
    return c

# ✅ GOOD: Clear, full names
def read_configuration_file(file_path):
    """Read and return the contents of a configuration file."""
    with open(file_path, 'r') as configuration_file:
        file_contents = configuration_file.read()
    
    return file_contents


# ============================================================================
# EXAMPLE 7: Boolean Functions and Flags
# ============================================================================

# ❌ BAD: Unclear boolean names
def chk_usr(u):
    flg = False
    if u.get('age') >= 18:
        flg = True
    return flg

# ✅ GOOD: Boolean names with is/has/can prefixes
def is_user_adult(user_profile):
    """Check if user is an adult (18 years or older)."""
    minimum_adult_age = 18
    user_age = user_profile.get('age')
    
    is_adult = user_age >= minimum_adult_age
    return is_adult


# ============================================================================
# EXAMPLE 8: API Response Handling
# ============================================================================

# ❌ BAD: Generic names that don't explain the data structure
def get_data(url):
    r = fetch_api(url)
    if r['s'] == 200:
        d = r['d']
        return d
    return None

# ✅ GOOD: Names that describe the data and its purpose
def fetch_user_profile_from_api(api_endpoint_url):
    """Fetch user profile data from API endpoint."""
    api_response = fetch_api(api_endpoint_url)
    http_status_code = api_response['status']
    
    is_successful_response = http_status_code == 200
    
    if is_successful_response:
        user_profile_data = api_response['data']
        return user_profile_data
    
    return None


# ============================================================================
# EXAMPLE 9: Loop Counters and Iterators
# ============================================================================

# ❌ BAD: Generic loop variables when processing complex data
def proc_items(items):
    for i in items:
        for j in i['tags']:
            print(j)

# ✅ GOOD: Descriptive loop variables
def display_product_tags(product_list):
    """Display all tags for each product in the list."""
    for product in product_list:
        product_tags = product['tags']
        
        for individual_tag in product_tags:
            print(individual_tag)


# ============================================================================
# EXAMPLE 10: Class and Method Names
# ============================================================================

# ❌ BAD: Vague class and method names
class DataProc:
    def __init__(self, d):
        self.d = d
    
    def do_thing(self):
        return self.d * 2

# ✅ GOOD: Clear class and method names
class TemperatureConverter:
    """Convert temperatures between different scales."""
    
    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature
    
    def convert_to_fahrenheit(self):
        """Convert Celsius temperature to Fahrenheit."""
        fahrenheit_temperature = (self.celsius_temperature * 9/5) + 32
        return fahrenheit_temperature


# ============================================================================
# Naming Best Practices Summary
# ============================================================================
"""
KEY PRINCIPLES FOR DESCRIPTIVE NAMING:

1. **Be Specific**: Use names that clearly describe what the variable contains
   or what the function does.

2. **Avoid Abbreviations**: Write full words unless the abbreviation is 
   universally understood (e.g., URL, API, HTTP).

3. **Use Verbs for Functions**: Functions should typically start with verbs
   (calculate, fetch, validate, format, process).

4. **Use Nouns for Variables**: Variables should be nouns or noun phrases
   that describe the data they contain.

5. **Boolean Naming**: Boolean variables should use prefixes like is_, has_, 
   can_, should_ to make their purpose clear.

6. **Be Consistent**: Use consistent naming patterns throughout your codebase.

7. **Avoid Generic Names**: Names like data, temp, info, value are too generic.
   Be more specific about what the data represents.

8. **Length vs Clarity**: Don't make names unnecessarily long, but don't 
   sacrifice clarity for brevity either.

9. **Context Matters**: Use the context to inform naming. In a loop over 
   users, 'user' is better than 'u' or 'item'.

10. **Searchability**: Good names make it easier to search and find code.
"""


# Example usage demonstration
if __name__ == "__main__":
    # Example 1: User address formatting
    sample_user = {
        'name': 'Jane Smith',
        'address': '123 Main Street, Springfield'
    }
    formatted_address = format_user_address(sample_user)
    print(f"Formatted Address: {formatted_address}")
    
    # Example 4: Username validation
    test_username = "john_doe_2024"
    is_valid = is_valid_username_length(test_username)
    print(f"Username '{test_username}' is valid: {is_valid}")
    
    # Example 5: Sum of positive numbers
    numbers = [-5, 10, 3, -2, 8, 15]
    positive_sum = calculate_sum_of_positive_numbers(numbers)
    print(f"Sum of positive numbers in {numbers}: {positive_sum}")
    
    # Example 7: Adult verification
    user = {'age': 25}
    is_adult = is_user_adult(user)
    print(f"User is adult: {is_adult}")
    
    # Example 10: Temperature conversion
    temp_converter = TemperatureConverter(25)
    fahrenheit = temp_converter.convert_to_fahrenheit()
    print(f"25°C = {fahrenheit}°F")
