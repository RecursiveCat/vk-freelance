def convert_list_to_int(arg):
    day = int(str((arg)[0][0])+str((arg)[0][1]))
    mounth = int(str((arg)[0][3])+str((arg)[0][4]))
    year = int(str((arg)[0][6::]))
    return {
      "DAY":day,
      "MOUNTH":mounth,
      "YEAR":year
           }

print(convert_list_to_int(["19.19.1945"]))
