# CS 303E Quiz 3C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

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


def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for i in range(0, len(s)):
        if ch in s[i]: count += 1
        else: continue
    return count

# Problem 1: Proportion of Vowels
def vowelProportion(str):
    # replace pass with your solution to problem 1
    count = len(myRemoveAll(str, " "))
    a = myCount(str, "a")
    e = myCount(str, "e")
    i = myCount(str, "i")
    o = myCount(str, "o")
    u = myCount(str, "u")
    return (a+e+i+o+u) / count


# Problem 2: Bank Account Class
class BankAccount:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, name, initialAmount):
        self.__Name = name
        self.__Amount = initialAmount

    def withdraw(self, amount):
        if amount <= self.__Amount:
            self.__Amount -= amount
            return amount
        else:
            minus = self.__Amount
            self.__Amount = 0
            return minus

    def deposit(self, amount):
        self.__Amount += amount

    def getBalance(self):
        return ("$" + format(self.__Amount, "0.2f"))

    def __str__(self):
        return ("The "+ str(self.__Name)+ " account currently has "+ "$" + format(self.__Amount, "0.2f"))


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(vowelProportion('purple burglar alarm'))
    # print(vowelProportion('predictive text says it was good news for the test and i think i should be able to get a new phone on the computer'))
    # print(vowelProportion('a'))

    # ba = BankAccount("Chase", 100.0)
    # print(ba.getBalance())

    # ba = BankAccount("Wells Fargo", 50.5)
    # print(ba.withdraw(75))
    # print(str(ba))

    # ba = BankAccount("Bank of America", 20.21)
    # print(ba.withdraw(10.21))
    # ba.deposit(90.0)
    # print(ba.getBalance())
    # print(str(ba))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT