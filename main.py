import getpass
import random


def z1():
    liczby = input("Wpisz liczby rozdzielone przecinkami: ").split(",")
    try:
        max_v = float(liczby[0])
        min_v = float(liczby[0])
        for liczba in liczby:
            liczba = float(liczba)
            max_v = liczba if liczba>max_v else max_v
            min_v = liczba if liczba<min_v else min_v
        print(f"Max: {max_v}")
        print(f"Min: {min_v}")
    except ValueError:
        print("Niepoprawne dane")
        SystemExit

def z2():
    Miasta = '''Warszawa
Kraków
Łódź
Wrocław
Poznań
Gdańsk
Szczecin
Bydgoszcz
Lublin
Białystok'''.split("\n")
    print("Plan wycieczki:")
    i=1
    while Miasta:
        rand_val = random.randint(0,len(Miasta)-1)
        print(f"{i}. {Miasta[rand_val]}")
        i+=1
        Miasta.remove(Miasta[rand_val])

def z3():

    global player2, player1, typ_gry, ilosc_rund
    poprawneDane = False
    while not poprawneDane:
        ilosc_rund = input("Wpisz ilość rund: ")
        typ_gry = input("Wpisz typ gry.\n komputer(wpisz 1) / 2 graczy(wpisz 2): ")
        player1 = input("Wpisz Imię "+("pierwszego gracza"if typ_gry=="2" else "komputera")+"(wpisz '_n' żeby nie nazywać graczy): ")
        if player1 == '_n':
            player1 = "player1" if typ_gry=="2" else "Komputer"
            player2 = "player2" if typ_gry=="2" else "player"
        else:
            player2 = input("Wpisz Imię " + ("drugirgo gracza: " if typ_gry=="2" else "gracza"))
        if(not ilosc_rund.isdigit() or (typ_gry!="1" and typ_gry!="2")):
            poprawneDane = False
            print("Niepoprawne dane.")
        else:
            poprawneDane = True
    runda = 1
    znaki = {'p':"Papier",'n':"Nożyce",'k':"Kamień"}
    wyniki = []#index=runda-1, val = 1 or 2 (players) 0 - remis
    while runda<=int(ilosc_rund):
        print("Runda "+ str(runda))
        runda+=1
        for znak_key in znaki.keys():
            print(f"{znaki[znak_key]} (Wpisz {znak_key})")
        if typ_gry=="2":
            p1 = getpass.getpass(f"{player1}: ")
            p2 = getpass.getpass(f"{player2}: ")
            print(f"{player1}: {znaki[p1]}")
            print(f"{player2}: {znaki[p2]}")
        else:
            p1 = input(player2+": ")
            p2 = list(znaki)[random.randint(0,2)]
            print(f"{player1}: {znaki[p2]}")
        if p1=='p':
            if p2=='n':
                wyniki.append(2)
            elif p2=='k':
                wyniki.append(1)
            else:
                wyniki.append(0)
        elif p1=='n':
            if p2=='n':
                wyniki.append(0)
            elif p2=='k':
                wyniki.append(2)
            else:
                wyniki.append(1)
        else:
            if p2=='n':
                wyniki.append(1)
            elif p2=='k':
                wyniki.append(0)
            else:
                wyniki.append(2)
        print('')

    for i in range(len(wyniki)):
        print(f"Runda {i}: "+(player1 if wyniki[i]==1 else player2 if wyniki[i]==2 else 'Remis'))

if __name__ == '__main__':
    #z1()
    #z2()
    z3()