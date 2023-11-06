# RecursiveFunctions.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 03 November 2023
# This program completes many recursive functions defined by the semantics 
# indicated by their comments without input validation.

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    """ Return the sum of the non-negative integers to n. 
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
        return 0
    else:
        return n + addToN(n-1)

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
        return 0
    else:
        z = n % 10
        n = (n - z) // 10
        return z + findSumOfDigits(n)

def integerToBinary( n ):
    """ Given a nonnegative integer n, return the 
    binary representation as a string. """
    if n == 0:
        return ""
    else:
        z = n % 2
        n = n // 2
        return integerToBinary(n) + str(z)

def integerToList( n ):
    """ Given a nonnegative integer, return a list of the 
    digits (as strings). """
    if n // 10 == 0:
        return [str(n % 10)]
    else:
        z = n % 10
        n = n // 10
        out = list(str(z))
        return integerToList(n)+out
    
def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if len(s) == 0:
        return True
    if s[len(s)-1] == s[0]:
        s = s[1:len(s)-1]
        return isPalindrome(s)
    else:
        return False

# def findFirstUppercase( s ):
#    """ Return the first uppercase letter in 
#    string s, if any. Return None if there
#    is none. """

# # for this one, don't reverse the string.
# def findLastUppercase( s ):
#    """ Return the last uppercase letter in 
#    string s, if any. Return None if there
#    is none. """

# def findFirstUppercaseIndexHelper( s, index ):
#    """ Helper function for findFirstUppercaseIndex.
#    Return the index of the first uppercase letter;
#    assume you are starting at index. Return -1 
#    if there is none."""

# # The following function is already completed for you. But 
# # make sure you understand what it's doing. 

# def findFirstUppercaseIndex( s ):
#    """ Return the index of the first uppercase letter in 
#    string s, if any. Return -1 if there is none. This one 
#    requires a helper function, which is the recursive 
#    function. """
#    return findFirstUppercaseIndexHelper( s, 0 )