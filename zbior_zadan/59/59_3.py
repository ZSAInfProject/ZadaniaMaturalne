liczby = []
moce_zbioru = [0, 0, 0, 0, 0, 0, 0, 0]

with open("liczby.txt") as file:
    liczby = file.read().splitlines()

minimum = float("inf")
maksimum = float("-inf")

for liczba in liczby:
    kopia = int(liczba)
    counter_kroki = 0
    liczba = int(liczba)
    while liczba >= 10:
        liczba = str(liczba)
        liczba_list = map(int, liczba)
        liczba = int(liczba)
        temp_wynik = 1
        for digit in liczba_list:
            temp_wynik *= digit
        liczba = temp_wynik
        counter_kroki += 1
    if counter_kroki <= 8:
        moce_zbioru[counter_kroki-1] += 1
        if counter_kroki == 1:
            if kopia < minimum:
                minimum = kopia
            if kopia > maksimum:
                maksimum = kopia

with open("wyniki.txt", "a") as file:
    file.write("59.3:\n")
    file.write("Moc 1: {}, Moc 2: {}, Moc 3: {}, Moc 4: {}, Moc 5: {}, Moc 6: {}, Moc 7: {}, Moc 8: {}\n"
    .format(moce_zbioru[0], moce_zbioru[1], moce_zbioru[2], moce_zbioru[3], moce_zbioru[4], moce_zbioru[5], moce_zbioru[6], moce_zbioru[7]))
    file.write("Maksimum: {}\n".format(maksimum))
    file.write("Minimum: {}\n".format(minimum))