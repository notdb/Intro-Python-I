# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even_the_classic(n):
        if n % 2 == 0:
            print('even')
        else:
            print('odd')

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
is_even_the_classic(num)
