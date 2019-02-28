def zadanie60():
    liczby = []

    mniej1000 = []

    with open("liczby.txt", "r") as file:
        liczby = file.read().splitlines()

    for index, liczba in enumerate(liczby):
        liczby[index] = int(liczba)
        
    for liczba in liczby:
        if liczba < 1000:
            mniej1000.append(liczba)

    with open("wyniki.txt", "w") as file:
        file.write("60.1\n")

    for liczba in liczby:
        dzielniki = [1]
        czynnik = 2
        while czynnik <= liczba/2:
            if liczba % czynnik == 0:
                dzielniki.append(czynnik)
            czynnik += 1
        dzielniki.append(liczba)
        if len(dzielniki) == 18:
            with open("wyniki.txt", "a") as file:
                file.write(("Liczba {}: {}\n".format(liczba, dzielniki)))

    maksimum = float("-inf")

    def nwd(x, y):
        if x < y:
            return nwd(y,x)
        if y == 0:
            return x
        return nwd(y, x%y)

    for i in range(0, 200):
        ok = True
        for j in range(0, 200):
            if i != j and nwd(liczby[i], liczby[j]) > 1:
                ok = False
        if ok and liczby[i] > maksimum:
            maksimum = liczby[i]

    with open("wyniki.txt", "a") as file:
        file.write("\n60.2\n")
        file.write("Ilosc liczb mniejszych od 1000: {}\n".format(len(mniej1000)))
        file.write("Dwie ostatnie liczby mniejsze od 1000: {}, {}\n\n".format(mniej1000[len(mniej1000)-1], mniej1000[len(mniej1000)-2]))
        file.write("60.3\n")