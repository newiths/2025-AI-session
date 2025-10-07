limit = 2000000
total = 0

for num in range(2, limit):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        total = total + num

print(total)