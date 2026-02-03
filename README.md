<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>Code Duplication Refactoring Demo</h1>

  <p>Demonstrating best practices for identifying and eliminating code duplication.</p>

  <a href="https://aistudio.google.com/apps">Built with AI Studio</a>

</div>

## Overview

This repository demonstrates common code duplication patterns and how to refactor them using software engineering best practices.

## What's Included

- **data_processor.py** - Refactored code showing DRY principles and design patterns
- **test_data_processor.py** - Comprehensive test suite (21 tests, 100% passing)
- **REFACTORING_NOTES.md** - Detailed explanation of refactoring process
- **BEFORE_AFTER_COMPARISON.md** - Side-by-side comparison with metrics

## Key Improvements

✅ **100% Duplication Eliminated** - Removed ~120 lines of duplicated code  
✅ **Better Design** - Template Method and Strategy patterns applied  
✅ **Data-Driven** - Configuration separated from logic  
✅ **Highly Testable** - Modular, focused functions  
✅ **Easy to Extend** - Add new features with minimal code  

## Running Tests

```bash
python -m unittest test_data_processor.py -v
```

All 21 tests pass, confirming the refactoring maintains functionality.

## Patterns Demonstrated

1. **Extract Method** - Common code blocks → reusable functions
2. **Replace Conditional with Dictionary** - If-elif chains → dictionary lookups
3. **Template Method Pattern** - Common structure with customizable steps
4. **Strategy Pattern** - Pluggable algorithms
5. **DRY Principle** - Don't Repeat Yourself

## Learn More

See [REFACTORING_NOTES.md](REFACTORING_NOTES.md) for detailed documentation and [BEFORE_AFTER_COMPARISON.md](BEFORE_AFTER_COMPARISON.md) for side-by-side examples.
