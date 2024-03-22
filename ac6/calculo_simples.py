item1 = input().split()
item2 = input().split()

c1, n1, v1 = item1
c2, n2, v2 = item2

total = (int(n1) * float(v1)) + (int(n2) * float(v2))

print("VALOR A PAGAR: R$ %0.2f" %total)