n = 7

current_sum = 0
i = 0

while i <= n:
    current_sum += i
    i += 1

print(current_sum)



for i in range(n+1):
    current_sum += i

print(current_sum)


n = 30293
count = 0

while n != 0:
    count = count + 1
    n = n // 10

print(count)