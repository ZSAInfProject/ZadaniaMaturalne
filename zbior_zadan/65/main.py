from math import gcd

with open("dane_ulamki.txt", "r") as file:
    ulamki = file.read().splitlines()

for index, ulamek in enumerate(ulamki):
    ulamki[index] = ulamek.split()

minimum = float("inf")
min_licznik = float("inf")
min_mianownik = float("inf")

for ulamek in ulamki:
    if minimum > (int(ulamek[0])/int(ulamek[1])):
        minimum = int(ulamek[0])/int(ulamek[1])
        min_licznik = int(ulamek[0])
        min_mianownik = int(ulamek[1])
    elif minimum == (int(ulamek[0])/int(ulamek[1])):
        if min_mianownik > int(ulamek[1]):
            min_mianownik = int(ulamek[1])
            min_licznik = int(ulamek[0])

with open("wyniki.txt", "w") as file:
    file.write("65.1: {} {}\n".format(min_licznik, min_mianownik))

nieskracalne = 0

for ulamek in ulamki:
    if gcd(int(ulamek[0]), int(ulamek[1])) == 1:
        nieskracalne += 1

with open("wyniki.txt", "a") as file:
    file.write("65.2: {}\n".format(nieskracalne))

suma_licznikow = 0

for ulamek in ulamki:
    while gcd(int(ulamek[0]), int(ulamek[1])) != 1:
        divisor = gcd(int(ulamek[0]), int(ulamek[1]))
        ulamek[0] = int(ulamek[0]) / divisor
        ulamek[1] = int(ulamek[1]) / divisor
    suma_licznikow += int(ulamek[0])

with open("wyniki.txt", "a") as file:
    file.write("65.3: {}\n".format(suma_licznikow))

suma_ulamkow = 0

for ulamek in ulamki:
    temp = int(ulamek[0])
    temp = temp*2*2*3*3*5*5*7*7*13
    temp = temp/int(ulamek[1])
    suma_ulamkow += temp

with open("wyniki.txt", "a") as file:
    file.write("65.4: {}".format(int(suma_ulamkow)))