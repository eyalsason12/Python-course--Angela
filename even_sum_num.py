target = int(input('enter a number between 0 to 1000 '))
even_sum = 0
for num in range(2, target+1, 2):
    if (num % 2) == 0:
        even_sum += num
print(even_sum)