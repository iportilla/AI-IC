## Calculate Fibonacci Sequence

This script calculates the Fibonacci sequence up to a specified number of terms.

**fibonacci(n)** function:

The `fibonacci(n)` function takes an integer `n` as input and returns a list containing the first `n` Fibonacci numbers.

*   If `n` is negative, it returns an empty list (0).
*   If `n` is 0 or 1, it returns a list containing only 0 or 1 respectively.
*   For `n` greater than 1, it iteratively calculates the Fibonacci numbers using the following formula:
    *   F(0) = 0
    *   F(1) = 1
    *   F(n) = F(n-1) + F(n-2)

**Example Usage:**
