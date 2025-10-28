'''Krishanamurthy Off-Class Test Case'''

def krishanamurthy_number():
    '''Function to check if a number is a Krishanamurthy number'''
    num = int(input("Enter a number: "))
    sum_of_factorials = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        temp //= 10

    if sum_of_factorials == num:
        print(f"{num} is a Krishanamurthy number.")
    else:
        print(f"{num} is not a Krishanamurthy number.")
krishanamurthy_number()
'''output:Enter a number: 145
145 is a Krishanamurthy number. '''