# exercicio 2
def maior(a, b):
    if a > b:
        return a
    elif a == b:
        return "São iguais"
    return b

def maior2(n1,n2):
    return n1 if n1 > n2 else n2

# exercicio 4
def vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "é vogal"
    return "é consoante"

# print(vogal("l"))
# print(vogal("a"))

def vogal2(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return "é vogal"
        case _:
            return "é consoante"

# print(vogal2("l"))
# print(vogal2("a"))

# exercicio 5
def nota_valida(nota):
    return 10 >= nota >= 0


def media(n1, n2, n3):
    m = (n1 + n2 + n3) / 3
    if nota_valida(n1) and nota_valida(n2) and nota_valida(n3):
        if 10 > m >= 7:
            print("Aprovado, sua nota foi", m)
        elif 0 <= m < 7:
            print("Reprovado, sua nota foi", m)
        elif m == 10:
            print("Aprovado com Distinção, sua nota foi", m)
    else:
        print("Nota Inválida")

# print(media(int(input("Primeira Nota: ")), int(input("Segunda Nota: ")), int(input("Terceira Nota: "))))
media(10, 10, 10)   # distinção
media(10, 8, 9)     # aprovado
media(6, 5, 5)      # reprovado
media(11, 11, 11)   #Nota Inválida
media(11, 9, 10)    # Nota Inválida