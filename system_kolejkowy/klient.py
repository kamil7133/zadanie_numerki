class Klient:
    def __init__(self, id, czas_przybycia, kategoria):
        self.id = id
        self.czas_przybycia = czas_przybycia
        self.kategoria = kategoria
    def __repr__(self):
        return f"klient {self.id} ({self.kategoria})"

    # każdy klient zajmuje inna ilosc czasu//do implementacji