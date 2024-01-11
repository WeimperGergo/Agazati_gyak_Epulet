from Epuletek_o import Epulet


def beolvas():
    lista = []
    fajlbol = open("epulet.txt", "r", encoding="utf-8")
    fajlbol.readline()
    sorok = fajlbol.readlines()
    fajlbol.close()

    for i in range(0, len(sorok)):
        lista.append(Epulet(sorok[i]))  # Sor = egy épülettel, hozzáadjuk a listához.

    return lista


def epuletDb(lista):
    epuletSzam = 0
    for i in range(0, len(lista)):
        epuletSzam += 1
    print(f"III/A, B:\n\tAz épületek száma: {epuletSzam}")


def magasabb555(lista: list[Epulet]):
    magasabbDb = 0
    LAB = 3.280839895       # Konstans, ezért nagybetűs az egész
    for i in range(0, len(lista)):
        # Magasságot méterben megszorozzuk lábbal, ha ez > 555 akkor megnöveli a db-ot
        if (lista[i].magassag*LAB) > 555:
            magasabbDb += 1
    print(f"III/C:\n\tAz 555 lábnál magasabb épületek száma: {magasabbDb}.")


# listán belüli osztály definiálással kiírja segítséként az osztály tulajdonságait
def legoregebb(lista: list[Epulet]):
    legoregebbIndex = 0
    for i in range(1, len(lista)):
        if lista[i].epultEv < lista[legoregebbIndex].epultEv:
            legoregebbIndex = i
    print(f"III/D:\n\tA legöregebb épület országa: {lista[legoregebbIndex].orszag}")






