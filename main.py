from system_kolejkowy import klient, kolejka, system
import random
import time
import uuid # generowanie unikalnych ID


system = system.System()
czas_symulacji = 0
max_czas = 60 #czas trwania symulacji w sekundach

while czas_symulacji < max_czas:
    if random.random() < 0.4: #40% sznas na nowego klineta
        kategoria = random.choice(["A", "B", "C", "D"])
        id_klienta = str(uuid.uuid4())[:8]  # generuje unikalne ID
        nowy_klient = klient.Klient(
            id=id_klienta,
            czas_przybycia=czas_symulacji,
            kategoria=kategoria
        )
        system.dodaj_klienta(kategoria, nowy_klient)



    # 20% szans na obsłużenie klienta
    for kat in ["A", "B", "C", "D"]:
        if random.random() < 0.2:
            system.obsluz_klienta(kat, czas_symulacji)

    if czas_symulacji % 5 == 0:
        print(f"\n--- Czas: {czas_symulacji}s ---")
        stan = system.akutalny_stan()
        for kat, rozmiar in stan.items():
            print(f"Kolejka {kat}: {rozmiar} klientów")

    czas_symulacji += 1
    time.sleep(1)
    
print("\n===Koniec symulacji ===")
statystyki = system.statystyki()
for kat, srednia in statystyki.items():
    print(f"Średni czas obsługi ({kat}): {srednia:.2f}s")



