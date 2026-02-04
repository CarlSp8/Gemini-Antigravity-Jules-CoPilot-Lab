# Variable and Function Naming Guide

This guide provides best practices for choosing descriptive variable and function names that improve code readability and maintainability.

## Table of Contents

1. [Why Naming Matters](#why-naming-matters)
2. [General Principles](#general-principles)
3. [Variable Naming](#variable-naming)
4. [Function Naming](#function-naming)
5. [Common Pitfalls](#common-pitfalls)
6. [Language-Specific Conventions](#language-specific-conventions)

---

## Why Naming Matters

Good names make code:
- **Self-documenting**: Reduces need for comments
- **Maintainable**: Easier for others (and future you) to understand
- **Debuggable**: Clearer what each variable represents
- **Professional**: Shows attention to detail and code quality

---

## General Principles

### 1. Be Descriptive and Specific

❌ **Bad**: `data`, `info`, `temp`, `result`
✅ **Good**: `userProfile`, `customerEmail`, `sortedProducts`, `validationResult`

### 2. Use Full Words Over Abbreviations

❌ **Bad**: `usrNm`, `addr`, `qty`, `msg`
✅ **Good**: `username`, `address`, `quantity`, `message`

**Exception**: Common abbreviations are acceptable: `id`, `url`, `api`, `html`, `max`, `min`

### 3. Avoid Single Letters (Except in Specific Cases)

❌ **Bad**: `a`, `b`, `x`, `y`, `t`
✅ **Good**: `age`, `balance`, `width`, `height`, `timestamp`

**Acceptable single letters**:
- Loop counters in simple loops: `i`, `j`, `k`
- Coordinates in mathematical contexts: `x`, `y`, `z`
- Generic type parameters: `T`, `U`, `V`

### 4. Make Boolean Names Obvious

Use prefixes that indicate yes/no states:
- `is`: `isActive`, `isValid`, `isLoggedIn`
- `has`: `hasPermission`, `hasChildren`, `hasError`
- `can`: `canEdit`, `canDelete`, `canAccess`
- `should`: `shouldUpdate`, `shouldNotify`, `shouldRetry`

### 5. Include Units in Names When Relevant

❌ **Bad**: `timeout`, `delay`, `duration`
✅ **Good**: `timeoutInSeconds`, `delayMs`, `durationInMinutes`

---

## Variable Naming

### Constants

Use UPPER_CASE_WITH_UNDERSCORES for constants:

```python
# Python
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"
```

```javascript
// JavaScript
const MAX_LOGIN_ATTEMPTS = 3;
const DEFAULT_TIMEOUT_MS = 30000;
const API_BASE_URL = "https://api.example.com";
```

### Collections (Arrays, Lists, Sets)

Use plural nouns for collections:

❌ **Bad**: `user`, `product`, `item`
✅ **Good**: `users`, `products`, `items`

```python
active_users = [user for user in all_users if user.is_active]
product_ids = [product.id for product in products]
```

### Dictionaries/Objects

Name based on what they represent:

❌ **Bad**: `obj`, `dict`, `map`
✅ **Good**: `userSettings`, `productPrices`, `configOptions`

```javascript
const userPreferences = {
    theme: "dark",
    language: "en",
    notificationsEnabled: true
};
```

### Loop Variables

Use descriptive names, not just `i`:

❌ **Bad**:
```python
for i in users:
    print(i.name)
```

✅ **Good**:
```python
for user in users:
    print(user.name)
```

For nested loops, use meaningful names:

```python
for order in customer_orders:
    for item in order.items:
        process_order_item(item)
```

---

## Function Naming

### Use Verbs or Verb Phrases

Functions perform actions, so start with verbs:

❌ **Bad**: `user()`, `email()`, `validation()`
✅ **Good**: `getUser()`, `sendEmail()`, `validateInput()`

### Common Verb Conventions

- **get/fetch**: Retrieve data
  - `getUserById()`, `fetchLatestPosts()`
  
- **set/update**: Modify data
  - `setUsername()`, `updateUserProfile()`
  
- **create/make**: Instantiate new objects
  - `createNewUser()`, `makePayment()`
  
- **delete/remove**: Eliminate data
  - `deleteAccount()`, `removeItem()`
  
- **is/has/can**: Return boolean
  - `isValidEmail()`, `hasPermission()`, `canEditPost()`
  
- **calculate/compute**: Perform calculations
  - `calculateTotal()`, `computeDistance()`
  
- **validate/verify**: Check validity
  - `validatePassword()`, `verifyEmail()`
  
- **find/search**: Locate data
  - `findUserByEmail()`, `searchProducts()`
  
- **parse/format**: Transform data
  - `parseJSON()`, `formatCurrency()`

### Be Specific About What Functions Do

❌ **Bad**: `process()`, `handle()`, `manage()`
✅ **Good**: `processPayment()`, `handleUserLogin()`, `manageInventory()`

### Function Name Length

Balance between descriptiveness and readability:

❌ **Too vague**: `get()`
❌ **Too long**: `getTheUserInformationFromTheDatabaseByTheirUniqueIdentifier()`
✅ **Just right**: `getUserById()`

---

## Common Pitfalls

### 1. Generic Names

Avoid: `data`, `info`, `value`, `item`, `element`, `object`, `array`, `list`, `result`, `temp`

These don't convey meaning. Be specific about what the data represents.

### 2. Misleading Names

❌ **Bad**: Function named `getUserId()` that returns entire user object
✅ **Good**: `getUser()` returns user object, `getUserId()` returns ID only

### 3. Inconsistent Naming

Pick a convention and stick with it:
- `getUser()` and `fetchProduct()` ❌ (inconsistent verbs)
- `getUser()` and `getProduct()` ✅ (consistent)

### 4. Redundant Context

If in a `UserService` class, don't prefix everything with `user`:

❌ **Bad**:
```python
class UserService:
    def get_user_by_id(self, user_id):
        pass
    def update_user_profile(self, user_id, user_data):
        pass
```

✅ **Good**:
```python
class UserService:
    def get_by_id(self, user_id):
        pass
    def update_profile(self, user_id, profile_data):
        pass
```

### 5. Magic Numbers

Don't use unexplained numbers in code:

❌ **Bad**:
```python
if user.age > 18:
    allow_access()
```

✅ **Good**:
```python
MINIMUM_AGE_FOR_ACCESS = 18
if user.age > MINIMUM_AGE_FOR_ACCESS:
    allow_access()
```

---

## Language-Specific Conventions

### Python

- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: prefix with `_` (e.g., `_internal_method`)

```python
MAX_RETRIES = 3

class UserAccount:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def calculate_total_balance(self):
        return self._get_balance()
    
    def _get_balance(self):
        pass
```

### JavaScript/TypeScript

- **Variables/Functions**: `camelCase`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: prefix with `#` or `_`

```javascript
const MAX_RETRY_ATTEMPTS = 3;

class UserAccount {
    constructor(userId) {
        this.userId = userId;
    }
    
    calculateTotalBalance() {
        return this.#getBalance();
    }
    
    #getBalance() {
        // private method
    }
}
```

### General Guidelines

1. **Consistency**: Follow your team's or project's style guide
2. **Readability**: Optimize for reading, not writing
3. **Intent**: Names should reveal intent
4. **Context**: Consider the scope and context
5. **Length**: Longer for broader scope, shorter for narrow scope

---

## Quick Checklist

Before committing code, check your names:

- [ ] Can someone understand what this variable holds without looking at its value?
- [ ] Does this function name clearly describe what it does?
- [ ] Are boolean variables prefixed with is/has/can/should?
- [ ] Are collections named with plural nouns?
- [ ] Are units included in time/measurement variables?
- [ ] Are constants in UPPER_CASE?
- [ ] Have I avoided single letters (except loop counters)?
- [ ] Are abbreviations avoided or commonly understood?
- [ ] Is the naming consistent with the rest of the codebase?

---

## Resources

- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [PEP 8 – Style Guide for Python Code](https://pep8.org/)
- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

---

## Examples

See the included example files:
- `naming_examples.py` - Python examples of good vs. bad naming
- `naming_examples.js` - JavaScript examples of good vs. bad naming
- `shopping_cart_example.py` - Real-world example with improved naming

---

**Remember**: Good naming is a sign of professional code. Take the time to choose names that make your code readable and maintainable!
