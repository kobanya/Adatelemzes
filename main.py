## NB 2023-05-03    Adatelemzés

# az adott TXT fájl  beolvasása, darabolása és listába mentése
def adatkinyeres ():
    with open("utonevkonyv.txt", "r") as utonev:
        vezeteknevek_lista = []                       # lista definiálása
        for sor in utonev:                            # bejárás
            sor_elemek = sor.strip().split(" ")       # adatdarabolás
            nev = sor_elemek[0]                       # Az első elem a NÉV
            datumok = []                              # A dátumok kinyerése
            for elem in sor_elemek[1:]:
                if len(elem) == 6 and elem.isdigit():   # szám-e illetve 6 katkter hosszú-e
                    datumok.append(elem)                # listához adás
            if len(datumok) > 0:                        # ha hosszabb mint 0 karakter
                for datum in datumok:
                    vezeteknevek_lista.append((nev, datum))
                    print("{:s} - {:s}".format(datum, nev))
            else:
                szoveg = " ".join(sor_elemek[1:])        # egyéb szöveg
                print("{:s} - {:s}".format(nev, szoveg))

#  1. FELADAT  - Nevek megszámolása, ezonosságok kizárásaával
def darabszam():
    with open("utonevkonyv.txt", "r") as f:             # megnyitás olvasására
        nevek = []                                      # lista definiálása
        for sor in f:                                   # Bejárás
            sor_elemek = sor.strip().split(" ")         # darabolás
            nev = sor_elemek[0]                         # az első elem kiválasztása- 0 index
            if nev not in nevek:                        # ma még nincs a listában hozzáadod
                nevek.append(nev)
    print('------------------------------------------------')
    print("A különböző keresztnevek száma:", len(nevek), " darab")   # kiírom a darabszámot


def kezdobetu_szamolo():
    with open("utonevkonyv.txt", "r") as f:             # megnyitás olvasására
        kezdobetu_dict = {}                             # kezdőbetű szótár

        for sor in f:                                   # Bejárás, szeleteléssel
            sor_elemek = sor.strip().split(" ")         # szeletelés szúközzel

            if len(sor_elemek) >= 1:
                nev = sor_elemek[0]

                if len(nev) >= 1:
                    kezdobetu = nev[0]

                    if kezdobetu in kezdobetu_dict:
                        kezdobetu_dict[kezdobetu] += 1
                    else:
                        kezdobetu_dict[kezdobetu] = 1

        i = 0
        for kezdobetu, gyakorisag in kezdobetu_dict.items():                # kezdőbetű kiírása
            print("{:s} - {:d}\t".format(kezdobetu, gyakorisag), end=" ")

            i += 1
            if i == 9:                  #  soronként  9 elem
                print("")
                i = 0
def nincs_nevnap():
    osszes_nev = 0
    datum_nelkuli_nevek = 0

    with open("utonevkonyv.txt", "r") as f:
        for sor in f:
            sor_elemek = sor.strip().split(" ")
            if len(sor_elemek) == 1:
                osszes_nev += 1
                if not any(char.isdigit() for char in sor_elemek[0]):
                    datum_nelkuli_nevek += 1
            elif all(not elem.isdigit() for elem in sor_elemek):
                osszes_nev += 1
                datum_nelkuli_nevek += 1

    print('\n----------------------------------------------')
    print("\nAz összes név száma:", osszes_nev)
    print("Azon nevek száma, amelyeknek nincs névnapja:", datum_nelkuli_nevek)
    print("Azon nevek százaléka, amelyeknek nincs névnapja: {:.2f}%".format((datum_nelkuli_nevek/osszes_nev)*100))


def gorog_osi():
    with open("utonevkonyv.txt", "r") as f:
        nevek = []
        for sor in f:
            sor_elemek = sor.strip().split(":")
            nev = sor_elemek[0]
            leiras = " ".join(sor_elemek[1:])
            if "görög" in leiras or "ősi" in leiras:
                nevek.append(nev)
    print('\nA görög és ősi nevek :')
    print(",".join(nevek))

adatkinyeres()
darabszam()
kezdobetu_szamolo()
nincs_nevnap()
gorog_osi()


