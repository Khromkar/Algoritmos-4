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
#########################################################################
#                   ****RECURSION WITH STRINGS****                      #
#########################################################################
# Example - String Reversal: Input a string, output the string backwards#
#                              "Hello" -> "olleH"                       #
#########################################################################
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
    #reverseString(input[1:]) shrinks the problem space, as I'm passing in a shorter string
    #input[0] is the smallest unit of work to contribute to the recursive call
    return reverseString(input[1:]) + input[0]

# print(reverseString("Hola"))
# reverseString("ola") + H
# reverseString ("la") + o
# reverseString ("a") + l
# reverseString ("") + a <- which reaches the base case
# returns aloH

#########################################################################
# Example - Palindrome: Input a string, check if its spelled the same   #
#                       backwards than forward                          #
#                    -> "kayak" backwards is "kayak"                    #
#########################################################################

def palindrome(word):
    # Base case. One or none letters left:
    if len(word) == 0 or len(word) == 1:
        return True
    
    # Shrink problem space
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    # In case the word is not palindrome
    else:
        return False

# print(palindrome("kayak"))
# as k = k, return palindrome("aya")
# as a = a, return palindrome("y")
# as y is 1 letter long, we reach base case, returns True

#########################################################################
#                   ****RECURSION WITH NUMBERS****                      #
#########################################################################
# Example - Decimal to Binary: Input a number, return its decimal value #
#########################################################################

def binaryConverter(number,result):
    # Base case: number//2 = 0
    if (number // 2) == 0:
        return result
    
    # Shrink problem space
    else:
        result = str(number % 2) + result
        return binaryConverter(number//2,result)

print(binaryConverter(233,""))
# 233 // 2 is not 0 -> result = "1" + "" -> return binaryConverter(116,"1")
# 116 // 2 is not 0 -> result = "0" + "1" -> return binaryConverter(58,"01")
# 58 // 2 is not 0 -> result = "0" + "01" -> return binaryConverter(29 + "001")
# 29 // 2 is not 0 -> result = "1" + "001" -> return binaryConverter(14 + "1001")
# 14 // 2 is not 0 -> result = "0" + "1001" -> return binaryConverter(7 + "01001")
# 7 // 2 is not 0 -> result = "1" + "01001" -> return binaryConverter(3 + "101001")
# 3 // 2 is not 0 -> result = "1" + "101001" -> return binaryConverter(1 + "1101001")
# 1 // 2 is 0 -> return "1101001"

