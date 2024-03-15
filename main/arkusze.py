from .utility import parsujZadania, filtrujZadania, Zadanie
import random


Dzialy = ['liczbyrzeczywiste','wyrazeniaalgebraiczne','rownania','funkcje','ciagi','trygonometria','planimetria','geometriaanalityczna','stereometria','statystyka','optymalizacja']

def wylosujZadanie(dzial, temat, trudnosc, i, czyTematyX):
    zadania = parsujZadania(dzial)
    przefiltrowane = []
    if (czyTematyX):
        if(i in [20,21,22,23,27, 28]):
            for zadanie in zadania:
                if(zadanie.trudnosc == trudnosc and zadanie.czymat == 1):
                    przefiltrowane.append(zadanie)
        else:
            for zadanie in zadania:
                if(zadanie.temat == temat and zadanie.trudnosc == trudnosc and zadanie.czymat == 1):
                    przefiltrowane.append(zadanie)
    else:
        for zadanie in zadania:
                if(zadanie.temat == temat and zadanie.trudnosc == trudnosc and zadanie.czymat == 1):
                    przefiltrowane.append(zadanie)
    return przefiltrowane[random.randint(0, len(przefiltrowane)-1)]


def generuj2023():
    tematy = ["Potęgi i pierwiastki","Logarytmy", "Procenty", "Upraszczanie wyrażeń", "Dowody algebraiczne", "Równania wymierne", "Układy równań", "Równania kwadratowe", "Nierówności liniowe", "Nierówności z wartością bezwzględną", "Nierówności kwadratowe", "Własności funkcji", "Funkcje liniowe", "Funkcje kwadratowe", "Funkcje kwadratowe", "Funkcje wykładnicze i logarytmiczne", "Ciągi Arytmetyczne", "Ciągi Arytmetyczne", "Ciągi Geometryczne", "Ciągi Geometryczne", "x", "x", "x", "x", "Odległości, symetrie, proste", "Odległości, symetrie, proste", "Okręgi", "x", "x", "Statystyka", "Statystyka", "Kombinatoryka", "Prawdopodobieństwo", "Optymalizacja"] 
    listatrudnosci = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
    random.shuffle(listatrudnosci)
    listazadan = []
    i=0
    while(i<34):
        if(i<3): listazadan.append(wylosujZadanie(Dzialy[0], tematy[i], listatrudnosci[i], i, True))
        elif(i>=3 and i<=4): listazadan.append(wylosujZadanie(Dzialy[1], tematy[i], listatrudnosci[i], i, True))
        elif(i>=5 and i<=10): listazadan.append(wylosujZadanie(Dzialy[2], tematy[i], listatrudnosci[i], i, True))
        elif(i>=11 and i<=15): listazadan.append(wylosujZadanie(Dzialy[3], tematy[i], listatrudnosci[i], i, True))
        elif(i>=16 and i<=19): listazadan.append(wylosujZadanie(Dzialy[4], tematy[i], listatrudnosci[i], i, True))
        elif(i == 20): listazadan.append(wylosujZadanie(Dzialy[5], tematy[i], listatrudnosci[i], i, True))
        elif(i>=21 and i<=23): listazadan.append(wylosujZadanie(Dzialy[6], tematy[i], listatrudnosci[i], i, True))
        elif(i>=24 and i<=26): listazadan.append(wylosujZadanie(Dzialy[7], tematy[i], listatrudnosci[i], i, True))
        elif(i>=27 and i<=28): listazadan.append(wylosujZadanie(Dzialy[8], tematy[i], listatrudnosci[i], i, True))
        elif(i>=29 and i<=32): listazadan.append(wylosujZadanie(Dzialy[9], tematy[i], listatrudnosci[i], i, True))
        else: listazadan.append(wylosujZadanie(Dzialy[10], tematy[i], listatrudnosci[i], i, True))
        i += 1
    return listazadan
    
        
def generuj2015():
    listatrudnosci = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
    tematy = ["Potęgi i pierwiastki","Logarytmy", "Procenty", "Wzory skróconego mnożenia", "Dowody algebraiczne", "Równania liniowe", "Równania wymierne", "Układy równań","Równania z wartością bezwzględną", "Równania kwadratowe", "Nierówności liniowe", "Nierówności z wartością bezwzględną", "Nierówności kwadratowe", "Własności funkcji", "Funkcje liniowe", "Funkcje kwadratowe", "Funkcje kwadratowe", "Funkcje wykładnicze i logarytmiczne", "Ciągi Arytmetyczne", "Ciągi Geometryczne", "Własności f. trygonometrycznych", "Zastosowania f. trygonometrycznych", "Trójkąty", "Trójkąty","Czworokąty i wielokąty","Koła i okręgi","Koła i okręgi", "Odległości, symetrie, proste", "Okręgi", "Graniastosłupy i ostrosłupy", "Bryły obrotowe","Kąty w bryłach", "Statystyka", "Statystyka", "Kombinatoryka", "Prawdopodobieństwo"]
    random.shuffle(listatrudnosci)
    listazadan = []
    i=0
    while(i<36):
        if(i<3): listazadan.append(wylosujZadanie(Dzialy[0], tematy[i], listatrudnosci[i], i, False))
        elif(i>=3 and i<=4): listazadan.append(wylosujZadanie(Dzialy[1], tematy[i], listatrudnosci[i], i, False))
        elif(i>=5 and i<=12): listazadan.append(wylosujZadanie(Dzialy[2], tematy[i], listatrudnosci[i], i, False))
        elif(i>=13 and i<=17): listazadan.append(wylosujZadanie(Dzialy[3], tematy[i], listatrudnosci[i], i, False))
        elif(i>=18 and i<=19): listazadan.append(wylosujZadanie(Dzialy[4], tematy[i], listatrudnosci[i], i, False))
        elif(i>=20 and i<=21): listazadan.append(wylosujZadanie(Dzialy[5], tematy[i], listatrudnosci[i], i, False))
        elif(i>=22 and i<=26): listazadan.append(wylosujZadanie(Dzialy[6], tematy[i], listatrudnosci[i], i, False))
        elif(i>=27 and i<=28): listazadan.append(wylosujZadanie(Dzialy[7], tematy[i], listatrudnosci[i], i, False))
        elif(i>=29 and i<=31): listazadan.append(wylosujZadanie(Dzialy[8], tematy[i], listatrudnosci[i], i, False))
        else: listazadan.append(wylosujZadanie(Dzialy[9], tematy[i], listatrudnosci[i], i, False))
        i += 1
    return listazadan

def generujMalaMatura():
    listatrudnosci = [1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    random.shuffle(listatrudnosci)
    i=0
    listazadan = []
    while(i<11):
        zadania = parsujZadania(Dzialy[i])
        przefiltrowane = []
        for zadanie in zadania:
            if(zadanie.trudnosc == listatrudnosci[i] and zadanie.czymat == 1): przefiltrowane.append(zadanie)
        listazadan.append(przefiltrowane[random.randint(0, len(przefiltrowane)-1)])
        i+=1
    return listazadan

def losujZadGlowna():
    dzial = Dzialy[random.randint(0, 10)]
    zadania = parsujZadania(dzial)
    return zadania[random.randint(0, len(zadania)-1)]