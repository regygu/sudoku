from SUD_new import random_map
import random
import copy

map = random_map()
blist = [[], [], [], [], [], [], [], [], []]
check_map = copy.deepcopy(map)


def print_map():
    print(map[0][0], map[0][1], map[0][2], "|", map[0][3], map[0][4], map[0][5], "|", map[0][6], map[0][7], map[0][8])
    print(map[1][0], map[1][1], map[1][2], "|", map[1][3], map[1][4], map[1][5], "|", map[1][6], map[1][7], map[1][8])
    print(map[2][0], map[2][1], map[2][2], "|", map[2][3], map[2][4], map[2][5], "|", map[2][6], map[2][7], map[2][8])
    print("----- + " * 2 + "-----")
    print(map[3][0], map[3][1], map[3][2], "|", map[3][3], map[3][4], map[3][5], "|", map[3][6], map[3][7], map[3][8])
    print(map[4][0], map[4][1], map[4][2], "|", map[4][3], map[4][4], map[4][5], "|", map[4][6], map[4][7], map[4][8])
    print(map[5][0], map[5][1], map[5][2], "|", map[5][3], map[5][4], map[5][5], "|", map[5][6], map[5][7], map[5][8])
    print("----- + " * 2 + "-----")
    print(map[6][0], map[6][1], map[6][2], "|", map[6][3], map[6][4], map[6][5], "|", map[6][6], map[6][7], map[6][8])
    print(map[7][0], map[7][1], map[7][2], "|", map[7][3], map[7][4], map[7][5], "|", map[7][6], map[7][7], map[7][8])
    print(map[8][0], map[8][1], map[8][2], "|", map[8][3], map[8][4], map[8][5], "|", map[8][6], map[8][7], map[8][8])


def difficulty():
    x, y = 0, 0
    print()
    number = input("Válasszon nehézségi szintet: Könnyű [1] / Közepes [2] / Nehéz [3] ")
    if number == "1":
        x, y = 4, 5
    elif number == "2":
        x, y = 6, 7
    elif number == "3":
        x, y = 8, 9
    else:
        print("Hibás bevitel, de sebaj...próbáld újra!")
        difficulty()

    for j in range(9):
        for i in range(random.randint(x, y)):
            a = random.choice(map[j])
            blist[j].append(a)
    for j in range(9):
        for i in range(9):
            if map[j][i] in blist[j]:
                map[j][i] = " "
    print()


def main():
    print()
    list_one_ten = range(1, 10)
    choose = input("Válasszon: I = Bevitel / D = Törlés / C = Ellenőrzés / R = Játékszabály /E = Kilépés -> ")
    print()

    if choose == "I":
        while True:
            try:
                chose_I = input("Írja be az oszlop számát(1-9), sor számát(1-9), és a behelyettesíteni kívánt számot(1-9): ")
                chose_I_list = chose_I.split(' ')
                if len(chose_I_list) == 3:
                    print("Bevitel...")
                else:
                    print("Valamelyik karakter nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
                try:
                    a = int(chose_I_list[0])
                    b = int(chose_I_list[1])
                    c = int(chose_I_list[2])
                except ValueError or IndexError or SyntaxError:
                    print("Valamelyik karakter nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
                if a in list_one_ten or b in list_one_ten or c in list_one_ten:
                    a -= 1
                    b -= 1
                    break
                else:
                    print("Valamelyik karakter nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
            except ValueError or IndexError or AttributeError:
                print("Ez nem egy szám vagy hiányos a bevitel!")
                print("")
                print_map()
                main()
        d = str(c)
        if map[b][a] == " ":
            map[b][a] = "\033[34m" + d + "\033[0m"
        else:
            print("Ez a szám nem módosítható!")

    elif choose == "D":
        while True:
            try:
                chose_D = input("Írja be az oszlop számát(1-9) és a sor számát(1-9) szóközzel elválasztva: ")
                chose_D_list = chose_D.split(' ')
                if len(chose_D_list) == 2:
                    print("Törlés folyamatban...")
                else:
                    print("Valamelyik karakter nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
                try:
                    a = int(chose_D_list[0])
                    b = int(chose_D_list[1])
                except ValueError or IndexError or AttributeError:
                    print("Valamelyik karakter nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
                if a in list_one_ten and b in list_one_ten:
                    a -= 1
                    b -= 1
                    break
                else:
                    print("Ez nem a megadott intervallumban található szám!")
                    print("")
                    print_map()
                    main()
            except ValueError:
                print("Ez nem egy szám!")
                print("")
                print_map()
                main()
        if map[b][a] == " ":
            print("Innen nincs mit törölni!")
        elif isinstance(map[b][a], str):
            map[b][a] = " "
        else:
            print("Ez a szám nem törölhető!")

    elif choose == "R":
        print(25 * " " + "JÁTÉKSZABÁLY \n A 9x9-es tábla összes sorába és oszlopába írd be a számokat 1-9-ig úgy, \n hogy minden szám csak egyszer szerepelhet soronként vagy oszloponként. \n A nagy négyzetrács további 3x3-as négyzeteiben is csak egyszer szerepelhet egy szám.")

    elif choose == "C":
        mapcopy = copy.deepcopy(map)
        for i in range(9):
            for j in range(9):
                if mapcopy[i][j] == " ":
                    print("Valami még biztosan hibás, vagy hiányzik. Ellenőrizd és javítsd ki a hibát!")
                    main()
                elif isinstance(mapcopy[i][j], str):
                    mapcopy[i][j] = int(mapcopy[i][j].strip("\033[34m\033[0m\x1b[34m\x1b[0m "))
        if mapcopy == check_map:
            print("Gratulálok, nyertél!")
        else:
            print("Valami még biztosan hibás, vagy hiányzik. Ellenőrizd és javítsd ki a hibát!") 

    elif choose == "E":
        exit()
    else:
        print("Ez a karakter nem szerepel a lehetőségek között. Próbáld újra!")
    print()
    print_map()
    print()
    main()

difficulty()
print_map()
main()
