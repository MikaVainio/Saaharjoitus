# Funktiot, joilla voi tehdä pääohjelman haut

# Kirjastojen ja modulien lataukset


# Funktioiden määrittelyt

# Haetaan aseman säähavainnot numeron perusteella, listamuuttuja annetaan parametrina
def hae_asemanumerolla_nimetysta_listasta(numero, lista):
    """Palauttaa säähavainnot havaintoaseman numeron perusteella

    Args:
        numero (int): säähavaintoaseman numero
        lista (list): lista säähavinnoista

    Returns:
        list: lista aseman numeroa vastaavista säähavainnoista
    """
    osumalista = []
    for jasen in lista:
        if jasen.numero == numero:
            osumalista.append(jasen)

    return osumalista

# Haetaan säähavainnot päivän perusteella, listamuuttuja annetaan parametrina
def hae_paivamaaralla_nimetysta_listasta(paiva, lista):
    """Palauttaa säähavainnot havaintoaseman numeron perusteella

    Args:
        paiva (str): säähavainnon päivämäärä
        lista (list): lista säähavinnoista

    Returns:
        list: lista halutun päivän säähavainnoista
    """
    osumalista = []
    for jasen in lista:
        if jasen.paiva == paiva:
            osumalista.append(jasen)
            
    return osumalista

# Haetaan aseman säähavainnot numeron perusteella, listamuuttuja annetaan parametrina
def hae_asemanumerolla_ja_paivalla_nimetysta_listasta(numero, paiva, lista):
    """Palauttaa säähavainnot havaintoaseman numeron ja päivämäärän perusteella

    Args:
        numero (int): säähavaintoaseman numero
        paiva (str): säähavainnon päivämäärä
        lista (list): lista säähavinnoista

    Returns:
        list: lista aseman numeroa vastaavista säähavainnoista
    """
    osumalista = []
    for jasen in lista:
        if jasen.numero == numero and jasen.paiva == paiva:
            osumalista.append(jasen)

    return osumalista