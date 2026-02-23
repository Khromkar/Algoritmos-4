# What is Recursion?
"""
    Recursion is a method that calls itself. Is usually a method that maybe returns a value but
    its conditioned on some parameter such that when you hit some conditional at some point in time
    you can stop recursing.

    We consider this point the "base case"
"""

def recursion(someValue):
    if someValue == 10:     # Base case
        return
    print(someValue)
    return recursion(someValue+1)    # Recursive call

"""
    Pros:
        - Reduces the need for complex loops and auxiliary data structures
        - Can reduce time complexity easily with *memoization*
        - Works really well with recursive structures like trees and graphs
    Cons:
        - Slowness due to CPU overload
        - Can lead to out of memory errors / stack overflow exceptions
        - Can be unnecesarily complex if poorly constructed
"""

# Recursion with strings

# Example - String Reversal: Input a string, output the string backwards
#                              "Hello" -> "olleH"

def reverseString(input):
    # What is the base case? || When can I no longer continue?
    """
        To construct base cases think if I were to just pass in A VERY SMALL INPUT,
        what is the SMALLEST input that I could pass in to start to this function,
        where I would need to IMMEDIATELY RETURN.

        In this case I could stop when I pass in ONE LETTER, or an EMPTY STRING
    """
    if input == "":
        return ""
    # What is the smallest amount of work I can do in each iteration?
    """
        How do we even get to the point where we pass in an empty string?
    """
    return reverseString(input[1:]) + input[0]

print(reverseString("Hola"))



