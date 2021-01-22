import config
import vk_api
from datetime import datetime


class VkBot:
	def __init__(self, number, password):
		vk_session = vk_api.VkApi(number,password)
		vk_session.auth()
		self.vk = vk_session.get_api()

	def get_users(self,link):
		post = link.split("wall")[1]
		owner_id = int(post[0])
		item_id = post[1]
		return self.vk.likes.getList(type="post",item_id=item_id, owner_id=-owner_id)['items']

	def get_user_data(self, id):
		fields = """domain, sex, country, city, bdate,
			 photo_50, photo_100, photo_200, photo_400_orig,
			 last_seen, online, home_town, nickname, maiden_name,
			 site, status, verified, career, relation, connections
			"""
		need_data = self.vk.users.get(user_ids=id,fields=fields)[0]
		need_data['id'] = id
		for field in fields.replace("\n","").replace("\t","").split(", "):
			if field in need_data.keys():
				if need_data[field] in ("", {}, [], None):
					need_data[field] = "не указано"
			else:
				need_data[field] = "не указано"

		need_data['verified'] = str(need_data['verified']).replace("0","нет").replace("1","да")
		need_data['link'] = "https://vk.com/" + need_data['domain']
		try:
			need_data['platform'] = str(need_data['last_seen']['platform']).replace("1","мобильная версия")\
			.replace("2","приложение для iPhone").replace("3","приложение для iPad").replace("4","приложение для Android")\
			.replace("5","приложение для Windows Phone").replace("6","приложение для Windows 10").replace("7","полная версия сайта")
			need_data['last_seen'] = datetime.utcfromtimestamp(need_data['last_seen']['time']).strftime('%Y-%m-%d %H:%M')
		except TypeError:
			need_data['platform'] = "не указано"
		try:
			need_data['age'] = str(2021 - int(need_data['bdate'].split(".")[2]))
		except (KeyError,IndexError):
			need_data['age'] = "не указано"
		try:
			if type(need_data['career']) is not str:
				need_data['career'] = need_data['career'][0]['position']
		except (KeyError,TypeError):
			need_data['career'] = "не указано"
		if need_data['relation'] != "не указано":
			need_data['relation'] = str(need_data['relation']).replace("1","не женат/не замужем")\
			.replace("2","есть друг/есть подруга").replace("3","помолвлен/помолвлена")\
			.replace("4","женат/замужем").replace("5","всё сложно")\
			.replace("6","в активном поиске").replace("7","влюблён/влюблена")\
			.replace("8"," в гражданском браке").replace("0","не указано")
		if "relation_partner" in need_data.keys():
			need_data['relation_link'] = "https://vk.com/" + str(need_data['relation_partner']['id'])
			need_data['relation_first_name'] = need_data['relation_partner']['first_name']
			need_data['relation_last_name'] = need_data['relation_partner']['last_name']
		else:
			need_data['relation_link'] = "не указано"
			need_data['relation_first_name'] = "не указано"
			need_data['relation_last_name'] = "не указано"
		need_data['sex'] = str(need_data['sex']).replace('2',"М").replace('1',"Ж").replace('0',"Н")
		need_data['online'] = str(need_data['online']).replace("1","онлайн").replace("0","оффлайн")
		if need_data['country'] != "не указано":
			need_data['country'] = need_data['country']['title']
		else:
			need_data['country'] =  "не указано"
		if need_data['city'] != "не указано":
			need_data['city'] = need_data['city']['title']
		else:
			need_data['city'] =  "не указано"
		if "instagram" not in need_data.keys():
			need_data['instagram'] = "не указано"
			need_data['instagram_link'] = "не указано"
			need_data['instagram_tag'] = "не указано"
		else:
			need_data['instagram_link'] = "https//www.instagram.com/" + need_data['instagram']
			need_data['instagram_tag'] = "@" + need_data['instagram']

		if "maiden_name" not in need_data.keys():
			need_data['maiden_name'] = "не указано"
		return need_data

#print(VkBot(config.number, config.pwd).get_user_data(612976792))