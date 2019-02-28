import math

lines1 = []
lines2 = []
lines3 = []
temps1 = []
temps2 = []
temps3 = []
hours1 = []
hours2 = []
hours3 = []

with open("dane_systemy1.txt", "r") as file:
    lines1 = file.readlines()

with open("dane_systemy2.txt", "r") as file:
    lines2 = file.readlines()

with open("dane_systemy3.txt", "r") as file:
    lines3 = file.readlines()

for x in lines1:
    temps1.append(int(x.split(" ")[1], 2))
    hours1.append(int(x.split(" ")[0], 2))

for x in lines2:
    temps2.append(int(x.split(" ")[1], 4))
    hours2.append(int(x.split(" ")[0], 4))

for x in lines3:
    temps3.append(int(x.split(" ")[1], 8))
    hours3.append(int(x.split(" ")[0], 8))

minimum1 = float("inf")
minimum2 = float("inf")
minimum3 = float("inf")

for x in temps1:
    if x < minimum1:
        minimum1 = x

for x in temps2:
    if x < minimum2:
        minimum2 = x

for x in temps3:
    if x < minimum3:
        minimum3 = x

najnizsza1 = format(minimum1, 'b')
najnizsza2 = format(minimum2, 'b')
najnizsza3 = format(minimum3, 'b')

counter = 0

for x, hour in enumerate(hours1):
    if (hour - 12) % 24 is not 0:
        if (hours2[x] - 12) % 24 is not 0:
            if (hours3[x] - 12) % 24 is not 0:
                counter += 1

minimum1_2 = float("-inf")
minimum2_2 = float("-inf")
minimum3_2 = float("-inf")

rekordy = []

for index, temp in enumerate(temps1):
    if minimum1_2 < temp:
        minimum1_2 = temp
        rekordy.append(index)

for index, temp in enumerate(temps2):
    if minimum2_2 < temp:
        minimum2_2 = temp
        rekordy.append(index)

for index, temp in enumerate(temps3):
    if minimum3_2 < temp:
        minimum3_2 = temp
        rekordy.append(index)

record_set = set(rekordy)
dni_rekordowe = len(record_set)

start = 1
max_skok = float("-inf")

for i in range(0, len(temps1) - 1):
    for j in range(start, len(temps1)):
        r = float(pow(temps1[i] - temps1[j], 2))
        skok = math.ceil(r / abs(i - j))
        if skok > max_skok:
            max_skok = skok
    start += 1

plik = open("systemy_wyniki.txt", "w")

plik.write("58.1\n")
plik.write("Najnizsza temp w stacji 1: {}\n".format(najnizsza1))
plik.write("Najnizsza temp w stacji 2: {}\n".format(najnizsza2))
plik.write("Najnizsza temp w stacji 3: {}\n\n".format(najnizsza3))
plik.write("58.2\n")
plik.write("Tyle razy zegar byl niepoprawny w kazdej stacji: {}\n\n".format(counter))
plik.write("58.3\n")
plik.write("Liczba dni rekordowych: {}\n\n".format(dni_rekordowe))
plik.write("58.4\n")
plik.write("Najwiekszy skok temperatury w stacji S1: {}".format(max_skok))

plik.close()