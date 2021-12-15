# repetitive Addition
def repetitiveAddition(m):
    sum1 = 0
    while (m > 0):
        sum1 = int(sum1 + m % 10)
        m = int(m) / 10
    return sum1


n = int(input("Enter a no"))
sum = repetitiveAddition(n)
while(sum >= 10):
    sum = repetitiveAddition(sum)
print(sum)

