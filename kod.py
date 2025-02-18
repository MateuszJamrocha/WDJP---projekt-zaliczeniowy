import random

class Dataset:

    def __init__(self):
        self.data_list = []
        self.headers = []

    def load_data(self, file, headers:bool=False):
        with open(file, 'r', newline='') as file_reader:
            for linia in file_reader:
                    self.data_list.append(linia)

        if headers == True:
            self.headers.append(self.data_list[0])
            self.data_list.pop(0)


    def get_headers(self):
        if self.headers == []:
            print('Nie ma etykiet w tym datasecie')
        else:
            for line in self.headers:
                print(line.split(','))

    def get_data(self,start=None,finish=None):
        if start == None or finish == None:
            for line in self.data_list:
                print(line)
        else:
            self.sliced_data_list = self.data_list[start:finish]
            for line in self.sliced_data_list:
                print(line)


    def split_data(self,trening=0, test=0, walidacja=0):
        """
        Metoda rozdzielająca zbiór na trzy podzbiory. Dane w żadnym z podzbiorów nie dublują się.
        """
        self.zbior_treningowy =[]
        self.zbior_testowy = []
        self.zbior_walidacyjny = []
        self.wykorzystane_indeksy =[]


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
                    print(self.random_index)
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



d1 = Dataset()
d1.load_data('car.data', False)
d1.get_headers()
# d1.get_data(10,20)
d1.split_data(15,30,60)
print('zbior treningowy',len(d1.zbior_treningowy))
print(d1.wykorzystane_indeksy)
print('zbior testowy', len(d1.zbior_testowy))
print(d1.wykorzystane_indeksy)
print('zbior walidacyjny', len(d1.zbior_walidacyjny))
print(d1.wykorzystane_indeksy)
print(len(d1.data_list))
