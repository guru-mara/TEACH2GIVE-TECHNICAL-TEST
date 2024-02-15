'''Question 2: Fibonacci Sequence 
Write a program to generate the Fibonacci sequence up to 100.'''  
a, b = 0, 1  # Starting values for the sequence
while a <= 100:
    print(a, end=' ')
    a, b = b, a + b  # Update the values for the next iteration
