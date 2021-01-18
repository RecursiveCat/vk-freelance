import vk_api

class VK:

  def __init__(self,num,pwd):
    print(str(__class__)+" : inited!")
    self.num = num
    self.pwd = pwd
    self.SESSION  = vk_api.VkApi(num,pwd)
    self.SESSION.auth()
    self.API = self.SESSION.get_api()

  def GET_API(self):
    print(str(__class__)+"->GET_API : called")
    try:
      return self.API
    except:
      print(str(__class__)+"->GET_API : error : cannot find API enitie")




