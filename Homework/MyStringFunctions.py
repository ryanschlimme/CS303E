# MyStringFunctions.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 13 October 2023
# This program defines a collection of functions with comments only using
# ord, chr, indexing, appending, len, in, not in, ==, !=. No other str class 
# methods allowed.

def myAppend( s, ch ):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for i in range(0, len(s)):
        if ch in s[i]: count += 1
        else: continue
    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if len(s) == 0: 
        print("Empty string: no min value")
        return None
    else: 
        min = ord(s[0])
        for i in range(0, len(s)):
            if ord(s[i]) < min: 
                min = ord(s[i])
                i += 1
            else: i += 1
        return chr(min)

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if i > len(s): 
        print("Invalid index")
    else:
        first = s[0:i]
        last = s[i:(len(s)+1)]
        return first + ch + last

def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    if i > len(s):
        print("Invalid index")
        return None
    else:
        first = s[0:i]
        last = s[(i+1):(len(s)+1)]
        remove = s[i]
        return first+last, remove

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(0, len(s)):
        if s[i] == ch:
            return i
        else:
            i +=1
    return -1   

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)-1, 1, -1):
        if s[i] == ch:
            return i
        else:
            i +=1
    return -1   

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    num = -1
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            num = i
            break
        else:
            i -=1
    if num == -1: return s
    else:
        first = s[0:num]
        last = s[num+1:len(s)]
        return first+last

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    if ch not in s: return s
    while ch in s:
        s = myRemove(s, ch)
    return s

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order. 
    if len(s) == 1: return s
    else:
        string = s[-1]
        for i in range(len(s)-2, -1, -1):
            string = string + s[i]
        return string