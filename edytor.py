from PIL import Image
from PIL import Image, ImageOps
from PIL import ImageFilter

import numpy as np
import sys
import time
import os

class edytorObrazow:
    def __init__(self):
        self.obraz = None
        self.oryginalny_obraz = None
##1. Wczytywanie
    def zaladuj_obraz(self, sciezka):
        try:
            self.obraz = Image.open(sciezka)
            self.oryginalny_obraz = self.obraz.copy()
            print("Obraz został wczytany.")
        except FileNotFoundError:
            print("Nie znaleziono pliku.")
##2. Zapisywanie
    def zapisz_obraz(self, sciezka):
        if self.obraz is not None:
            try:
                self.obraz.save(sciezka)
                print("Obraz został zapisany.")
                input("Otwieram zapisane zdjecie")
                os.system('start ' + sciezka)
            except:
                print("Wystąpił błąd podczas zapisywania obrazu.")
        else:
            print("Nie wczytano żadnego obrazu.")
##3. Podglad
    def pokaz_obraz(self):
        if self.obraz is not None:
            try:
                self.obraz.show()
            except:
                print("Nie wczytano żadnego obrazu.")
##4. Transformacja przestrzeni barw
    def przestrzen_barw(self):
        if self.obraz is not None:
            try:
                self.obraz = self.obraz.convert('RGB')
                print("Przekształcono przestrzeń barw.")
            except:
                print("Wystąpił błąd podczas przekształcania przestrzeni barw.")
        else:
            print("Nie wczytano żadnego obrazu.")
##5. Negatyw
    def negatyw(self):
        if self.obraz is not None:
            try:
                self.obraz = ImageOps.invert(self.obraz)
                print("Zastosowano negatyw.")
            except:
                print("Wystąpił błąd podczas stosowania negatywu.")
        else:
            print("Nie wczytano żadnego obrazu.")
##6. Binaryzacja
    def binaryzacja(self, wartosc):
        if self.obraz is not None:
            try:
                ##Konwersja do skali szarości
                self.obraz = self.obraz.convert('L')
                ##piksele ponizej wartosci $wartosc$, otrzymuja wartosc 0, powyzej niej otrzymuja wartosc 255
                self.obraz = self.obraz.point(lambda x: 0 if x < wartosc else 255, '1')
                print("Zastosowano binaryzację.")
            except:
                print("Wystąpił błąd podczas stosowania binaryzacji.")
        else:
            print("Nie wczytano żadnego obrazu.")
##7. Erozja
    def erozja(self):
        if self.obraz is not None:
            try:
                ##Filtr minimalny, wybiera najmniejsza wartosc piksela w oknie o rozmiarze 3
                self.obraz = self.obraz.filter(ImageFilter.MinFilter(3))
                print("Zastosowano erozję.")
            except:
                print("Wystąpił błąd podczas stosowania erozji.")
        else:
            print("Nie wczytano żadnego obrazu.")
##8. Otwarcie
    def otwarcie(self):
        if self.obraz is not None:
            try:
                self.obraz = self.obraz.filter(ImageFilter.MinFilter(3))
                self.obraz = self.obraz.filter(ImageFilter.MaxFilter(3))
                print("Zastosowano otwarcie.")
            except:
                print("Wystąpił błąd podczas stosowania otwarcia.")
        else:
            print("Nie wczytano żadnego obrazu.")
##9. Domknięcie
    def domkniecie(self):
        if self.obraz is not None:
            try:
                ##Filtr minimalny, maksymalny wybiera najmniejsza/ najwieksza wartosc piksela w oknie o rozmiarze 3
                self.obraz = self.obraz.filter(ImageFilter.MaxFilter(3))
                self.obraz = self.obraz.filter(ImageFilter.MinFilter(3))
                print("Zastosowano domknięcie.")
            except:
                print("Wystąpił błąd podczas stosowania domknięcia.")
        else:
            print("Nie wczytano żadnego obrazu.")
##10. Filtr
    def filtr(self, nazwa_filtru):
        if self.obraz is not None:
            try:
                if nazwa_filtru == 'rozmycie':
                    self.obraz = self.obraz.filter(ImageFilter.BLUR)
                elif nazwa_filtru == 'szczegolowosc':
                    self.obraz = self.obraz.filter(ImageFilter.DETAIL)
                elif nazwa_filtru == 'krawedz':
                    self.obraz = self.obraz.filter(ImageFilter.FIND_EDGES)
                elif nazwa_filtru == 'wyostrz':
                    self.obraz = self.obraz.filter(ImageFilter.SHARPEN)
                else:
                    print("Nieznany filtr.")
                    return
                print("Zastosowano filtr: {}".format(nazwa_filtru))
            except:
                print("Wystąpił błąd podczas stosowania filtru.")
        else:
            print("Nie wczytano żadnego obrazu.")
##11. Wyrównanie histogramu
    def histogram(self):
        if self.obraz is not None:
            try:
                self.obraz = ImageOps.equalize(self.obraz)
                print("Wyrównano histogram.")
            except:
                print("Wystąpił błąd podczas wyrównywania histogramu.")
        else:
            print("Nie wczytano żadnego obrazu.")
##12. Kompresja
    def kompresuj(self, jakosc):
        if self.obraz is not None:
            try:
                self.obraz.save("temp.jpg", "JPEG", jakosc=jakosc)
                self.obraz = Image.open("temp.jpg")
                print("Zastosowano kompresję.")
            except:
                print("Wystąpił błąd podczas kompresji.")
        else:
            print("Nie wczytano żadnego obrazu.")
##13. Wygładzanie
    def wygladz(self):
        if self.obraz is not None:
            try:
                self.obraz = self.obraz.filter(ImageFilter.SMOOTH)
                print("Zastosowano wygładzanie.")
            except:
                print("Wystąpił błąd podczas stosowania wygładzania.")
        else:
            print("Nie wczytano żadnego obrazu.")
##14. Pomoc
    def help(self):
        print("")
        print("1. Transformacja przestrzeni barw")
        print("2. Negatyw")
        print("3. Binaryzacja")
        print("4. Erozja")
        print("5. Otwarcie")
        print("6. Domknięcie")
        print("7. Filtr")
        print("8. Wyrównanie histogramu")
        print("9. Kompresja")
        print("10. Wygładzanie")
        print("Wybierz numer, a zobaczysz na czym polega dana operacja.")
        wybor = input()
        print("")

        match wybor:
            case '1':
                print("Transformacja przestrzeni barw w edycji zdjęć to proces zmiany przestrzeni barw z jednej na drugą w celu uzyskania pożądanego efektu końcowego. Przykładowo, jeśli zdjęcie zostało wykonane w przestrzeni barw Adobe RGB, a drukarka wymaga zdjęcia w przestrzeni barw sRGB, konieczna jest transformacja przestrzeni barw")
            case '2':
                print("Negatyw w edycji zdjęć to proces zmiany kolorów zdjęcia na przeciwne")
            case '3':
                print("Przeprowadzenie procesu binaryzacji polega na tym, aby obraz mający wiele poziomów szarości zmienić na obraz, którego piksele mają wyłącznie wartości i .")
            case '4':
                print("Erozja w edycji zdjęć to proces usuwania pikseli z obrazu. W wyniku erozji obraz staje się mniejszy i mniej szczegółowy. Polega na przyłożeniu elementu strukturalnego do każdego z pikseli i jeżeli któremuś elementowi o wartości 1 na obiekcie strukturalnym odpowiada wartość 0 na obrazie, wówczas piksel obrazu znajdujący się w tej samej pozycji co środek elementu strukturalnego otrzymuje wartość 0.")
            case '5':
                print("Otwarcie w edycji zdjęć to operacja morfologiczna polegająca na wykonaniu operacji dylatacji na obrazie, a następnie wykonaniu operacji erozji na wyniku dylatacji. Otwarcie jest często stosowane w celu usunięcia małych elementów z obrazu lub zmniejszenia rozmiaru obrazu.")
            case '6':
                print("Domknięcie w edycji zdjęć to operacja morfologiczna polegająca na wykonaniu operacji erozji na obrazie, a następnie wykonaniu operacji dylatacji na wyniku erozji. Domknięcie jest często stosowane w celu usunięcia małych elementów z obrazu lub zmniejszenia rozmiaru obrazu")
            case '7':
                print("Filtr w edycji zdjęć to narzędzie służące do modyfikacji obrazu poprzez zmianę jego właściwości. Filtry mogą zmieniać kolorystykę, nasycenie, kontrast, jasność i wiele innych parametrów.")
            case '8':
                print("Wyrównanie histogramu to sposób regulacji kontrastu o obrazie cyfrowym, który korzysta z histogramu. Polega na zastosowaniu transformacji do każdego piksela obrazu, a tym samym na uzyskaniu nowego obrazu w wyniku niezależnej operacji na każdym z pikseli")
            case '9':
                print("Kompresja obrazu to proces zmniejszania rozmiaru pliku obrazu.")
            case '10':
                print("Wygładzenie w edycji zdjęć to proces zmniejszania szumów na zdjęciu. Szumy to przypadkowe piksele, które pojawiają się na zdjęciu i mogą zniekształcać obraz.")
            case _:
                print("Bledny input!")
##O
    def o(self):
            print("")
            self.__wiadomosc = "Program stworzony przez: Michala Zebrowskiego. \n Wykorzystane moduly przy tworzeniu programu: \n -Pillow \n -numpy \n -sys \n -time \n -os"
            for char in self.__wiadomosc:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            print("")
            input("")

##Menu programu
def menu():
    print("1. Wczytaj obraz")
    print("2. Zapisz obraz")
    print("3. Podejrzyj obraz")
    print("4. Transformacja przestrzeni barw")
    print("5. Negatyw")
    print("6. Binaryzacja")
    print("7. Erozja")
    print("8. Otwarcie")
    print("9. Domknięcie")
    print("10. Filtr")
    print("11. Wyrównanie histogramu")
    print("12. Kompresja")
    print("13. Wygładzanie")
    print("14. Pomoc")
    print("15. O")
    print("0. Wyjście")
##Logo programu
def logo():
    print("$$$$$$$\  $$\                  $$\                     $$$$$$$$\      $$\ $$\   $$\                         ")
    print("$$  __$$\ $$ |                 $$ |                    $$  _____|     $$ |\__|  $$ |                        ")
    print("$$ |  $$ |$$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\        $$ |      $$$$$$$ |$$\ $$$$$$\    $$$$$$\   $$$$$$\  ")
    print("$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|  $$  __$$\       $$$$$\   $$  __$$ |$$ |\_$$  _|  $$  __$$\ $$  __$$\ ")
    print("$$  ____/ $$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |      $$  __|  $$ /  $$ |$$ |  $$ |    $$ /  $$ |$$ |  \__|")
    print("$$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$\ $$ |  $$ |$$ |      ")
    print("$$ |      $$ |  $$ |\$$$$$$  | \$$$$  |\$$$$$$  |      $$$$$$$$\\$$$$$$$ |$$ |  \$$$$  |\$$$$$$  |$$ |      ")
    print("\__|      \__|  \__| \______/   \____/  \______/       \________|\_______|\__|   \____/  \______/ \__|      ")
    print()
                                                                                                    

def main():
    edytor = edytorObrazow()
    logo()

    while True:
        menu()
        wybor = input("Wybierz operację: ")
        
        match wybor:
            case '1':
                sciezka = input("Podaj ścieżkę do pliku: ")
                edytor.zaladuj_obraz(sciezka)
            case '2':
                sciezka = input("Podaj ścieżkę do zapisu: ")
                edytor.zapisz_obraz(sciezka)
            case '3':
                edytor.pokaz_obraz()
            case '4':
                edytor.przestrzen_barw()
            case '5':
                edytor.negatyw()
            case '6':
                wartosc = int(input("Podaj próg binaryzacji: "))
                edytor.binaryzacja(wartosc)
            case '7':
                edytor.erozja()
            case '8':
                edytor.otwarcie()
            case '9':
                edytor.domkniecie()
            case '10':
                nazwa_filtru = input("Podaj nazwę filtru (rozmycie, szczegolowosc, krawedz, wyostrz): ")
                edytor.filtr(nazwa_filtru)
            case '11':
                edytor.histogram()
            case '12':
                jakosc = int(input("Podaj jakość kompresji (0-100): "))
                edytor.kompresuj(jakosc)
            case '13':
                edytor.wygladz()
            case '14':
                edytor.help()
            case '15':
                logo()
                edytor.o()
            case '0':
                print("Bye.")
                break
            case _:
                print("Nieprawidłowy wybór.")

        print()


if __name__ == '__main__':
    main()
