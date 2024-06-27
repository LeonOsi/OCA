from collections import defaultdict

datain = []

# Wczytanie danych z pliku 'imports-85.data' i zapisanie ich do listy datain
with open('imports-85.data', 'r') as file:
    for line in file:
        line = line.strip().split(',')
        datain.append(line)

dataout = datain
data = datain.copy()

def handleData(inp):
    """
    Przetwarza wejściowy string inp na listę, wykonuje numeryzację atrybutów klasowych
    i dokonuje przekształceń na podstawie danych z pliku 'imports-85.data'.

    Args:
        inp (str): Wejściowy string zawierający dane do przetworzenia.

    Returns:
        tuple: Krotka zawierająca dwie listy:
            - dataout: Zaktualizowana lista danych wyjściowych bez brakujących wartości.
            - output: Przetworzona lista danych wejściowych inp.
    """
    stripped_string = inp.strip("[]")
    list_of_strings = stripped_string.split(', ')
    inpucik = [elem.strip("'") for elem in list_of_strings]
    print(inpucik)

    for klasa in range(25):
        if True:
            srednie_ceny = defaultdict(list)

            # Obliczenie średnich cen dla każdej marki samochodu
            for samochod in datain:
                if samochod[klasa] == "dohcv":
                    samochod[klasa] = "dohc"
                marka = samochod[klasa]
                cena = samochod[-1]

                try:
                    cena_float = float(cena)
                    srednie_ceny[marka].append(cena_float)
                except ValueError:
                    continue

            # Obliczenie średnich cen i przekształcenie ich na skalę od 0 do 100
            for marka, ceny in srednie_ceny.items():
                srednia_cena = sum(ceny) / len(ceny)
                srednie_ceny[marka] = srednia_cena

            posortowane_marki = sorted(srednie_ceny.items(), key=lambda x: x[1])

            nowa_lista = []

            max = posortowane_marki[-1][1]

            # Utworzenie nowej listy z przekształconymi wartościami
            for marka, srednia_cena in posortowane_marki:
                wartosc = round(srednia_cena / max * 100, 2)
                nowa_lista.append([marka, wartosc])

            # Aktualizacja danych wyjściowych dataout
            for row in dataout:
                marka = row[klasa]
                for i in nowa_lista:
                    if i[0] == marka:
                        row[klasa] = i[1]
                        break

            # Aktualizacja danych wejściowych inpucik
            marka = inpucik[klasa]
            found = False
            for i in nowa_lista:
                if i[0] == marka:
                    inpucik[klasa] = i[1]
                    found = True
                    break
            if marka != "?" and not (found):
                for i in nowa_lista:
                    min = 9999999999
                    app_nowa_lista = None
                    for j in nowa_lista:
                        if float(j[0]) - float(inpucik[klasa]) < min:
                            min = float(j[0]) - float(inpucik[klasa])
                            app_nowa_lista = j[1]
                    inpucik[klasa] = app_nowa_lista
            if marka == "?":
                inpucik[klasa] = 50

    output = inpucik.copy()
    print(output)

    # Usunięcie wierszy z brakującymi wartościami z dataout
    i = 0
    while i < len(dataout):
        if dataout[i][-1] == '?':
            dataout.pop(i)
        else:
            i += 1

    return dataout, output
