
import csv

class CSV:

    def __init__(self,path_to_table_source_file):
        self.delimiter_spliter = ";"
        self.path_to_table_source_file = path_to_table_source_file
        self.table_source_file = open(self.path_to_table_source_file, 'r')
        self.row_reader = csv.reader(self.table_source_file,delimiter=self.delimiter_spliter)

    def get_row_by_index (self,waiting_row_index):
        current_row_index = 0
        for row in self.row_reader:
            if current_row_index == waiting_row_index:
                return  {
                 'VK ID'             :row[0],
                 'ССЫЛКА НА ПРОФИЛЬ' :row[1],
                 'ИМЯ'               :row[2],
                 'ФАМИЛИЯ'           :row[3],
                 'ПОЛ'               :row[4],
                 'СТРАНА'            :row[5],
                 'ГОРОД'             :row[6],
                 'ЛЕТ'               :row[7],
                 'ДАТА РОЖДЕНИЯ'     :row[8],
                 'ФОТО 50PX'         :row[9],
                 'ФОТО 100PX'        :row[10],
                 'ФОТО 200PX'        :row[11],
                 'ФОТО 400PX'        :row[12],
                 'ВИЗИТ В ВК'        :row[14],
                 'УСТРОЙСТВО ВИЗИТА В ВК':row[15],
                 'ОНЛАЙН'            :row[16],
                 'РОДНОЙ ГОРОД'      :row[17],
                 'VK КОРОТКИЙ АДРЕС' :row[18],
                 'VK URL'            :row[19],
                 'НИКНЕЙМ'           :row[20],
                 'ДЕВИЧЬЯ ФАМИЛИЯ'   :row[21],
                 'САЙТ'              :row[22],
                 'СТАТУС'            :row[23],
                 'ВЕРИФИКАЦИЯ'       :row[24],
                 'ТЕКУЩАЯ ЗАНЯТОСТЬ' :row[25],
                 'СЕМЕЙНОЕ ПОЛОЖЕНИЕ':row[26],
                 'ССЫЛКА НА ПАРТНЁРА':row[27],
                 'ИМЯ ПАРТНЁРА'      :row[28],
                 'ФАМИЛИЯ ПАРТНЁРА'  :row[29],
                 'INSTAGRAM'         :row[30],
                 'INSTAGRAM-@'       :row[31],
                 'INSTAGRAM-ССЫЛКА'  :row[32],
                }
            else:
                current_row_index =    current_row_index + 1

    def is_element_exists(self,element,row):
        if element in row:
            return True
        else:
            return False

    def write_row_to_csv(self,row,path_to_csv_file):
       with open(path_to_csv_file, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)


table = CSV("/home/int0x80/Desktop/freelance/vk-freelance/tables/test.csv")
row = table.get_row_by_index(1)
print(row)
print(table.is_element_exists("Александра",row))
table.write_row_to_csv("lol","tes1.csv")
