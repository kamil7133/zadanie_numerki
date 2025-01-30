import random
class Klient:
    def __init__(self, id, czas_przybycia, kategoria):
        self.id = id
        self.czas_przybycia = czas_przybycia
        self.kategoria = kategoria
        self.czas_obslugi = self.losuj_czas_obslugi()
    # każdy klient zajmuje inna ilosc czasu
    def losuj_czas_obslugi(self):
        if self.kategoria == "A": #szybki odbiór zamówienia
            return random.randint(2, 5)
        elif self.kategoria == "B": #doradztwo w zakupie
            return random.randint(5, 10)
        elif self.kategoria == "C": #serwis
            return random.randint(10, 20)
        elif self.kategoria == "D": #luźne pogaduchy
            return random.randint(15, 30)

    def __repr__(self):
        return f"klient {self.id} ({self.kategoria})"
