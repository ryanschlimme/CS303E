# Zeller.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 12 September 2023
# This program takes integer inputs Y, m, d corresponding to year, month (1-12), day (1-31). Then it computes
# K (last two digits of year), J (century) and outputs the day of the week for that year using Zeller's Congruence 
# algorithm. Program does not correct for illegal dates such as Feb 31 or produce an error for float inputs.

def main():
    # Executes Zeller's algorthm with built in error printing.

    # Accept the year from the user and convert it to an int.
    Y = int(input("\nEnter year (e.g., 2008): "))
    # If the year is not greater than 1752, print an error
    # message and exit the program. 
    if (Y < 1753):
        print("Year must be > 1752. Illegal year entered:", Y, "\n")
        return

    # Accept the month from the user and convert it to an int.
    m = int(input("Enter month (1-12): "))
    # If the month is not greater than 1752, print an error
    # message and exit the program. 
    if (m < 1 or m > 12):
        print("Month must be in [1..12]. Illegal month entered:", m, "\n")
        return

    # Accept the day from the user and convert it to an int.
    d = int(input("Enter day of the month (1-31): "))
    # If the day is not greater than 1752, print an error
    # message and exit the program. 
    if (d < 1 or d > 31):
        print("Day must be in [1..31]. Illegal day entered:", d, "\n")
        return

    # Compute the other variables, including h
    if (m == 1 or m == 2):
        m = m + 12
        if Y % 100 == 0:
            J = Y // 100 - 1
            K = (Y-1) % 100
        else:
            J = Y // 100
            K = (Y-1) % 100
    else:
        J = Y // 100
        K = Y % 100
    
    # Zeller's Congruence algorithm where h is the day of the week (1-7)
    h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7

    # Compute the name of the day from h
    if h == 1:
        h = "Sunday"
    elif h == 2:
        h = "Monday"
    elif h == 3:
        h = "Tuesday"
    elif h == 4:
        h = "Wednesday"
    elif h == 5:
        h = "Thursday"
    elif h == 6:
        h = "Friday"
    else:
        h = "Saturday"

    # print the day of week message
    print("Day of the week is", h, "\n")

# You'll need this to run your main program. 
main()     