def paresEntre5():
    par = 0

    a = int(input())
    if a % 2 == 0:
        par += 1

    b = int(input())
    if b % 2 == 0:
        par += 1

    c = int(input())
    if c % 2 == 0:
        par += 1

    d = int(input())
    if d % 2 == 0:
        par += 1

    e = int(input())
    if e % 2 == 0:
        par += 1

    print(f"{par} valores pares")

paresEntre5()