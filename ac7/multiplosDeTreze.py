min = int(input())
max = int(input())
soma = 0

for i in range(min, max + 1):
    if i % 13 == 0:
        continue
    soma = soma + i

print(soma)