def example_function(numbers):
    result = []
    for num in numbers:
        # Perform some operation on each number
        modified_num = num * 2 - 3
        
        # Append the result to the list
        result.append(modified_num)
        
        # Print the result for each number
        print(f"Result for {num}: {modified_num}")
    
    return result

# Example usage with 5 numbers
numbers = [1, 2, 3, 4, 5]
example_function(numbers)