def conta_pares(min, max):
    if min % 2:
        min += 1
    for n in range(min, max + 1, 2):
        if n == max or n == max - 1:
            print(n)
        else:
            print(n, end=" - ")

conta_pares(2, 9)

def fatorial(num):
    x = num
    result = 1
    for i in range(num):
        result = result * (num)
        num = num - 1
    print(x, "! = ", result, sep="")

fatorial(5)

def fatorial2(num):
    if num == 1:
        return 1
    return num * fatorial2(num - 1)

print(fatorial2(5))