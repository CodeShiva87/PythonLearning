#Find the sum of all the multiples of 3 or 5 below 1000.
n = 1000
count = 3
total = 0
while count < n:
    if count % 3 == 0 or count % 5 == 0:
        total += count
    count += 1

print(total)
