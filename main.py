#BASE
import modules
import config
import vk_api

#CLASSES
from modules import VK



num = config.number
pwd = config.pwd
post = "https://vk.com/wall612976792_6"
class VkBot:
	def __init__(self, number, password):
		vk_session = vk_api.VkApi(number,password)
		vk_session.auth()
		self.vk = vk_session.get_api()

<<<<<<< HEAD
vk = VK.VK(num,pwd)
vk = vk.GET_API()
=======
	def get_users(self,post):
		print(self.vk.likes.getList(type="post",item_id=6))

>>>>>>> afb63c1 (make it better)

vk = VkBot(num, pwd)

vk.get_users(post)