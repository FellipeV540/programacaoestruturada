import random

def fight():
    # stats aventureiro
    hp_aven = 100
    atk_aven = random.randint(10, 20)
    def_aven = random.randint(1, 5)

    # stats monstro
    hp_mon = random.randint(60, 80)
    atk_mon = random.randint(20, 30)

    r = 1

    while hp_mon > 0 and hp_aven > 0:

        print("Aventureiro: vida", hp_aven, "- Ataque", atk_aven, "- Defesa", def_aven)
        print("Monstro: vida", hp_mon, "- Ataque", atk_mon)
        print("rodada", r)

        atk_aven_r = random.randint(1, atk_aven)
        hp_mon = hp_mon - atk_aven_r

        if hp_mon <= 0:
            print("Monstro Derrotado")
            break

        atk_mon_r = random.randint(1, atk_mon)
        if def_aven < atk_mon_r:
            hp_aven = hp_aven - (atk_mon_r - def_aven)

        if hp_aven <= 0:
            print("Aventureiro Derrotado")
            break

        r += 1

fight()
