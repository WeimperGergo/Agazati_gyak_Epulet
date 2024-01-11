import bevezetes
import epuletek
import sorozat

# bevezetes.jatekos()
# penzlista = sorozat.penzdobas()
# fejSzam = sorozat.fejek_szama(penzlista)
# sorozat.konzol_kiir(fejSzam)
# sorozat.fajl_kiir(fejSzam)

epuletLista = epuletek.beolvas()
epuletek.epuletDb(epuletLista)
epuletek.magasabb555(epuletLista)
epuletek.legoregebb(epuletLista)

