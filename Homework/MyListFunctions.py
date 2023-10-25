# MyListFunctions.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 22 October 2023
# This program defines functions acting on lists, many from the list class.
# Each function is defined with supplied headers with a comment.
# These functions are restricted to indexing/slicing (except for mySlice), 
# appending, len, in, not in, ==, !=.

def myAppend( lst, x ):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in order.
    out = []
    for i in lst1:
        out.append(i)
    for i in lst2:
        out.append(i)
    return out

def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    if len(lst) == 0:
        print("Empty list: no max value")
        return None
    else:
        maxValue = lst[0]
        for i in range(0, len(lst)):
            if lst[i] > maxValue:
                maxValue = lst[i]
        return maxValue
    

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    sumList = 0
    for i in lst:
        sumList += i
    return sumList

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    count = 0
    for i in range(0, len(lst)):
        if lst[i] == x:
            count += 1
    return count

def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    if i < 0 or i > (len(lst)):
        print("Invalid index")
        return None
    else:
        result = lst[0:i]
        result.append(x)
        result = result + lst[i:]
        return result

def myPop( lst, i ):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    if i < 0 or i >= (len(lst)):
        print("Invalid index")
        return lst, None
    else:
        remove = lst[i]
        result = lst[0:i]
        result = result + lst[i+1:]
        return result, remove

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    if x not in lst:
        return -1
    else:
        for i in range(0, len(lst)):
            if x == lst[i]:
                return i

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    if x not in lst:
        return -1
    else:
        for i in range(len(lst)-1, -1, -1):
            if x == lst[i]:
                return i

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    result = []
    for i in range(0, len(lst)):
        if lst[i] == x:
            result.append(i)
    return result

def myReverse( lst ):
    # Return a new list like lst but with the characters
    # in the reverse order. 
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    if x not in lst:
        return lst
    else:
        lst = lst[0:myFind(lst,x)] + lst[myFind(lst,x)+1:]
    return lst

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    if x not in lst:
        return lst
    else:
        while x in lst:
            lst = myRemove(lst, x)
        return lst

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves. 
    if i not in [x for x in range(0, len(lst)+1)] or j not in [x for x in range(0, len(lst)+1)]:
        return "Invalid index(s)"
    if len(lst) == 0:
        return lst
    else:
        result = []
        for x in range(i, j+1):
            result.append(lst[x])
        return result
    