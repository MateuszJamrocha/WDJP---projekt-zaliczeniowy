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



d1 = Dataset()
d1.load_data('car.data', False)
# print(f'headery: {d1.headers}, datalist: {d1.data_list}')
print(d1.data_list[0],d1.headers)