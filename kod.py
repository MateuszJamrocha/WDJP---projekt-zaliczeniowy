import random
import csv

class Dataset:

    def __init__(self, file, kolumna_decyzyjna, headers:bool=False, ):
        """
        Konstruktor wczytuje dane i zapisuje do zmiennej data_list.
        Parametr kolumna_decyzyjna zawiera indeks kolumny z klasami decyzyjnymi.
        Parametr headers określa czy są etykiety w pliku.
        """
        self.data_list = []
        self.headers = []
        self.kolumna_decyzyjna = kolumna_decyzyjna

        if isinstance(file,str) and isinstance(kolumna_decyzyjna,int) and isinstance(headers,bool):
            with open(file, 'r', newline='') as file_reader:
                for linia in file_reader:
                        linia = linia.rstrip('\n').split(',')
                        self.data_list.append(linia)

            if headers == True:
                self.headers.append(self.data_list[0])
                self.data_list.pop(0)


    def get_headers(self):
        """funkcja wyświetlająca etykiety"""
        if self.headers == []:
            print('Nie ma etykiet w tym datasecie')
        else:
            for line in self.headers:
                print(line.split(','))

    def get_data(self,start=None,finish=None):
        """Funkcja wyświetlająca wycinek danych"""
        if start == None or finish == None:
            for line in self.data_list:
                print(line)
        else:
            if isinstance(start,int) and isinstance(finish,int):
                self.sliced_data_list = self.data_list[start:finish]
                for line in self.sliced_data_list:
                    print(line)


    def split_data(self,trening=0, test=0, walidacja=0):
        """
        Metoda rozdzielająca zbiór na trzy podzbiory. Dane w żadnym z podzbiorów nie dublują się.
        Funkcja najpierw sprawdza czy parametry są liczbami, a potem czy ich suma nie przekracza 100.
        """
        self.zbior_treningowy =[]
        self.zbior_testowy = []
        self.zbior_walidacyjny = []
        self.wykorzystane_indeksy =[]

        if isinstance(trening, (float, int)) and isinstance(test, (float, int)) and isinstance(walidacja, (float, int)):
            if trening + test + walidacja > 100:
                print('suma parametrów nie może być większa niz 100')
            else:
                 # zbiór treningowy
                self.counter = 0
                while self.counter < round(len(self.data_list)*trening/100):
                    self.random_index = random.randint(0,len(self.data_list)-1)
                    if self.random_index not in self.wykorzystane_indeksy:
                        self.zbior_treningowy.append(self.data_list[self.random_index])
                        self.wykorzystane_indeksy.append(self.random_index)
                        self.counter += 1

                # zbiór testowy
                self.counter = 0
                while self.counter < round(len(self.data_list)*test/100):
                    self.random_index = random.randint(0, len(self.data_list)-1)
                    if self.random_index not in self.wykorzystane_indeksy:
                        self.zbior_testowy.append(self.data_list[self.random_index])
                        self.wykorzystane_indeksy.append(self.random_index)
                        self.counter += 1

                # zbiór walidacyjny
                self.counter = 0
                while self.counter < round(len(self.data_list)*walidacja/100):
                    self.random_index = random.randint(0, len(self.data_list)-1)
                    if self.random_index not in self.wykorzystane_indeksy:
                        self.zbior_walidacyjny.append(self.data_list[self.random_index])
                        self.wykorzystane_indeksy.append(self.random_index)
                        self.counter += 1

        else: print('Parametry muszą być liczbami')

    def get_klasy_decyzyjne(self):
        """
        Metoda wyświetlająca klasy decyzyjne
        """
        self.unikalne_klasy = {}

        for linia in self.data_list:
            if linia[self.kolumna_decyzyjna] not in self.unikalne_klasy:
                self.unikalne_klasy[linia[self.kolumna_decyzyjna]] = 1
            else:
                self.unikalne_klasy[linia[self.kolumna_decyzyjna]] += 1

        for k, v in self.unikalne_klasy.items():
            print((k,v))

    def get_rows(self, value):
        """
        Funkcja pokazuje rzędy gdzie w kolumnie decyzyjnej jest konkretna wartość
        """
        for linia in self.data_list:
            if linia[self.kolumna_decyzyjna] == value:
                print(linia)

    def save_csv(self,data:list,name:str):
        """
        Funckja zapisuje dane do pliku csv
        """
        if isinstance(data,list) and isinstance(name, str):
            with open(name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        else: print('dane muszą być listą a nazwa pliku stringiem')


d1 = Dataset('car.data', 6)
# print(d1.data_list)
# d1.get_headers()
# d1.get_data(0,12)
# d1.split_data(15,30,20)
# d1.get_klasy_decyzyjne()
# d1.get_rows('good')
# d1.save_csv(d1.zbior_testowy,'test')



