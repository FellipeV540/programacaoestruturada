"""
operações em python
- Aritimeticas
-Atribuição
- Comparação (ou Relacionais)
- Logicas (ou Booleanas)
"""

# Operações Aritimeticas
# Dois operandos numéricos
x = 8.4
y = 2.3

print(x + y)
print(x - y)
print(x * y)
print(x / y)  # divisao normal
print(x ** y) # potencia
print(x // y) # divisao (inteira)
print(x % y)  # modulo (sobra da divisao)

# round(valor, num_digitos)
print(round(x - y,2))

# um operando é uma str
print("-" + "-") #concentração de strings
print("-" * 30) #multriplicação de strings

# operações de atribuição
x = 10

# mais comuns
x += 2 # x = x + 2
x -= 3 # x = x - 3

# menos comuns
x *= 5
x /= 4
x **= 2
x //= 6
x %= 2
print(x)
print(y)

# operações de comparação
# Resultam num valor booleano (True ou False)
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Comparação entre strins - tabela ASCII
# https://pt.wikipedia.org/wiki/ASCII

print("-" * 30)
x = "Fbc"
y = "abc"
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Operadores loicos
print("-" * 30)

x = True
y = False
print(x and y) # E
print(x or y)  # OU
print(not x)   # NÃO

# type casting
x = 9
print(float(x))
print(int("10"))

#  Em python, tudo que for diferente de "", 0, 0.0, é true
print(bool(x))
print(bool(0))

print("abc" and 16)
print(0 and 16)
print(False and 16)
print("" and 16)

print("abc" or 16)
print(10.5 or 16)
print(True or 16)
print("" or 16)

# isso sobe uma operação se o primeiro operando for false
print(6 or int("a"))

# Pythonico
nome = input("Seu nome: ") or "Valor inválido"

print(nome)

"""
Precedência

()
**
* / // %
+ -
> >= < <= == !=
not
and
or
"""

print(6 + 3 * 2 <= 15 - 2.5 // 4 % 3 and 10 / 2 or not 15 + 2 ** 2 < 2)
print(6 + 3 * 2 <= 15 - 2.5 // 4 % 3 and 10 / 2 or not 15 + 4 < 2)
print(6 + 6 <= 15 - 1.0 % 3 and 5 or not 15 + 4 < 2)
print(6 + 6 <= 15 + 2,0 and 5 or not 15 + 4 < 2)
print(True and 5 or not False)
print(True and 5 or True)
print(5.0 or True)
print(5,0)

print(6 + 3 * 2 <= 15 -( 2.5 // 4 % 3 and 10 / 2) or not 15 + 2 ** 2 < 2)
print(6 + 3 * 2 <= 15 -( 0.0 % 3 and 5) or not 15 + 2 ** 2 < 2)
print(12 <= 15 -( 0.0 and 5) or not 19 < 2)
print(12 <= 15 - 0.0 or not 19 < 2)
print(True or not False)
print(True or False)
print(True)