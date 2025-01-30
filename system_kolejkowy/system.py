from zadanie_numerki.system_kolejkowy.kolejka import Kolejka
from zadanie_numerki.system_kolejkowy.klient import Klient

class System:
    def __init__(self):
        self.kolejki = {
            'A': Kolejka(),
            'B': Kolejka(),
            'C': Kolejka(),
            'D': Kolejka()
        }
        self.historia = {
            'A': [],
            'B': [],
            'C': [],
            'D': []
        }

    def dodaj_klienta(self, kategoria, klient):
        if kategoria in self.kolejki:
            self.kolejki[kategoria].enqueue(klient)
        else:
            print(f"Nieznana kategoria: {kategoria}")

    def obsluz_klienta(self, kategoria, aktualny_czas):
        if self.kolejki[kategoria].is_empty():
            return None

        klient = self.kolejki[kategoria].dequeue()
        czas_obslugi = aktualny_czas - klient.czas_przybycia #obliczenie czasu obslugi
        czas_zakonczenia = aktualny_czas + czas_obslugi # nowa logika czasu
        #zapisanie czasu trwania oblsugi
        self.historia[kategoria].append(czas_obslugi)

        #wyswietlanie komunikatu
        self.wyswietl_komunikat(klient, aktualny_czas, czas_zakonczenia)
        return klient
    def akutalny_stan(self):
        return {
            'A': self.kolejki['A'].size(),
            'B': self.kolejki['B'].size(),
            'C': self.kolejki['C'].size(),
            'D': self.kolejki['D'].size()
        }
    def wyswietl_komunikat(self, klient, start, koniec):
        kategorie_tekst = {
            'A': 'szybki odbiór zamówienia',
            'B': 'doradztwo w zakupie',
            'C': 'serwis',
            'D': 'luźne pogaduchy'
        }
        print(
            f"\n[+] Obsługa klienta {klient.id} "
            f"(kategoria {klient.kategoria} - {kategorie_tekst[klient.kategoria]}) "
            f"\n    Czas obsługi: {klient.czas_obslugi}s (zakonczenie: {koniec}s) "
        )
    def statystyki(self):
        staty = {}
        for kat, czasy in self.historia.items():
            if len(czasy) == 0:
                staty[kat] = 0
            else:
                staty[kat] = sum(czasy) / len(czasy)
        return staty
