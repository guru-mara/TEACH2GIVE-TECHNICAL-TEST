'''Question 6: Count Vowels 
Write a program that counts the number of vowels in a sentence. 
eg " Hello World " => returns 2'''
def count_unique_vowels(sentence):
    # Define the vowels
    vowels = set("aeiouAEIOU")
    # Convert the sentence to a set of unique characters
    unique_chars = set(sentence)
    # Count and return the number of unique vowels in the sentence
    return len(vowels.intersection(unique_chars))

# Example usage
print(count_unique_vowels("Hello World"))  # Output: 2
