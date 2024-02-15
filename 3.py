'''question 3: Power of Two 
Write a program that takes an integer as input and returns true if the input is a power of two. 
Examples:  
8=> returns true 
6=> returns false'''
def is_power_of_two(n):
    # Method 1: Continuous division by 2 for even numbers
    if n<= 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1
# Test cases
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False