from math import sqrt

liczby = []

trzy_czynniki = 0

with open("liczby.txt") as file:
    liczby = file.readlines()

for index, liczba in enumerate(liczby):
    liczby[index] = int(liczba, 10)

nr_liczby = 1

for liczba in liczby:
    rozklady = 0
    rozklad = 3
    temp_liczba = liczba

    print("Liczba nr: {}".format(nr_liczby))

    while rozklad <= int(liczba/2) and liczba % 2 != 0 and temp_liczba > 1:
        if rozklad > int(sqrt(liczba)) and rozklady == 0:
            break
        if temp_liczba % rozklad == 0:
            rozklady += 1
            while temp_liczba % rozklad == 0:
                temp_liczba /= rozklad
            if rozklady > 3:
                break
            rozklad = 1
        rozklad += 2

    nr_liczby += 1

    if rozklady == 3:
        trzy_czynniki += 1

with open("wyniki.txt", "w") as file:
    file.write("59.1:\n")
    file.write("Trzy rozne czynniki, z ktorych kazdy jest nieparzysty, wystapily tyle razy: {}\n\n".format(trzy_czynniki))
        