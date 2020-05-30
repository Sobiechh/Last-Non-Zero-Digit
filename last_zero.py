import glob  # sciezki do plikow
import random
import datetime as dt

files_path = "in/"

for i in range(10):
    file = files_path + str(i) + ".txt"
    with open(file, 'w') as in_:
        prawd = random.randint(0, 100)
        range_ = random.randint(1, 20)
        in_.write(str(range_) + '\n')
        if prawd > 15:
            for i in range(range_):
                in_.write(str(random.randint(1, 1000)) + '\n')
        else:
            for i in range(random.randint(1, 5)):
                in_.write(str(random.randint(1, 100)) + '\n')

time = dt.datetime.now()
time_in = time.strftime('%Y-%m-%d %H:%M:%S')

dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]


def lastNon0Digit(n):  # funkcja sprawdzająca ostatnią niezerowa cyfre silni
    if n < 10:
        return dig[n]
    if ((n // 10) % 10) % 2 == 0:
        return (6 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
    else:
        return (4 * lastNon0Digit(n // 5) * dig[n % 10]) % 10
    return 0


files_path = "in/*.txt"  # sciezka do plikow in

files_in = glob.glob(files_path)  # przechowuje wszystkie nazwy folderow .txt w folderze in
files_out = []

for name in files_in:
    files_out.append("out" + name[2:])  # przekopiowanie plikow z /in tylko zamiana na wyjscie /out

contents = []

for name in files_in:
    with open(name) as f:
        word = f.readlines()
        contents.append(word)
        f.close()

for i, list_of_numbers in enumerate(contents):  # dla kazdej z list znajdujacej sie w liscie contents
    for number in list_of_numbers:
        # walidacja
        try:
            int(number) #czy dane nie zostaly blednie wpisane  tj. czy sa typu int
        except ValueError as e:
            print(e)
            break

    # wypisywanie do plikow

    if int(list_of_numbers[:1][0]) != len(list_of_numbers[1:]): #sprawdzanie przypadku, z za mała ilością danych do testów
        with open(files_out[i], 'w') as out:
            out.write('Za malo danych')
    else:
        wynik = ""
        for number in list_of_numbers[1:]: #wykonywanie głownego algorytmu
            wynik += str(lastNon0Digit(int(number.strip()))) + ","
        with open(files_out[i], 'w') as out:
            out.write(wynik[:-1])