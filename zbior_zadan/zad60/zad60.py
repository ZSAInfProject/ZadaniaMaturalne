from math import sqrt

def zadanie60(f):
    liczby = []
    mniej1000 = []

    liczby = f.read().splitlines()

    for index, liczba in enumerate(liczby):
        liczby[index] = int(liczba)
        
    for liczba in liczby:
        if liczba < 1000:
            mniej1000.append(liczba)

    with open("wyniki.txt", "w") as file:
        file.write("60.1\n")

    for liczba in liczby:
        dzielniki = [1]
        czynnik = 3
        root = int(sqrt(liczba)) + 1
        if liczba % 2 == 0:
            dzielniki.append(2)
            dzielniki.append(liczba/2)
        while czynnik <= root:
            if not liczba % czynnik:
                dzielniki.append(czynnik)
                second = int(liczba/czynnik)
                if second != root:
                    dzielniki.append(second)
            if 2 not in dzielniki:
                czynnik += 2
            else:
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
        file.write("Najwieksza wzglednie pierwsza: {}".format(maksimum))