from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalva = {}

    def foglal(self, datum):
        if datum in self.foglalva:
            print("Ez a szoba már foglalt ezen a napon.")
            return False
        else:
            self.foglalva[datum] = True
            return True

    def lemond(self, datum):
        if datum in self.foglalva:
            del self.foglalva[datum]
            print("A foglalás sikeresen törölve.")
        else:
            print("Ezen a napon nincs foglalás a szobára.")

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szoba.foglal(datum):
                    print(f"A {szobaszam} szoba foglalása {datum}-ra sikeres. Ár: {szoba.ar} Ft.")
                    return szoba.ar
                else:
                    print(f"A {szobaszam} szoba már foglalt ezen a napon.")
                    return None
        print(f"A {szobaszam} szoba nem található a szállodában.")
        return None

    def foglalas_lemondas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                szoba.lemond(datum)
                return
        print(f"A {szobaszam} szoba nem található a szállodában.")

    def listaz_foglalasok(self):
        print(f"Foglalások a(z) {self.nev} szállodában:")
        for szoba in self.szobak:
            print(f"  Szoba {szoba.szobaszam}:")
            for datum in szoba.foglalva:
                print(f"    - {datum}: {szoba.ar} Ft")

hotel = Szalloda("Példa Hotel")
hotel.add_szoba(EgyagyasSzoba("101"))
hotel.add_szoba(EgyagyasSzoba("102"))
hotel.add_szoba(KetagyasSzoba("103"))
hotel.add_szoba(KetagyasSzoba("104"))

# Interfész
while True:
    print("\nVálassz egy műveletet:")
    print("1. Egyágyas szoba foglalása")
    print("2. Kétágyas szoba foglalása")
    print("3. Lemondás")
    print("4. Foglalások listázása")
    print("0. Kilépés")

    valasztas = input("Választott művelet: ")

    if valasztas == "1" or valasztas == "2":  # Foglalás
        if valasztas == "1":
            szobaszam = input("Add meg az egyágyas szoba számát: ")
        else:
            szobaszam = input("Add meg a kétágyas szoba számát: ")
        
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")

        try:
            foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
            if foglalas_datum < datetime.now():
                print("Csak jövőbeli foglalás lehetséges.")
                continue
        except ValueError:
            print("Hibás dátum formátum. Kérlek, próbáld újra.")
            continue

        hotel.foglalas(szobaszam, datum)

    elif valasztas == "3":  # Lemondás
        szobaszam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
        datum = input("Add meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")

        hotel.foglalas_lemondas(szobaszam, datum)

    elif valasztas == "4":  # Foglalások listázása
        hotel.listaz_foglalasok()

    elif valasztas == "0":  # Kilépés
        break

    else:
        print("Nem megfelelő választás. Kérlek, válassz egy számot a felsoroltak közül.")
