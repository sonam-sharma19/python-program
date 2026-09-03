
def print_fibonacci_loop(n):
    """Prints the first n terms of the Fibonacci sequence."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
        
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage: Print the first 10 terms
print_fibonacci_loop(10)