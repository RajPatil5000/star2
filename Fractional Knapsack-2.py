# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate maximum value with fractional knapsack approach
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    total_value = 0  # Total value of knapsack
    
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            # Take the whole item if it fits in remaining capacity
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item that fits
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is full

        if capacity == 0:
            break

    return total_value

# Example usage
if __name__ == "__main__":
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50
    max_value = fractional_knapsack(items, capacity)
    print("Maximum value in Knapsack =", max_value)
