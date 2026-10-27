def powitaj(nick):
    print(f"Witaj w turnieju czleku {nick}")

powitaj("Adra")
powitaj("Young maga")
powitaj("Ala")

def oblicz_punkty(punkty):
    print(punkty + 20)

def policz_bonus(punkty):
    return punkty + 20

nowy_wynik = policz_bonus(100)
print(nowy_wynik * 2)



wyniki = [120, 85, 160, 85, 210, 95, 140]


def najlepszy_wynik(lista):
    return max(lista)


def policz_srednia(lista):
    if len(lista) == 0:
        return 0
    return round(sum(lista) / len(lista), 2)


def policz_awansy(lista, prog):
    licznik = 0

    for wynik in lista:
        if wynik >= prog:
            licznik = licznik + 1

    return licznik


def pokaz_raport(lista):
    print("CENTRUM WYNIKOW")
    print("Najlepszy wynik:", najlepszy_wynik(lista))
    print("Srednia punktow:", policz_srednia(lista))
    print("Liczba awansow (prog 120):", policz_awansy(lista, 120))


pokaz_raport(wyniki)
