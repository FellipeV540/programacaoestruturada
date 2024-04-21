def preenchimentoDeVetor():
    v = int(input())
    if v <= 50:
        for i in range(1, 11):
            v = v * 2
            print(f"N[{i}] = {v}")

preenchimentoDeVetor()