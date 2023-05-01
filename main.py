## NB 2023-05-03    Adatelemzés

def adatkinyeres ():
    with open("utonevkonyv.txt", "r") as utonev:
        vezeteknevek_lista = []
        for sor in utonev:
            sor_elemek = sor.strip().split(" ")
            nev = sor_elemek[0]
            datumok = []
            for elem in sor_elemek[1:]:
                if len(elem) == 6 and elem.isdigit():   # szám-e
                    datumok.append(elem)
            if len(datumok) > 0:
                for datum in datumok:
                    vezeteknevek_lista.append((nev, datum))
                    print("{:s} - {:s}".format(datum, nev))
            else:
                szoveg = " ".join(sor_elemek[1:])
                print("{:s} - {:s}".format(nev, szoveg))


adatkinyeres()