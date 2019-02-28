liczby = []

with open("liczby.txt") as file:
    liczby = file.readlines()

for index, liczba in enumerate(liczby):
    liczby[index] = int(liczba, 10)

liczby_rev = []

for liczba in liczby:
    liczby_rev.append(liczba + int(str(liczba)[::-1]))

ile_palindromow = 0

for liczba in liczby_rev:
    if str(liczba) == str(liczba)[::-1]:
        ile_palindromow += 1

with open("wyniki.txt", "a") as file:
    file.write("59.2:\n")
    file.write("Tyle jest palindromow: {}\n\n".format(ile_palindromow))