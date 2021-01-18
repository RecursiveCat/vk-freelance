import pandas

class EXEL:
  def __init__(self,path_to_table):
    print(str(__class__)+" : inited")
    self.FILE = path_to_file
    try:
      self.TABLE = pandas.read_csv(self.FILE)
    except:
      print(str(__class__)+" : running error : cannot open file " + str(self.FILE))
  def DUMP_TABLE(self):
    try:
      return list(self.TABLE)
    except:
      print(str(__class__)+" : error while exporting data from table")
