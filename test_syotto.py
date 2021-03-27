# Testataan syötteen ja konsolitulostusten toimintaa

# Kirjastojen ja modulien lataukset
import syotto

# Testifunktiot

# Testataan syötteen simulointia, käyttämällä pytest-kirjaston monkeypatch funktioita
def test_kysy_nimi(monkeypatch): # argumenttina monkeypatch-moduli (venv - pytest - monkeypatch.py)
    syote = 'Calle'
    monkeypatch.setattr('builtins.input', lambda _: syote) # korvataan järjestelmän input() muuttujalla syote
    assert syotto.kysy_nimi() == syote # varsinainen testi

# Testataan tulosteen simulointia käyttämällä järjestelmälaitteiden kaappausta capsys
def test_ilmoitus(capsys):
    syotto.ilmoitus('Erkki') # Tulostaa: Hei vaan hei Erkki
    ulos, virhe = capsys.readouterr() # Kaapataan konsolin tuoloste kahteen muuttujaan
    assert ulos == 'Hei vaan hei Erkki\n' # Tarkistetaan lopputulos, huomaa print lisää rivinvaihdon \n
    assert virhe == ''