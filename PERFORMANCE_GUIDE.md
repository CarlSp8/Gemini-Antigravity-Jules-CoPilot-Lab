# Performance Optimization Guide

This repository demonstrates common performance anti-patterns and their optimized solutions.

## Overview

This project contains:
- `data_processor.py` - Original code with intentional performance issues
- `optimized_data_processor.py` - Optimized version with best practices
- `compare_performance.py` - Performance comparison tool
- `test_performance.py` - Performance benchmarking suite

## Performance Improvements Summary

### Overall Results
- **Total Speedup: 57.29x faster**
- **Overall Improvement: 98.3% reduction in execution time**

## Detailed Optimizations

### 1. Find Duplicates (~1000x faster)
**Problem:** O(n²) nested loops checking every element against every other element
```python
# SLOW - O(n²)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            duplicates.append(numbers[i])
```

**Solution:** O(n) using set for tracking seen elements
```python
# FAST - O(n)
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
```

### 2. String Concatenation (~120x faster)
**Problem:** O(n²) string concatenation in loop creates new string each iteration
```python
# SLOW - O(n²)
result = ""
for s in strings:
    result = result + s + ","
```

**Solution:** O(n) using join() which builds the string once
```python
# FAST - O(n)
return ",".join(strings)
```

### 3. Sorting (~210x faster)
**Problem:** O(n²) bubble sort algorithm
```python
# SLOW - O(n²)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(arr[j]) > len(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

**Solution:** O(n log n) built-in Timsort
```python
# FAST - O(n log n)
return sorted(strings, key=len)
```

### 4. Finding Common Elements (~270x faster)
**Problem:** O(n*m) nested loops
```python
# SLOW - O(n*m)
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common.append(item1)
```

**Solution:** O(n+m) using set intersection
```python
# FAST - O(n+m)
return list(set(list1) & set(list2))
```

### 5. Fibonacci Calculation (~11,500x faster!)
**Problem:** Exponential time complexity O(2ⁿ) with naive recursion
```python
# SLOW - O(2ⁿ)
def calculate_fibonacci(self, n):
    if n <= 1:
        return n
    return self.calculate_fibonacci(n - 1) + self.calculate_fibonacci(n - 2)
```

**Solution:** Linear time O(n) with manual memoization or iterative approach
```python
# FAST - O(n) with manual memoization
def calculate_fibonacci(self, n):
    if n not in self.cache:
        if n <= 1:
            self.cache[n] = n
        else:
            self.cache[n] = self.calculate_fibonacci(n - 1) + self.calculate_fibonacci(n - 2)
    return self.cache[n]

# FASTEST - O(n) time, O(1) space
def calculate_fibonacci_iterative(self, n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 6. Word Frequency Counting (~12x faster)
**Problem:** O(n²) nested loops through list
```python
# SLOW - O(n²)
for word in words:
    for item in frequency:
        if item[0] == word:
            item[1] += 1
```

**Solution:** O(n) using dictionary
```python
# FAST - O(n)
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
```

### 7. Remove Duplicates (~15x faster)
**Problem:** O(n²) checking membership in growing list
```python
# SLOW - O(n²)
result = []
for item in items:
    if item not in result:  # O(n) check each time
        result.append(item)
```

**Solution:** O(n) using dict.fromkeys() to maintain order
```python
# FAST - O(n)
return list(dict.fromkeys(items))
```

### 8. Calculate Sum (~3x faster)
**Problem:** Manual loop accumulation
```python
# SLOW
total = 0
for num in numbers:
    total = total + num
```

**Solution:** Built-in optimized function
```python
# FAST
return sum(numbers)
```

### 9. Filter Even Numbers (1.1x faster)
**Problem:** Manual append in loop
```python
# SLOW
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
```

**Solution:** List comprehension
```python
# FAST
return [num for num in numbers if num % 2 == 0]
```

## Key Performance Principles

### 1. **Use Appropriate Data Structures**
- Sets for membership testing (O(1) vs O(n))
- Dictionaries for counting/mapping (O(1) vs O(n))
- Deques for queue operations

### 2. **Avoid Nested Loops When Possible**
- Use set operations for intersections/unions
- Use dictionaries for lookups
- Consider sorting + two-pointer technique

### 3. **Use Built-in Functions**
- They're implemented in C and highly optimized
- Examples: `sum()`, `sorted()`, `min()`, `max()`

### 4. **String Concatenation**
- Use `str.join()` instead of `+` in loops
- Use list and join for building strings

### 5. **List Comprehensions**
- Faster than manual append loops
- More readable and Pythonic

### 6. **Avoid Redundant Calculations**
- Cache/memoize expensive computations
- Move invariant calculations outside loops

### 7. **Choose Right Algorithm Complexity**
- Understand Big O notation
- Choose algorithms with better time complexity
- Sometimes sacrifice space for time

### 8. **Memory Efficiency**
- Process data in streams when possible
- Don't load entire files into memory unnecessarily
- Use generators for large datasets

## Running the Tests

### Run baseline performance tests:
```bash
python3 test_performance.py
```

### Run performance comparison:
```bash
python3 compare_performance.py
```

### Test individual implementations:
```bash
python3 data_processor.py          # Original
python3 optimized_data_processor.py  # Optimized
```

## Lessons Learned

1. **Profile Before Optimizing**: Always measure to find actual bottlenecks
2. **Algorithm Choice Matters**: Often more important than micro-optimizations
3. **Use the Standard Library**: Python's built-ins are highly optimized
4. **Consider Time vs Space Trade-offs**: Sometimes using more memory speeds things up
5. **Test for Correctness**: Optimizations should maintain correct behavior

## Further Optimizations

For even better performance in production:
- Use NumPy for numerical operations
- Use multiprocessing for CPU-bound tasks
- Use async/await for I/O-bound tasks
- Profile with `cProfile` or `line_profiler`
- Consider Cython or PyPy for critical paths

## References

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [Time Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
