sum_of_squares = 0
sum_total = 0

for i in range(1, 101):
    sum_of_squares = sum_of_squares + i * i
    sum_total = sum_total + i

square_of_sum = sum_total * sum_total

print(square_of_sum - sum_of_squares)