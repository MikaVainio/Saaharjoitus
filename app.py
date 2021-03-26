# Sovelluksen pääohjelma

# Kirjastojen ja modulien lataukset
import luokat
import funktiot # jos haluaa käyttää funktioita funktiot.py:stä

# Luodaan havaintoasemat
saa_asema1 = luokat.Saa_asema(1, 'Rajakari', 'Rannikkoasema', 'Turku')
saa_asema2 = luokat.Saa_asema(2, 'Pori', 'Lentokenttä', 'Pori')
saa_asema3 = luokat.Saa_asema(3, 'Helsinki-Vantaa', 'Lentokenttä', 'Vantaa')

havaintolista = []

# Syötetään havaintoja kunnes käyttäjä keskeyttää
while True:

    # Kysymykset ja tietotyyppimuunnokset
    numero = int(input('Aseman numero: '))
    paiva = input('Päivämäärä: ')
    lampotila = float(input('Lämpotila: '))
    tuulen_nopeus = float(input('Tuulen nopeus (m/s): '))
    suunta = float(input('Tuulen suunta (astetta): '))
    pilvisyys = int(input('Pilvisyys x/8: '))
    nakyvyys = float(input('Näkyvyys (km): '))

    # havainto-olion luominen
    havainto = luokat.Saahavainto(numero, paiva, lampotila, tuulen_nopeus, suunta, pilvisyys, nakyvyys)

    # Lisätään olio listaan
    havaintolista.append(havainto)

    # Tarkistetaan halutaanko syöttämistä jatkaa
    jatketaanko = input('Lisätäänkö uusi havainto? K/e ')
    if jatketaanko.upper() == 'E':
        break

# Haetaan yhden aseman havainnot aseman numeron perusteella
asemanumero = int(input('Anna aseman numero, jonka havainnot haluat: '))

for jasen in havaintolista:
    if jasen.numero == asemanumero:
        print('As.', jasen.numero, 'pvm:', jasen.paiva, 'lampötila:', jasen.lampotila, 'tuulen nopeus:', jasen.tuulen_nopeus)

# Haetaan kaikki tietyn päivän havainnot
paivays = input('Minkä päivän tiedot haluat? ')

for jasen in havaintolista:
    if jasen.paiva == paivays:
        print('As.', jasen.numero, 'pvm:', jasen.paiva, 'lampötila:', jasen.lampotila, 'tuulen nopeus:', jasen.tuulen_nopeus)

# Haetaan tietyn päivän havainnot halutusta asemasta
for jasen in havaintolista:
    if jasen.numero == asemanumero and jasen.paiva == paivays:
       print('As.', jasen.numero, 'pvm:', jasen.paiva, 'lampötila:', jasen.lampotila, 'tuulen nopeus:', jasen.tuulen_nopeus) 

# Hakufunktio, joka käyttää kiinteää listamuuttujaa (so. app.py:n muuttujaa)
def hae_asemanumerolla(numero):
    """Palauttaa säähavainnot havaintoaseman numeron perusteella app.py:n listasta havaintolista

    Args:
        numero (int): säähavaintoaseman numero
        
    Returns:
        list: lista aseman numeroa vastaavista säähavainnoista
    """
    osumalista = []
    for jasen in havaintolista:
        if jasen.numero == numero:
            osumalista.append(jasen)

    return osumalista


# Hakufunktio, joka käyttää kiinteää listamuuttujaa (so. app.py:n muuttujaa)
def hae_paivamaaralla (paiva):
    """Palauttaa säähavainnot päivämäärän perusteella app.py:n listasta havaintolista

    Args:
        paiva (str): säähavainnon päivämäärä
        
    Returns:
        list: lista päivän säähavainnoista
    """
    osumalista = []
    for jasen in havaintolista:
        if jasen.paiva == paiva:
            osumalista.append(jasen)

    return osumalista

# Tietojen haku funktiot.py:n funktioilla (vain viimeistä funktiota on käytetty)

# Numeron ja päivän perusteella parametrina annetusta listasta
tulokset = funktiot.hae_asemanumerolla_ja_paivalla_nimetysta_listasta(asemanumero, paivays, havaintolista)

print('Tuloksia löytyi', len(tulokset))

for tulos in tulokset:
    print('As', tulos.numero, 'pvm', tulos.paiva, 'lämpötila', tulos.lampotila )