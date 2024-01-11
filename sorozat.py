import random


def penzdobas():
    lista = []
    for i in range(7):
        rSzam = random.randint(0, 1)
        lista.append(rSzam)
    print("II/A, B, C:", end="\n\t")
    for i in range(len(lista)-1):
        if lista[i] == 0:
            print("ÍRÁS", end="-")
        else:
            print("FEJ", end="-")
    # if lista[-1] == 0:
    #     print("ÍRÁS")
    # else:
    #     print("FEJ")
    print(f"ÍRÁS" if lista[-1] == 0 else "FEJ")
    return lista


def fejek_szama(lista):
    fejSz = 0
    for i in range(0, len(lista)):
        if lista[i] == 1:
            fejSz += 1

    return fejSz


def konzol_kiir(fejSz):
    print(f"II/D, E:\n\tA fejek száma: {fejSz}")


def fajl_kiir(fejSzam):
    fajlba = open("fejek.txt", "w", encoding="utf-8")
    fajlba.write(f"II/F:\n\tA fejek száma: {fejSzam}")
    fajlba.close()
