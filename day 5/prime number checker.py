def prime_checker(number):
    divided_count = 0
    for num in range(2, 101):
        if number % num == 0:
            divided_count += 1
    if divided_count > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input())  # Check this number
prime_checker(number=n)
