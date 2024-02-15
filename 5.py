'''Question 5: Reverse Integer 
Write a program that takes an integer as input and returns an integer with reversed digit 
ordering. 
Examples: 
For input 500, the program should return 5. 
For input -56, the program should return -65. 
For input -90, the program should return -9. 
For input 91, the program should return 19. '''
def reverse_integer(x):
    # Check if the number is negative
    is_negative = x < 0
    
    # Convert the integer to string and remove the negative sign if necessary
    x_str = str(abs(x))
    
    # Reverse the string
    reversed_str = x_str[::-1]
    
    # Convert the reversed string back to integer
    reversed_int = int(reversed_str)
    
    # If the original number was negative, return the negative of the reversed integer
    if is_negative:
        return -reversed_int
    else:
        return reversed_int

# Example usage
print(reverse_integer(500))  # Output: 5
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))   # Output: 19