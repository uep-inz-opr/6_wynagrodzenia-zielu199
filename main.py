class Pracownik:
    def __init__(self, imie, placa):
        self.imie = imie
        self.placa = int(placa)

    def oblicz_wynagrodzenie_netto(self) -> float:
        ubezpieczenia_spoleczne = float(round(self.placa * 0.0976, 2) + round(self.placa * 0.015, 2) +
                                        round(self.placa * 0.0245, 2))
        podstawa_na_ubezp_zdrowotne = self.placa - ubezpieczenia_spoleczne
        skladka_na_uz_wynagrodzenie = round(podstawa_na_ubezp_zdrowotne * 0.09, 2)
        skladka_na_uz_podatek = round(podstawa_na_ubezp_zdrowotne * 0.0775, 2)
        koszty_uzyskania_przychodu = 111.25
        podstawa_obliczenia_zaliczki_na_pd = round(self.placa - koszty_uzyskania_przychodu -
                                                   ubezpieczenia_spoleczne, 2)
        zaliczka_na_pd_przed_odliczeniem_sz = round((podstawa_obliczenia_zaliczki_na_pd * 0.18) - 46.33, 2)
        zaliczka_na_pd_do_pobrania = round(zaliczka_na_pd_przed_odliczeniem_sz - skladka_na_uz_podatek)
        kwota_do_wyplaty = self.placa - ubezpieczenia_spoleczne - skladka_na_uz_wynagrodzenie - \
                           zaliczka_na_pd_do_pobrania
        return round(kwota_do_wyplaty, 2)

    def oblicz_koszt_pracodawcy(self) -> float:
        skladka_emerytalna = round(self.placa * 0.0976, 2)
        skladka_rentowa = round(self.placa * 0.065, 2)
        skladka_wypadkowa = round(self.placa * 0.0193, 2)
        skladka_na_fp = round(self.placa * 0.0245, 2)
        skladka_na_fgsp = round(self.placa * 0.001, 2)
        return round(self.placa + skladka_na_fp + skladka_emerytalna + skladka_na_fgsp + skladka_rentowa + \
               skladka_wypadkowa, 2)

pracownicy = []
liczba_pracownikow = int(input())

for pracownik in range(liczba_pracownikow):
    dane_pracownika = input().split()
    imie = dane_pracownika[0]
    placa = int(dane_pracownika[1])
    pracownik = Pracownik(imie, placa)
    pracownicy.append(pracownik)

for pracownik in pracownicy:
    wynagrodzenie_netto = pracownik.oblicz_wynagrodzenie_netto()
    koszt_pracowdawcy = pracownik.oblicz_koszt_pracodawcy()
    suma_skladek = round(koszt_pracowdawcy - pracownik.placa, 2)
    formatowanie = "{0:.2f}"
    print(pracownik.imie + " " + str(formatowanie.format(wynagrodzenie_netto)) + " " +
          str(formatowanie.format(suma_skladek)) + " " + str(formatowanie.format(koszt_pracowdawcy)))




laczny_koszt_pracodawcy = 0
for i in range(len(pracownicy)):
    koszt = pracownicy[i].oblicz_koszt_pracodawcy()
    laczny_koszt_pracodawcy += koszt

print(laczny_koszt_pracodawcy)
