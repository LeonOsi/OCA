def najmniejsze(lista, x):
    """
    Funkcja zwracająca x najmniejszych elementów z listy lista.

    Args:
        lista (list): Lista zawierająca elementy do przeszukania.
        x (int): Liczba elementów do zwrócenia.

    Returns:
        list: Lista zawierająca x najmniejszych elementów z listy lista, posortowana rosnąco.
    """
    posortowane = sorted(lista, key=lambda sublist: sublist[0])
    return posortowane[:x]

def kNN(d, c, knn):
    """
    Algorytm k najbliższych sąsiadów (kNN) do przewidywania ceny samochodu.

    Args:
        d (list): Lista danych treningowych zawierających cechy samochodów.
        c (list): Lista cech samochodu, dla którego przewidujemy cenę.
        knn (int): Liczba najbliższych sąsiadów do uwzględnienia w algorytmie kNN.

    Returns:
        float: Przewidziana cena samochodu na podstawie algorytmu kNN.
    """
    data = d
    car = c

    k = knn
    distances = []
    for traincar in data:
        sum = 0
        for i in range(25):
            sum += (float(traincar[i]) - float(car[i]))**2
        distances.append([sum, traincar[-1]])
    listaK = najmniejsze(distances, k)

    proporcje = []
    wsumie = 0
    for i in listaK:
        wsumie += i[0]
    for i in listaK:
        p = i[0] / wsumie
        proporcje.append(p)
    approxcena = 0
    for i in range(len(proporcje)):
        approxcena += round(proporcje[i] * float(listaK[i][1]), 2)

    return approxcena
