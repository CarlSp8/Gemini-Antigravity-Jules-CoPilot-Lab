"""
Data processing module with various performance issues.
This module demonstrates common performance anti-patterns.
"""

import time
import random


class DataProcessor:
    """Process data with various inefficient operations."""
    
    def __init__(self):
        self.data = []
        self.cache = {}
    
    def find_duplicates(self, numbers):
        """Find duplicate numbers in a list - INEFFICIENT: O(n^2) nested loops."""
        duplicates = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j and numbers[i] == numbers[j]:
                    if numbers[i] not in duplicates:
                        duplicates.append(numbers[i])
        return duplicates
    
    def calculate_sum(self, numbers):
        """Calculate sum of numbers - INEFFICIENT: Using loop instead of built-in."""
        total = 0
        for num in numbers:
            total = total + num
        return total
    
    def filter_even_numbers(self, numbers):
        """Filter even numbers - INEFFICIENT: Creating new list with append."""
        result = []
        for num in numbers:
            if num % 2 == 0:
                result.append(num)
        return result
    
    def process_string_list(self, strings):
        """Process strings - INEFFICIENT: String concatenation in loop."""
        result = ""
        for s in strings:
            result = result + s + ","
        return result.rstrip(",")
    
    def search_in_list(self, items, target):
        """Search for item in list - INEFFICIENT: Linear search in unsorted list."""
        for i in range(len(items)):
            if items[i] == target:
                return i
        return -1
    
    def calculate_factorial(self, n):
        """Calculate factorial - INEFFICIENT: Recursive without memoization."""
        if n <= 1:
            return 1
        return n * self.calculate_factorial(n - 1)
    
    def count_word_frequency(self, text):
        """Count word frequency - INEFFICIENT: Nested loops instead of dict."""
        words = text.lower().split()
        frequency = []
        
        for word in words:
            found = False
            for item in frequency:
                if item[0] == word:
                    item[1] += 1
                    found = True
                    break
            if not found:
                frequency.append([word, 1])
        
        return frequency
    
    def remove_duplicates_from_list(self, items):
        """Remove duplicates - INEFFICIENT: Checking membership in list repeatedly."""
        result = []
        for item in items:
            if item not in result:
                result.append(item)
        return result
    
    def find_common_elements(self, list1, list2):
        """Find common elements - INEFFICIENT: Nested loops."""
        common = []
        for item1 in list1:
            for item2 in list2:
                if item1 == item2 and item1 not in common:
                    common.append(item1)
        return common
    
    def sort_by_length(self, strings):
        """Sort strings by length - INEFFICIENT: Bubble sort."""
        arr = strings.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if len(arr[j]) > len(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def read_and_process_file(self, filename):
        """Read file - INEFFICIENT: Reading entire file into memory at once."""
        try:
            with open(filename, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                processed = []
                for line in lines:
                    processed.append(line.strip().upper())
                return processed
        except FileNotFoundError:
            return []
    
    def calculate_fibonacci(self, n):
        """Calculate Fibonacci - INEFFICIENT: Naive recursion."""
        if n <= 1:
            return n
        return self.calculate_fibonacci(n - 1) + self.calculate_fibonacci(n - 2)
    
    def matrix_multiply(self, matrix1, matrix2):
        """Multiply matrices - INEFFICIENT: Naive implementation without optimization."""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        cols2 = len(matrix2[0])
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    sum_val = sum_val + matrix1[i][k] * matrix2[k][j]
                row.append(sum_val)
            result.append(row)
        
        return result


def main():
    """Demonstrate the inefficient operations."""
    processor = DataProcessor()
    
    # Test with sample data
    numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 3]
    print("Finding duplicates...")
    duplicates = processor.find_duplicates(numbers)
    print(f"Duplicates: {duplicates}")
    
    print("\nCalculating sum...")
    total = processor.calculate_sum(numbers)
    print(f"Sum: {total}")
    
    print("\nFiltering even numbers...")
    evens = processor.filter_even_numbers(numbers)
    print(f"Even numbers: {evens}")
    
    strings = ["hello", "world", "python", "performance"]
    print("\nProcessing strings...")
    result = processor.process_string_list(strings)
    print(f"Result: {result}")
    
    print("\nCounting word frequency...")
    text = "the quick brown fox jumps over the lazy dog the fox"
    frequency = processor.count_word_frequency(text)
    print(f"Word frequency: {frequency}")
    
    print("\nRemoving duplicates...")
    items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    unique = processor.remove_duplicates_from_list(items)
    print(f"Unique items: {unique}")
    
    print("\nSorting by length...")
    sorted_strings = processor.sort_by_length(strings)
    print(f"Sorted: {sorted_strings}")
    
    print("\nCalculating Fibonacci(10)...")
    fib = processor.calculate_fibonacci(10)
    print(f"Fibonacci: {fib}")


if __name__ == "__main__":
    main()
