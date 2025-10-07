a=1
b = 2
total = 0

while b <= 4000000:
    if b % 2 == 0:
        total = total + b
    temp = a + b
    a = b
    b = temp

print(total)