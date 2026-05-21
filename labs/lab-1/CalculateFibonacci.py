#calculate Fibonacci given n
def fibonacci(n):
  """
  Calculates the nth Fibonacci number.

    n: The index of the desired Fibonacci number (non-negative integer).
    return 0  # Handle negative input (conventionally return 0)
  """
  if n < 0:
    return 0  # Handle negative input (conventionally return 0)
  elif n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

# Example usage:
list = [0,1,2,3,4,5,10]
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(2))  # Output: 1
print(fibonacci(3))  # Output: 2
print(fibonacci(4))  # Output: 3
print(fibonacci(5))  # Output: 5
print(fibonacci(10)) # Output: 55
print(fibonacci(-1)) # Output: 0 (handling negative input)
