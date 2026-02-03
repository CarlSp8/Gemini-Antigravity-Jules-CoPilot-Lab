<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>Built with AI Studio</h2>

  <p>The fastest path from prompt to production with Gemini.</p>

  <a href="https://aistudio.google.com/apps">Start building</a>

</div>

---

## Performance Optimization Demo

This repository demonstrates identifying and fixing common performance issues in Python code.

### 🚀 Key Results
- **57.29x overall speedup** achieved through algorithmic improvements
- **98.3% reduction** in execution time
- Fibonacci calculation: **11,598x faster** with memoization
- String concatenation: **122x faster** using join()
- Finding duplicates: **959x faster** using sets

### 📁 Project Structure
- `data_processor.py` - Original code with performance anti-patterns
- `optimized_data_processor.py` - Optimized implementation
- `compare_performance.py` - Performance benchmarking tool
- `PERFORMANCE_GUIDE.md` - Detailed optimization guide

### 🏃 Quick Start
```bash
# Run performance comparison
python3 compare_performance.py

# Run individual implementations
python3 data_processor.py          # Original
python3 optimized_data_processor.py  # Optimized
```

### 📚 Learn More
See [PERFORMANCE_GUIDE.md](PERFORMANCE_GUIDE.md) for detailed explanations of each optimization.

### 🎯 Key Techniques Demonstrated
1. Algorithm complexity improvement (O(n²) → O(n))
2. Proper data structure selection (lists → sets/dicts)
3. Built-in function usage over manual loops
4. Memoization for recursive functions
5. String operation optimization
6. List comprehensions vs manual loops

---
