n = 1000
count = 3
total = 0
while count < n:
    if count % 3 == 0 or count % 5 == 0:
        total += count
    count += 1

print(total)
