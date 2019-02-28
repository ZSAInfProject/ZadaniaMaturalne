with open("liczby1.txt", "r") as file:
    liczby_oct = file.read().splitlines()

with open("liczby2.txt", "r") as file:
    liczby_dec = file.read().splitlines()

converted_oct = []
converted_dec = []

for liczba in liczby_oct:
    converted_oct.append(int(liczba, 8))

for liczba in liczby_dec:
    converted_dec.append(int(liczba))

minimum = float("inf")
maksimum = float("-inf")

for liczba in converted_oct:
    if liczba < minimum:
        minimum = liczba
    if liczba > maksimum:
        maksimum = liczba

longest_series = 0
current_series = 0
first_element = 0

for index in range(0, len(converted_dec)-1):
    if converted_dec[index+1] >= converted_dec[index]:
        current_series += 1
    else:
        if current_series > longest_series:
            longest_series = current_series + 1
            first_element = converted_dec[index-current_series]
        current_series = 0

same_value = 0
bigger_octal = 0

for index in range(0, len(converted_dec)):
    if converted_dec[index] == converted_oct[index]:
        same_value += 1
    elif converted_oct[index] > converted_dec[index]:
        bigger_octal += 1

octal_from_dec = []
devils_counter_dec = 0
devils_counter_oct = 0

for liczba in converted_dec:
    octal_from_dec.append(format(liczba, 'o'))
    temp = str(liczba)
    if temp.count('6') != 0:
        devils_counter_dec += temp.count('6')

for liczba in octal_from_dec:
    temp = str(liczba)
    if temp.count('6') != 0:
        devils_counter_oct += temp.count('6')

with open("wyniki.txt", "w") as file:
    file.write("62.1\n")
    file.write("Maksimum: {}, minimum: {}\n\n".format(format(maksimum, 'o'), format(minimum, 'o')))
    file.write("62.2\n")
    file.write("Pierwszy element: {}, najdluzszy ciag ma tyle wyrazow: {}\n\n".format(first_element, longest_series))
    file.write("62.3\n")
    file.write("Tyle samo wierszy ma taka sama wartosc: {}, tyle wierszy w liczby2 jest wiekszych: {}\n\n".format(same_value, bigger_octal))
    file.write("62.4\n")
    file.write("W zapisie dziesietnym 6 wystepuje tyle razy: {}, a w oktalnym dodatkowo: {} razy".format(devils_counter_dec, devils_counter_oct))