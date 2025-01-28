from zadanie_numerki.system_kolejkowy.kolejka import Kolejka
from zadanie_numerki.system_kolejkowy.klient import Klient

class System:
    def __init__(self, historia):
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
            print(f"Nieznana kategorai: {kategoria}")

    def obsluz_klienta(self, kategoria):
        if self.kolejki[kategoria].is_empty():
            return None

        klient = self.kolejki[kategoria].dequeue()
        czas_obslugi = aktualny_czas - klient.czas_przybycia
        self.historia[kategoria].append(czas_obslugi)

    def akutalny_stan(self):
        return {
            'A': self.kolejki['A'].size(),
            'B': self.kolejki['B'].size(),
            'C': self.kolejki['C'].size(),
            'D': self.kolejki['D'].size()
        }

    def statystyki(self):
        staty = {}
        for kat, czasy in self.historia.items():
            if len(czasy) == 0:
                staty[kat] = 0
            else:
                staty[kat] = sum(czasy) / len(czasy)
        return staty
