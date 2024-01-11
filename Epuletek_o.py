class Epulet:
    def __init__(self, sor: str):
        darabolt = sor.strip().split('$')
        self.nev = darabolt[0]
        self.varos = darabolt[1]
        self.orszag = darabolt[2]
        self.magassag = float(darabolt[3].replace(",",  "."))
        self.emeletek = int(darabolt[4])
        self.epultEv = int(darabolt[5])
