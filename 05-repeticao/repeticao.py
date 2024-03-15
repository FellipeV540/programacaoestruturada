def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1

    print("Acabou")

contagem_regressiva(5)
print("_" * 30)

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(2, 10, 2)))
print("_" * 30)

def contagem_regressiva2(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva2(2)
print("_" * 30)

def pula_mult_3(max):
    for num in range(1, max + 1):
        if not num % 3:
            continue
        print(num)

pula_mult_3(15)
print("_" * 30)

def le_nome():
    while True:
        nome = input("Informe o nome: ")
        if nome:
            break

    print(nome)

le_nome()

def e_primo(num):
    for div in range(2, num):
        if num % div == 0:
            print("não é primo")
            break
    else:
        print(num, "é primo")

e_primo(7)
e_primo(15)
e_primo(31)
e_primo(49)