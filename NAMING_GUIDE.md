# Descriptive Variable and Function Naming Guide

## Overview

This guide provides best practices for creating descriptive variable and function names that make your code more readable, maintainable, and self-documenting.

## Why Descriptive Names Matter

- **Readability**: Code is read far more often than it's written
- **Maintainability**: Future developers (including yourself) can understand code faster
- **Self-Documentation**: Good names reduce the need for comments
- **Debugging**: Clear names make it easier to track down bugs
- **Collaboration**: Team members can understand your code without extensive explanation

## Core Principles

### 1. Clarity Over Brevity

**❌ Bad Example:**
```python
def calc(a, b, c):
    return (a * b) / c
```

**✅ Good Example:**
```python
def calculate_unit_price(total_cost, quantity, tax_rate):
    return (total_cost * tax_rate) / quantity
```

### 2. Use Meaningful Context

**❌ Bad Example:**
```python
def process(data):
    result = data['value'] * 2
    return result
```

**✅ Good Example:**
```python
def double_employee_salary(employee_record):
    current_salary = employee_record['value']
    doubled_salary = current_salary * 2
    return doubled_salary
```

### 3. Avoid Unnecessary Abbreviations

**❌ Bad Example:**
```python
usr_addr = get_usr_addr(usr_id)
```

**✅ Good Example:**
```python
user_address = get_user_address(user_id)
```

**Exception:** Well-known abbreviations are acceptable:
- `url` (Uniform Resource Locator)
- `api` (Application Programming Interface)
- `http` (Hypertext Transfer Protocol)
- `json` (JavaScript Object Notation)
- `html` (Hypertext Markup Language)

## Naming Conventions by Type

### Functions and Methods

Functions should use **verbs** that describe the action being performed.

#### Common Verb Patterns:

- **Retrieval**: `get`, `fetch`, `retrieve`, `find`, `query`
  ```python
  get_user_profile(user_id)
  fetch_latest_transactions()
  find_products_by_category(category_name)
  ```

- **Validation**: `is`, `has`, `can`, `should`, `validate`, `check`
  ```python
  is_valid_email(email_address)
  has_admin_privileges(user)
  can_access_resource(user, resource)
  validate_password_strength(password)
  ```

- **Transformation**: `convert`, `transform`, `format`, `parse`
  ```python
  convert_celsius_to_fahrenheit(temperature)
  format_phone_number(raw_number)
  parse_json_response(response_text)
  ```

- **Calculation**: `calculate`, `compute`, `sum`, `average`
  ```python
  calculate_total_price(items)
  compute_distance_between_points(point_a, point_b)
  ```

- **Creation**: `create`, `build`, `generate`, `make`
  ```python
  create_new_user_account(user_data)
  generate_unique_identifier()
  ```

- **Update**: `update`, `modify`, `change`, `set`
  ```python
  update_user_email(user_id, new_email)
  set_user_preferences(preferences)
  ```

- **Deletion**: `delete`, `remove`, `clear`
  ```python
  delete_user_account(user_id)
  remove_expired_sessions()
  ```

### Variables

Variables should use **nouns** or **noun phrases** that describe what they contain.

**❌ Bad Examples:**
```python
data = fetch_api()
temp = calculate()
x = get_value()
```

**✅ Good Examples:**
```python
customer_order_data = fetch_api()
calculated_temperature = calculate()
user_age = get_value()
```

### Boolean Variables

Boolean variables should use prefixes that make their true/false nature clear.

**Recommended Prefixes:**
- `is_`: State or condition
- `has_`: Possession or inclusion
- `can_`: Ability or permission
- `should_`: Recommendation or requirement
- `will_`: Future action
- `did_`: Past action

**Examples:**
```python
is_authenticated = check_auth_token(token)
has_premium_subscription = user.subscription_type == 'premium'
can_edit_document = check_permissions(user, document)
should_send_notification = user.preferences.notifications_enabled
will_expire_soon = days_until_expiry < 7
did_complete_onboarding = user.onboarding_completed
```

### Constants

Constants should use UPPERCASE_WITH_UNDERSCORES and descriptive names.

**❌ Bad Example:**
```python
MAX = 100
MIN = 10
```

**✅ Good Example:**
```python
MAXIMUM_LOGIN_ATTEMPTS = 5
MINIMUM_PASSWORD_LENGTH = 8
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"
```

### Loop Variables

Use descriptive loop variables, especially for nested loops or complex iterations.

**❌ Bad Example:**
```python
for i in items:
    for j in i:
        for k in j:
            process(k)
```

**✅ Good Example:**
```python
for order in customer_orders:
    for line_item in order.items:
        for product_variant in line_item.variants:
            process_product_variant(product_variant)
```

**Exception:** Simple numeric loops can use single letters:
```python
for i in range(10):  # Acceptable for simple counting
    print(i)
```

### Class Names

Classes should use PascalCase and be named with nouns that represent entities or concepts.

**Examples:**
```python
class UserProfile:
    pass

class DatabaseConnection:
    pass

class PaymentProcessor:
    pass

class EmailValidator:
    pass
```

## Common Anti-Patterns to Avoid

### 1. Single-Letter Variables (Except in Limited Cases)

**❌ Avoid:**
```python
def calculate(a, b, c):
    x = a + b
    y = x * c
    return y
```

### 2. Generic Names

**❌ Avoid:**
```python
data = fetch_data()
info = get_info()
temp = process_temp()
value = calculate_value()
```

### 3. Redundant Naming

**❌ Avoid:**
```python
user_user_name = user.name  # Redundant 'user'
string_name = "John"  # Type in variable name
```

### 4. Inconsistent Naming

**❌ Avoid:**
```python
getUserProfile()  # camelCase
get_user_address()  # snake_case
GetUserPhone()  # PascalCase
```

Pick one convention and stick with it (Python uses snake_case).

### 5. Overly Long Names

While descriptive names are important, avoid excessive length:

**❌ Too Long:**
```python
def calculate_the_total_price_of_all_items_in_the_shopping_cart_including_tax():
    pass
```

**✅ Balanced:**
```python
def calculate_cart_total_with_tax():
    pass
```

## Language-Specific Conventions

### Python

- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`

### JavaScript

- Functions and variables: `camelCase`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE` or `camelCase`

### Java

- Methods and variables: `camelCase`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### C#

- Methods and classes: `PascalCase`
- Private fields: `_camelCase` (with underscore)
- Local variables and parameters: `camelCase`

## Refactoring Tips

When improving existing code:

1. **Use IDE Refactoring Tools**: Most IDEs have "Rename" features that update all references
2. **Refactor Incrementally**: Don't change everything at once
3. **Update Tests**: Ensure tests still pass after renaming
4. **Update Documentation**: Update any documentation that references old names
5. **Review with Team**: Get feedback on proposed names before committing

## Quick Checklist

Before finalizing a variable or function name, ask yourself:

- [ ] Does the name clearly describe what it contains or does?
- [ ] Could someone unfamiliar with the code understand this name?
- [ ] Have I avoided unnecessary abbreviations?
- [ ] Is the name consistent with the project's naming conventions?
- [ ] Is the name neither too short nor too long?
- [ ] For booleans, does the name clearly indicate a yes/no answer?
- [ ] For functions, does the name start with a verb?
- [ ] For variables, does the name use a descriptive noun?

## Additional Resources

- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Google Style Guides](https://google.github.io/styleguide/)

## Conclusion

Good naming is one of the most important aspects of writing clean, maintainable code. While it may take extra time initially, descriptive names pay dividends in reduced debugging time, easier maintenance, and better collaboration. Remember: code is written once but read many times—make it count!
