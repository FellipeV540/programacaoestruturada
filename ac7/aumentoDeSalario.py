def aumentoSalario():
    salAtual = float(input())

    if 0 <= salAtual <= 400.00:
        reajuste = salAtual * 0.15
        salNovo = salAtual + reajuste
        print(f"Novo salario: {salNovo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 15 %")

    elif 400.01 <= salAtual <= 800.00:
        reajuste = salAtual * 0.12
        salNovo = salAtual + reajuste
        print(f"Novo salario: {salNovo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 12 %")

    elif 800.01 <= salAtual <= 1200.00:
        reajuste = salAtual * 0.10
        salNovo = salAtual + reajuste
        print(f"Novo salario: {salNovo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 10 %")

    elif 1200.01 <= salAtual <= 2000.00:
        reajuste = salAtual * 0.07
        salNovo = salAtual + reajuste
        print(f"Novo salario: {salNovo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 7 %")

    elif salAtual > 2000.00:
        reajuste = salAtual * 0.04
        salNovo = salAtual + reajuste
        print(f"Novo salario: {salNovo:.2f}")
        print(f"Reajuste ganho: {reajuste:.2f}")
        print("Em percentual: 4 %")

    else:
        print("Valor Inválido")

aumentoSalario()
