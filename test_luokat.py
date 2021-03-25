# Tässä tiedostossa testataan lukkien metodeja

# Kirjastojen ja modulien lataukset
import luokat

# Luodaan testejä varten olio
pvm= '25.3.2021'
lampo = 4.5
tuulen_nopeus = 3
tuulen_suunta = 90
pilvisyys = 1
nakyvyys = 25
testihavainto = luokat.Saahavainto(pvm, lampo, tuulen_nopeus, tuulen_suunta, pilvisyys, nakyvyys)

def test_mps2km():
    assert round(testihavainto.mps2kmh(), 1) == 10.8

def test_mps2knots():
    assert round(testihavainto.mps2knots(), 1) == 5.8
