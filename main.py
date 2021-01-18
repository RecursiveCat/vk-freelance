try:
  import modules
  import config
  import vk_api
except:
  print("Error: cannot import extensions :(")

try:
  from modules import VK
except:
  print("Error: cannot import program files :(")

try:
  num = config.number
  pwd = config.pwd
except:
  print("Error: cannot use config - invalid or doesnt exists")

try:
  vk = VK.VK(num,pwd)
  vk = vk.GET_API()
except:
  print("Error: program entities didnt inits")

def send():
  print(vk.wall.post(message='Hello world!'))
