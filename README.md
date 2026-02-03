<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>Built with AI Studio</h2>

  <p>The fastest path from prompt to production with Gemini.</p>

  <a href="https://aistudio.google.com/apps">Start building</a>

</div>

## Descriptive Variable and Function Naming

This repository demonstrates best practices for creating clear, descriptive variable and function names that make code more readable and maintainable.

### 📚 Resources

- **[NAMING_GUIDE.md](NAMING_GUIDE.md)** - Comprehensive guide on naming conventions and best practices
- **[naming_examples.py](naming_examples.py)** - Side-by-side examples comparing poor vs. good naming practices

### 🎯 Key Principles

1. **Be Specific**: Use names that clearly describe what the variable contains or what the function does
2. **Avoid Abbreviations**: Write full words unless the abbreviation is universally understood
3. **Use Verbs for Functions**: Functions should start with action words (calculate, fetch, validate)
4. **Use Nouns for Variables**: Variables should describe the data they contain
5. **Boolean Naming**: Use prefixes like `is_`, `has_`, `can_` for clarity

### 💡 Quick Example

```python
# ❌ Bad: Non-descriptive names
def proc(d):
    x = d.get('n')
    return x * 2

# ✅ Good: Descriptive names
def calculate_doubled_salary(employee_record):
    current_salary = employee_record.get('salary')
    doubled_salary = current_salary * 2
    return doubled_salary
```

### 🚀 Getting Started

Check out the [naming_examples.py](naming_examples.py) file to see 10 detailed examples of good naming practices, or read the full [NAMING_GUIDE.md](NAMING_GUIDE.md) for comprehensive guidelines.
