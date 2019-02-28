liczba_wyrazow = []
wyrazy = []
szesciany = []

with open("ciagi.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            liczba_wyrazow.append(int(line.strip()))
        else:
            array = line.split()
            for x in array:
                wyrazy.append(int(x))

index = 0
liczba_arytmet = 0
max_roznica = float("-inf")

for x in liczba_wyrazow:
    r = set()
    for y in range(0, x-1):
        r.add(wyrazy[index + y + 1] - wyrazy[index + y])
    if len(r) == 1:
        liczba_arytmet += 1
        if max(r) > max_roznica:
            max_roznica = max(r)
    index += x

index = 0
for x in liczba_wyrazow:
    max_szescian = float("-inf")
    for y in range(0, x):
        temp = round(wyrazy[index + y] ** (1./3.))
        potega = temp**3
        if potega == wyrazy[index + y] and temp > max_szescian:
            max_szescian = wyrazy[index + y]
    if max_szescian > 0:
        szesciany.append(max_szescian)
    index += x

liczba_wyrazow_blednych = []
wyrazy_bledne = []

with open("bledne.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            liczba_wyrazow_blednych.append(int(line.strip()))
        else:
            array = line.split()
            for x in array:
                wyrazy_bledne.append(int(x))
index = 0
fejk_wyrazy = []
for x in liczba_wyrazow_blednych:
    roznice = []
    for y in range(0, x-1):
        temp = wyrazy_bledne[index+y+1] - wyrazy_bledne[index+y]
        roznice.append(temp)
    
    if roznice[0] != roznice[1] and roznice[1] == roznice[2]:
        fejk_wyrazy.append(wyrazy_bledne[0 + index])
    elif roznice[0] != roznice[1] and roznice[1] != roznice[2] and roznice[2] == roznice[3]:
        fejk_wyrazy.append(wyrazy_bledne[1 + index])
    else:
        for i in range(0, x-1):
            if roznice[i] != roznice[0]:
                fejk_wyrazy.append(wyrazy_bledne[i+1 + index])
    index += x

with open("wyniki1.txt", "w") as file:
    file.write("61.1\nTyle ciagow arytmetycznych: {}\n".format(liczba_arytmet))
    file.write("Maksymalna roznica: {}\n\n".format(max_roznica))
    file.write("61.2\nNajwieksze pelne szesciany: {}\n\n".format(szesciany))
    file.write("61.3\nBledne wyrazy: {}\n".format(fejk_wyrazy))