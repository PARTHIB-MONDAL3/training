'''Write a while loop program that keeps
asking the user to enter a positive number and stops only when the user enters
a negative number.'''
while True:
    n = int(input("Enter a positive number (negative to stop): "))
    if n < 0:
        print("Stopping on negative input.")
        break
    # At this point n is >= 0 (positive or zero)
    print("You entered:", n)


