def ler_nome():
    """Retorna nome do aluno inserido pelo usuario"""
    return input("Informe seu Nome: ")

def ler_notas():
    """le as notas do usuario"""
    ap1 = float(input("Nota Ap1: "))
    ap2 = float(input("Nota Ap2: "))
    asub = float(input("Nota Asub: "))
    ac = float(input("Nota Ac: "))
    return ap1, ap2, asub, ac



def analisar_subst(ap1, ap2, asub):
    """analiasr se a substitutiva deveria substituir alguma nota"""
    if asub > ap1 and ap1 < ap2:
        ap1 = asub
    elif asub > ap2 and ap2 < ap1:
        ap2 = asub
    elif asub > ap1 and ap1 == ap2:
        ap1 = asub
    return ap1, ap2


def calcular_media(ap1, ap2, asub, ac):
    """calcula e retorna a media do usuario"""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """retorna se o aulo foi aprovado"""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    """Retorna True se todas as notas estao entre 0 e 10, Inclusive."""
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return ap1, ap2, asub, ac



def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            print("Média final:", media)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado. Sua nota foi", media)
            else:
                print("Aluno foi reprovado. Sua nota foi", media)

main()
