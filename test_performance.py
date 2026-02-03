"""
Performance tests for data processor.
"""

import time
import random
from data_processor import DataProcessor


def measure_time(func, *args):
    """Measure execution time of a function."""
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def test_find_duplicates():
    """Test find duplicates performance."""
    processor = DataProcessor()
    numbers = [random.randint(1, 100) for _ in range(1000)]
    result, elapsed = measure_time(processor.find_duplicates, numbers)
    print(f"find_duplicates: {elapsed:.4f}s")
    return elapsed


def test_calculate_sum():
    """Test sum calculation performance."""
    processor = DataProcessor()
    numbers = list(range(10000))
    result, elapsed = measure_time(processor.calculate_sum, numbers)
    print(f"calculate_sum: {elapsed:.4f}s")
    return elapsed


def test_filter_even_numbers():
    """Test filtering performance."""
    processor = DataProcessor()
    numbers = list(range(10000))
    result, elapsed = measure_time(processor.filter_even_numbers, numbers)
    print(f"filter_even_numbers: {elapsed:.4f}s")
    return elapsed


def test_string_concatenation():
    """Test string concatenation performance."""
    processor = DataProcessor()
    strings = [f"item_{i}" for i in range(1000)]
    result, elapsed = measure_time(processor.process_string_list, strings)
    print(f"process_string_list: {elapsed:.4f}s")
    return elapsed


def test_search_in_list():
    """Test search performance."""
    processor = DataProcessor()
    items = list(range(10000))
    result, elapsed = measure_time(processor.search_in_list, items, 9999)
    print(f"search_in_list: {elapsed:.4f}s")
    return elapsed


def test_count_word_frequency():
    """Test word frequency counting."""
    processor = DataProcessor()
    words = ["word" + str(i % 100) for i in range(1000)]
    text = " ".join(words)
    result, elapsed = measure_time(processor.count_word_frequency, text)
    print(f"count_word_frequency: {elapsed:.4f}s")
    return elapsed


def test_remove_duplicates():
    """Test duplicate removal."""
    processor = DataProcessor()
    items = [random.randint(1, 100) for _ in range(1000)]
    result, elapsed = measure_time(processor.remove_duplicates_from_list, items)
    print(f"remove_duplicates_from_list: {elapsed:.4f}s")
    return elapsed


def test_sort_by_length():
    """Test sorting performance."""
    processor = DataProcessor()
    strings = [f"string_{'x' * random.randint(1, 20)}" for _ in range(100)]
    result, elapsed = measure_time(processor.sort_by_length, strings)
    print(f"sort_by_length: {elapsed:.4f}s")
    return elapsed


def run_all_tests():
    """Run all performance tests."""
    print("Running performance tests...\n")
    
    tests = [
        test_find_duplicates,
        test_calculate_sum,
        test_filter_even_numbers,
        test_string_concatenation,
        test_search_in_list,
        test_count_word_frequency,
        test_remove_duplicates,
        test_sort_by_length,
    ]
    
    total_time = 0
    for test in tests:
        elapsed = test()
        total_time += elapsed
    
    print(f"\nTotal time: {total_time:.4f}s")


if __name__ == "__main__":
    run_all_tests()
