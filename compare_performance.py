"""
Performance comparison between original and optimized implementations.
"""

import time
import random
from data_processor import DataProcessor
from optimized_data_processor import OptimizedDataProcessor


def measure_time(func, *args):
    """Measure execution time of a function."""
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def compare_find_duplicates():
    """Compare find duplicates performance."""
    numbers = [random.randint(1, 100) for _ in range(1000)]
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.find_duplicates, numbers)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.find_duplicates, numbers)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"find_duplicates:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_calculate_sum():
    """Compare sum calculation performance."""
    numbers = list(range(100000))
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.calculate_sum, numbers)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.calculate_sum, numbers)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"calculate_sum:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_filter_even_numbers():
    """Compare filtering performance."""
    numbers = list(range(100000))
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.filter_even_numbers, numbers)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.filter_even_numbers, numbers)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"filter_even_numbers:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_string_concatenation():
    """Compare string concatenation performance."""
    strings = [f"item_{i}" for i in range(5000)]
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.process_string_list, strings)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.process_string_list, strings)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"process_string_list:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_count_word_frequency():
    """Compare word frequency counting."""
    words = ["word" + str(i % 100) for i in range(2000)]
    text = " ".join(words)
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.count_word_frequency, text)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.count_word_frequency, text)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"count_word_frequency:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_remove_duplicates():
    """Compare duplicate removal."""
    items = [random.randint(1, 100) for _ in range(2000)]
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.remove_duplicates_from_list, items)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.remove_duplicates_from_list, items)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"remove_duplicates_from_list:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_sort_by_length():
    """Compare sorting performance."""
    strings = [f"string_{'x' * random.randint(1, 20)}" for _ in range(500)]
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.sort_by_length, strings)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.sort_by_length, strings)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"sort_by_length:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_fibonacci():
    """Compare Fibonacci calculation."""
    n = 30
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.calculate_fibonacci, n)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.calculate_fibonacci, n)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"calculate_fibonacci({n}):")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def compare_find_common_elements():
    """Compare finding common elements."""
    list1 = [random.randint(1, 500) for _ in range(1000)]
    list2 = [random.randint(1, 500) for _ in range(1000)]
    
    processor = DataProcessor()
    _, time_orig = measure_time(processor.find_common_elements, list1, list2)
    
    opt_processor = OptimizedDataProcessor()
    _, time_opt = measure_time(opt_processor.find_common_elements, list1, list2)
    
    improvement = ((time_orig - time_opt) / time_orig * 100) if time_orig > 0 else 0
    print(f"find_common_elements:")
    print(f"  Original:  {time_orig:.6f}s")
    print(f"  Optimized: {time_opt:.6f}s")
    print(f"  Speedup:   {time_orig/time_opt:.2f}x ({improvement:.1f}% faster)\n")
    return time_orig, time_opt


def run_all_comparisons():
    """Run all performance comparisons."""
    print("=" * 70)
    print("PERFORMANCE COMPARISON: Original vs Optimized Implementation")
    print("=" * 70)
    print()
    
    comparisons = [
        compare_find_duplicates,
        compare_calculate_sum,
        compare_filter_even_numbers,
        compare_string_concatenation,
        compare_count_word_frequency,
        compare_remove_duplicates,
        compare_sort_by_length,
        compare_find_common_elements,
        compare_fibonacci,
    ]
    
    total_orig = 0
    total_opt = 0
    
    for comparison in comparisons:
        time_orig, time_opt = comparison()
        total_orig += time_orig
        total_opt += time_opt
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Original Time:  {total_orig:.6f}s")
    print(f"Total Optimized Time: {total_opt:.6f}s")
    overall_speedup = total_orig / total_opt if total_opt > 0 else 0
    overall_improvement = ((total_orig - total_opt) / total_orig * 100) if total_orig > 0 else 0
    print(f"Overall Speedup:      {overall_speedup:.2f}x ({overall_improvement:.1f}% faster)")
    print("=" * 70)


if __name__ == "__main__":
    run_all_comparisons()
