# Initialize step counters for both recursive and iterative methods
recursive_steps = 0
iterative_steps = 0

# Recursive Fibonacci function with step count
def fibonacci_recursive(n):
    global recursive_steps
    recursive_steps += 1  # Increment step counter for each function call
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci function with step count
def fibonacci_iterative(n):
    global iterative_steps
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        iterative_steps += 1  # Increment step counter for each loop iteration
        a, b = b, a + b
    return b

# Main function to test both methods
if __name__ == "__main__":
    n = 10  # You can change this to any Fibonacci position

    # Calculate Fibonacci recursively
    recursive_steps = 0
    result_recursive = fibonacci_recursive(n)
    print("Recursive Fibonacci({}): {}".format(n, result_recursive))
    print("Recursive steps:", recursive_steps)

    # Calculate Fibonacci iteratively
    iterative_steps = 0
    result_iterative = fibonacci_iterative(n)
    print("Iterative Fibonacci({}): {}".format(n, result_iterative))
    print("Iterative steps:", iterative_steps)
