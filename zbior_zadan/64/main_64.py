obrazek = []
temp = []

with open("dane_obrazki.txt") as file:
    obrazek = file.read().splitlines()

index = 0
rewers = 0
biggest_ones = 0
temp = list(obrazek)

while index <= 4378:
    how_many_ones = 0
    how_many_zeros = 0
    
    for i in range(0, 20):
        temp[i+index] = temp[i+index][0:(len(temp[i+index])-1)]
        how_many_ones += temp[i+index].count('1')
        how_many_zeros += temp[i+index].count('0')
    index += 22
    if how_many_ones > how_many_zeros:
        rewers += 1
    if how_many_ones > biggest_ones:
        biggest_ones = how_many_ones

with open("wyniki.txt", "w") as file:
    file.write("64.1\n")
    file.write("Liczba rewersow: {}\n".format(rewers))
    file.write("Najwiecej jedynek: {}\n".format(biggest_ones))

index = 0
recursive = 0
first_recursive = True
picture = ""

while index <= 4378:

    first_quarter, second_quarter, third_quarter, fourth_quarter = ("","","","")

    for i in range(0,10):
        first_quarter += temp[i+index][0:10]
        second_quarter += temp[i+index][10:20]
    for i in range(10,20):
        third_quarter += temp[i+index][0:10]
        fourth_quarter += temp[i+index][10:20]

    if first_quarter == second_quarter == third_quarter == fourth_quarter:
        recursive += 1
        if first_recursive:
            for i in range(0,100,10):
                picture += first_quarter[i:i+10] + second_quarter[i:i+10] + "\n"
            for i in range(0,100,10):
                picture += third_quarter[i:i+10] + fourth_quarter[i:i+10] + "\n"
            first_recursive = False
    index += 22

with open("wyniki.txt", "a") as file:
    file.write("64.2\n")
    file.write("Liczba obrazkow rekurencyjnych: {}\n".format(recursive))
    file.write("Pierwszy obrazek rekurencyjny:\n{}\n".format(picture))
    file.write("64.4\n")

index = 0
poprawny = 0
naprawialny = 0
nienaprawialny = 0
najwiecej_bledow = 0

kord_kolumny = []
kord_rzedu = []
nr_obrazka = 1

while index <= 4378:
    wrong_row = 0
    wrong_column = 0
    for i in range(0,20):
        if not temp[i+index].count('1') % 2 == int(obrazek[i+index][-1]):
            wrong_row +=1
            kord_rzedu.append(i+1) 
    for j in range(0,20):
        temp_string = ""
        for x in range(0,20):
            temp_string += obrazek[x+index][j]
        if not temp_string.count('1') % 2 == int(obrazek[index + 20][j]):
            wrong_column += 1
            kord_kolumny.append(j+1)
             
    index += 22

    if wrong_column + wrong_row == 0:
        poprawny += 1
    elif (wrong_column == 1 and wrong_row < 2) or (wrong_column < 2 and wrong_row == 1):
        naprawialny += 1
        with open("wyniki.txt", "a") as file:
            if len(kord_kolumny) == 0:
                file.write("({}, {}, {})\n".format(nr_obrazka, kord_rzedu[0], "21"))
            elif len(kord_rzedu) == 0:
                file.write("({}, {}, {})\n".format(nr_obrazka, "21", kord_kolumny[0]))
            elif len(kord_kolumny) == 1 and len(kord_rzedu) == 1:
                file.write("({}, {}, {})\n".format(nr_obrazka, kord_rzedu[0], kord_kolumny[0]))
    elif (wrong_column >= 2) or (wrong_row >= 2):
        nienaprawialny +=1

    nr_obrazka += 1
    kord_rzedu = []
    kord_kolumny = []

    if wrong_column + wrong_row > najwiecej_bledow:
        najwiecej_bledow = wrong_column + wrong_row

with open("wyniki.txt", "a") as file:
    file.write("64.3\n")
    file.write("Liczba obrazkow poprawnych: {}\n".format(poprawny))
    file.write("Liczba obrazkow naprawialnych: {}\n".format(naprawialny))
    file.write("Liczba obrazkow nienaprawialnych: {}\n".format(nienaprawialny))
    file.write("Najwieksza liczba blednych bitow parzystosci: {}\n".format(najwiecej_bledow))