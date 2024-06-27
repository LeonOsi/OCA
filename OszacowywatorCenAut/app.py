import tkinter as tk
from tkinter import messagebox
from main import kNN
from fileHandler import handleData


def start():
    # Przetworzenie danych wejściowych za pomocą funkcji handleData
    result = handleData(entry.get())
    d = result[0]
    c = result[1]

    # Wyświetlenie danych wejściowych c w celach diagnostycznych
    print(c)

    # Pobranie wartości k z pola tekstowego knn
    k_str = knn.get()

    # Sprawdzenie, czy wartość k jest liczbą całkowitą
    try:
        k = int(k_str)
    except ValueError:
        messagebox.showerror("Błąd", "Podaj liczbę całkowitą dla wartości k.")
        return

    # Wywołanie funkcji kNN i wyświetlenie wyniku w messageboxie
    szacowana_wartosc = kNN(d, c, k)
    messagebox.showinfo("OCA", f"Przewidywana cena samochodu: {szacowana_wartosc} $")


# Tworzenie głównego okna
root = tk.Tk()
root.title("Oszacowywator Ceny Auta")
root.geometry("800x300")

# Dodanie etykiety "Podaj wektor auta"
label = tk.Label(root, text="Podaj wektor auta:")
label.pack()

# Dodanie pola do wprowadzania tekstu dla wektora auta
entry = tk.Entry(root, width=100)
entry.pack()

# Dodanie etykiety "k:"
label2 = tk.Label(root, text="k:")
label2.pack()

# Dodanie pola do wprowadzania wartości k
knn = tk.Entry(root, width=10)
knn.pack()

# Dodanie przycisku "Oszacuj"
button = tk.Button(root, text="Oszacuj", command=start)
button.pack()

# Etykieta wynikowa (na potrzeby przyszłych rozszerzeń)
result_label = tk.Label(root, text="")
result_label.pack()

# Uruchomienie głównej pętli programu
root.mainloop()

# Pobranie wartości wektora auta po zamknięciu głównego okna
car = entry.get()
