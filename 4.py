'''Question 4: Capitalize Words 
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string. 
Examples:  
"hi"=> returns "Hi" 
"i love programming"=> returns "I Love Programming"'''
def capitalize_words(input_string):
    # Split the string into words
    words = input_string.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a single string
    result_string = ' '.join(capitalized_words)

    return result_string

# Example
print(capitalize_words("hi"))  # Output: "Hi"
print(capitalize_words("i love programming"))  # Output: "I Love Programming"

