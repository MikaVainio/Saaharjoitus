# Sovelluksen luokat määritellään täällä:

# Kirjastojen ja modulien lataukset

# Komponenttien alustukset

# Luokkien määritykset

class Saa_asema:
    """Luokka, jossa määritellään sääaseman ominaisuudet"""
    def __init__(self, nimi, tyyppi, sijainti):
        self.nimi = nimi
        self.tyyppi =tyyppi
        self.sijainti = sijainti

class Saahavainto:
    """Luokka, jossa määritellään sääsanoma ja muunoksia"""
    def __init__(self, paiva, lampotila, tuulen_nopeus, suunta, pilvisyys, nakyvyys):
        self.paiva = paiva
        self.lampotila = lampotila
        self.tuulen_nopeus = tuulen_nopeus
        self.suunta = suunta
        self.pilvisyys = pilvisyys
        self.nakyvyys = nakyvyys
        
    # Metodi, joka muutta m/s -> km/h
    def mps2kmh(self):
        kmh = self.tuulen_nopeus * 3.6 # x 3600(h) / 1000 (k)
        return kmh 

    # Metodi, joka muuttaa m/s -> kt
    def mps2knots(self):
        kts = self.tuulen_nopeus * 3600 / 1852 # 3600(h) / 1852(NM)
        return kts

if __name__ == "__main__":
    saa_asema = Saa_asema('Rajakari', 'Rannikkoasema', 'Turku')
    saahavainto = Saahavainto('25.4.', 4, 3, 90, 1, 25)
    print(saa_asema.sijainti, saa_asema.nimi)
    print('Tuuli:', saahavainto.tuulen_nopeus, 'm/s')
    print('Tuuli:', round(saahavainto.mps2kmh(), 1), 'km/h')
    print('Tuuli', round(saahavainto.mps2knots(), 1), 'solmua')