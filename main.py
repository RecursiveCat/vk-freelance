#BASE
import modules
import config
import vk_api

#CLASSES
from modules import VK



num = config.number
pwd = config.pwd

vk = VK.VK(num,pwd)
vk = vk.GET_API()

print(vk.wall.post(message='Hello world!'))
