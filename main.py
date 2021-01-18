try:
  import sys
  import modules
  import config
  import vk_api
except:
  print("Error: cannot import extensions :(")

try:
  from modules import VK
  from modules import EXEL
except:
  print("Error: cannot import program files :(")

try:
  num = config.number
  pwd = config.pwd
  file_with_table = sys.argv[1]
  print("Table: "+str(file_with_table))
except:
  print("Error: cannot use config - invalid or doesnt exists")

try:
  vk = VK.VK(num,pwd)
  vk = vk.GET_API()
  exel = EXEL.EXEL(file_with_table)
  print(exel.DUMP_TABLE())
except:
  print("Error: program entities didnt inits")

def send():
  print(vk.wall.post(message='Hello world!'))
