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



adatkinyeres()
darabszam()
kezdobetu_szamolo()