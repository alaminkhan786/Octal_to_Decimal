N = int(input("Enter the value of N: "))
sum = 0
i = 0

while N != 0:
    digit = N % 10
    digit = digit * (8**i)
    sum = sum + digit
    N = N // 10
    i = i + 1
print(sum)