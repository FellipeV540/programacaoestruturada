# exercicio 1
def media():
    ap1 = float(input("Nota AP1: "))
    ap2 = float(input("Nota AP2: "))
    ac = float(input("Nota AC: "))

    media = (ap1 + ap2) * 0.4 + ac * 0.2

    print("A média é", round(media, 2))

# exercicio 2
def outra_media(ap1, ap2, ac):
    return (ap1 + ap2) * 0.4 + ac * 0.2

def main():
    media()
    print(outra_media(7, 8, 9.2))
    print(outra_media(7.7, 6.5, 7.3))

main()
