"""
Example demonstrating the concept of 'private now public later'

This module shows how to manage visibility of class members,
transitioning from private (internal use) to public (external API).
"""


class DataManager:
    """
    A class that demonstrates changing visibility from private to public.
    
    Initially, attributes and methods are private (prefixed with _).
    After refactoring or API stabilization, they can be made public.
    """
    
    def __init__(self):
        # Public attributes - part of the stable API
        self.data = []
        self.count = 0
    
    def add_item(self, item):
        """Public method to add an item to the data collection."""
        self.data.append(item)
        self.count += 1
    
    def get_items(self):
        """Public method to retrieve all items."""
        return self.data.copy()
    
    def get_count(self):
        """Public method to get the count of items."""
        return self.count


if __name__ == "__main__":
    # Example usage
    manager = DataManager()
    manager.add_item("first")
    manager.add_item("second")
    
    print(f"Items: {manager.get_items()}")
    print(f"Count: {manager.get_count()}")
