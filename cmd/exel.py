import csv

class Exel:

    def __init__(self,path_to_csv_table):
        self.path_to_csv_table = path_to_csv_table

    def get_row_from_table(self,row_index):
        counter = 0
        self.cache_row = None
        self.csv_file = open(self.path_to_csv_table, 'r')
        self.csv_reader = csv.reader(self.csv_file)
        for row in self.csv_reader:
            if counter == row_index:
                self.cache_row = row
            else:
                counter = counter + 1
        self.csv_file.close()
        return self.cache_row

    def write_row_to_csv(self,row,path_to_csv_file):
       self.row_to_write = list(row)
       with open(path_to_csv_file, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.row_to_write)

    def find_symbols_in_row(self,symbols,row):
        for word in row:
            if symbols in word:
                return True
        return False

    def get_last_writed_row(self):
        return self.row_to_write

    def get_last_exported_row(self):
        return self.cache_row


## Base demo
# exel = Exel("/home/int0x80/Public/vk-freelance/tables/test.csv")
# print(exel.get_row_from_table(1))
# exel.write_row_to_csv([1,2,3],"lol.csv")
# print(exel.get_last_writed_row())
# print(exel.get_last_exported_row())
# print(exel.find_symbols_in_row("sucka",exel.get_last_exported_row()))
##
