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
            print('No headers in this data set')
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
        self.zbior_treningowy =[]
        self.zbior_testowy = []
        self.zbior_walidacyjny = []

        for n in range(round(len(self.data_list)*trening/100)):
            self.zbior_treningowy.append(self.data_list[random.randint(0,len(self.data_list))])



d1 = Dataset()
d1.load_data('car.data', True)
d1.get_headers()
# d1.get_data(10,20)
d1.split_data(15)
print(len(d1.zbior_treningowy))
