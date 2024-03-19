"""
Estruturas de decisão
- if/elif/else
-match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom Dia!")
    elif turno == "T":
        print("Boa Tarde")
    elif turno == "N":
        print("Boa Noite")
    else:
        print("Dado Inválido")

def saudacao2(turno):
    if turno == "M":
        return "Bom Dia"
    if turno == "T":
        return "Boa Tarde"
    if turno == "N":
        return "Boa Noite"
    return "Dado Inválido"

saudacao("N")
saudacao("M")
saudacao("T")
saudacao("A")

print("-" * 30)
saudacao2("M")
saudacao2("N")

def le_nome():
    nome = input("Informe o nome: ")
    # if nome == "":
    if not nome:
        print("Erro! Entrada Inválida.")

    return nome

# ternario
def e_par(num):
    if num % 2:
        return "é impar"
    return "é par"

def e_par2(num):
    return "é impar" if num % 2 else "é par"

def saudacao3(turno):
    match turno:
        case "M":
            print("Bom Dia!")
        case "T":
            print("Boa Tarde!")
        case "N":
            print("Boa Noite!")
        case _: # default case, opicional
            print("Dado Inválido")

saudacao3("M")
saudacao3("T")
saudacao3("N")
saudacao3("A")



