# Print prime numbers between 10 and 100
for num in range(10, 101):
    if num < 2:# as no less than 2 are no n prime so the condition continue skips the line
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
# sqrt because a no multiple suppose 4*4 if the ssqrt of 4 is there means the no is non prime
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
