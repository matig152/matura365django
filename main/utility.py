import os
import json
from matura365.settings import BASE_DIR
from random import randint






# STAŁE
Dzialy = (('liczbyrzeczywiste','Liczby Rzeczywiste'), ('wyrazeniaalgebraiczne','Wyrażenia algebraiczne'),('rownania','Równania i nierówności'),
        ('funkcje','Funkcje'),('ciagi','Ciągi'),('trygonometria','Trygonometria'),('geometriaanalityczna','Geometria Analityczna'),('planimetria','Planimetria'),
        ('stereometria','Stereometria'),('statystyka','Statystyka i prawdopodobieństwo'),('optymalizacja','Optymalizacja'),)
# TEMATY
liczbyrzeczywiste = (('Ułamki','Ułamki'),('Potęgi i pierwiastki','Potęgi i pierwiastki'), ('Logarytmy','Logarytmy'), ('Procenty','Procenty'), ('Zbiory i przedziały','Zbiory i przedziały')) 
wyrazeniaalgebraiczne = (('Upraszczanie wyrażeń','Upraszczanie wyrażeń'), ('Wzory skróconego mnożenia','Wzory skróconego mnożenia'), ('Dowody algebraiczne','Dowody algebraiczne'))
rownania = (("Równania liniowe","Równania liniowe"), ("Równania wymierne","Równania wymierne"), ("Układy równań","Układy równań"), ("Równania z wartością bezwzględną","Równania z wartością bezwzględną"), ("Równania kwadratowe","Równania kwadratowe"), ("Nierówności liniowe","Nierówności liniowe"), ("Nierówności z wartością bezwzględną","Nierówności z wartością bezwzględną"), ("Nierówności kwadratowe","Nierówności kwadratowe"))
funkcje = (("Własności funkcji","Własności funkcji"), ("Funkcje liniowe","Funkcje liniowe"), ("Funkcje kwadratowe","Funkcje kwadratowe"), ("Funkcje wykładnicze i logarytmiczne","Funkcje wykładnicze i logarytmiczne"))
ciagi = (("Ciągi Arytmetyczne","Ciągi Arytmetyczne"), ("Ciągi Geometryczne","Ciągi Geometryczne"))
trygonometria = (("Własności f. trygonometrycznych","Własności f. trygonometrycznych"),  ("Zastosowania f. trygonometrycznych","Zastosowania f. trygonometrycznych"))
geometriaanalityczna = (("Odległości, symetrie, proste","Odległości, symetrie, proste"), ("Okręgi","Okręgi"))
planimetria = (("Trójkąty","Trójkąty"), ("Czworokąty i wielokąty","Czworokąty i wielokąty"), ("Koła i okręgi","Koła i okręgi"))
stereometria = (("Graniastosłupy i ostrosłupy","Graniastosłupy i ostrosłupy"), ("Bryły obrotowe","Bryły obrotowe"), ("Kąty w bryłach","Kąty w bryłach"))
statystyka = (("Statystyka","Statystyka"), ("Kombinatoryka","Kombinatoryka"), ("Prawdopodobieństwo","Prawdopodobieństwo"))
optymalizacja = (("Optymalizacja","Optymalizacja"), ("",""))


class Zadanie:
    def __init__(self, tresc, temat, trudnosc, czymat, odpowiedz):
        self.tresc = tresc
        self.temat = temat
        self.trudnosc = trudnosc
        self.czymat = czymat
        self.odpowiedz = odpowiedz
    
    def __str__(self):
        if(self.czymat==1):
            cz = ", Maturalne"
        else:
            cz = " "

        sb = "Temat: " + self.temat + "<br>Trudność: " + str(self.trudnosc) + cz +"<br>Treść: " + self.tresc + "<br>Odpowiedź: " + self.odpowiedz + "<br><br>"
        return sb

def parsujZadania(dzial):
    with open(os.path.join(BASE_DIR, f'main\static\json\{dzial}.json'), encoding='utf-8') as file:
        data = json.load(file)
        Zadania = []
        for zadanie in data:
            Zadania.append(Zadanie(zadanie['tresc'], zadanie['temat'], zadanie['trudnosc'], zadanie['czymat'], zadanie['odpowiedz']))
    return Zadania

def filtrujZadania(zadania, temat, trudnosc):
    ZadF = []
    for zad in zadania:
        if((zad.trudnosc in trudnosc) and (zad.temat in temat)):
            ZadF.append(zad)
    return ZadF

def losujZad(dzial, tematy, trudnosc):
    zadania = parsujZadania(dzial)
    zadania = filtrujZadania(zadania, tematy, trudnosc)
    return zadania[randint(0, len(zadania)-1)]

def generujTest(dzial, tematy, trudnosc, liczbazad):
    zadania = parsujZadania(dzial)
    zadania = filtrujZadania(zadania, tematy, trudnosc)
    i = 0
    zadaniaDoTestu = []
    while (i < liczbazad):
        los = randint(0, len(zadania)-1)
        zadaniaDoTestu.append(zadania[los])
        zadania.pop(los)
        i += 1
    return zadaniaDoTestu


def dzialText(dzial):
    dzialText = ""
    match dzial:
        case 'liczbyrzeczywiste': dzialText = "Liczby rzeczywiste"
        case 'wyrazeniaalgebraiczne': dzialText = "Wyrażenia algebraiczne"
        case 'rownania': dzialText = 'Równania i nierówności'
        case 'funkcje': dzialText = 'Funkcje'
        case 'ciagi':dzialText = 'Ciągi'
        case 'trygonometria':dzialText = 'Trygonometria'
        case 'geometriaanalityczna': dzialText = 'Geometria Analityczna'
        case 'planimetria':dzialText = 'Planimetria'
        case 'stereometria': dzialText = 'Stereometria'
        case 'statystyka':dzialText = 'Statystyka i prawdopodobieństwo'
        case 'optymalizacja':dzialText = 'Optymalizacja'
    return dzialText

def trudnoscText(t):
    match t:
        case 1:return("Łatwy")
        case 2:return("Średni")
        case 3:return("Trudny")

def dzialTematy(dzial):
    match dzial:
        case 'liczbyrzeczywiste': return liczbyrzeczywiste
        case 'wyrazeniaalgebraiczne': return wyrazeniaalgebraiczne
        case 'rownania': return rownania
        case 'funkcje': return funkcje
        case 'ciagi': return ciagi
        case 'trygonometria': return trygonometria
        case 'geometriaanalityczna': return geometriaanalityczna
        case 'planimetria': return planimetria
        case 'stereometria': return stereometria
        case 'statystyka': return statystyka
        case 'optymalizacja': return optymalizacja

def tematyText(tematy):
    if(len(tematy)==1):
        sb = "Temat: "
    else:
        sb = "Tematy: "
    for idx, temat in enumerate(tematy):
        if (idx != len(tematy)-1): 
            sb += f"{temat}, "
        else:
            sb += f"{temat}"
    return sb

def przegladajBaze(dzial, tematy, trudnosc):
    zadania = parsujZadania(dzial)
    zadania = filtrujZadania(zadania, tematy, trudnosc)
    return zadania


