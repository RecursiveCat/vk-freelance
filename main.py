from bot import VkBot
from excel import CSV
import config

bot = VkBot(config.number, config.pwd)
open("ТАБЛИЦА.csv", "wb").close()
table = CSV("ТАБЛИЦА.csv")

with open("links.txt") as file:
	links = []
	for link in file:
		links.append(link.replace("\n", ""))

if links == []:
	print("Файл links.txt пуст! пожалуйста, вставьте туда ссылки, чтобы скрипт работал.")
	exit()

table.write_row_to_csv(['VK ID',
        'ССЫЛКА НА ПРОФИЛЬ',
        'ИМЯ',
        'ФАМИЛИЯ',
        'ПОЛ',
        'СТРАНА',
        'ГОРОД',
        'ЛЕТ',
        'ДАТА РОЖДЕНИЯ',
        'ФОТО 50PX',
        'ФОТО 100PX',
        'ФОТО 200PX',
        'ФОТО 400PX',
        'ВИЗИТ В ВК',
        'УСТРОЙСТВО ВИЗИТА В ВК',
        'ОНЛАЙН',
        'РОДНОЙ ГОРОД',
        'VK КОРОТКИЙ АДРЕС',
        'VK URL',
        'НИКНЕЙМ',
        'ДЕВИЧЬЯ ФАМИЛИЯ',
        'САЙТ',
        'СТАТУС',
        'ВЕРИФИКАЦИЯ',
        'ТЕКУЩАЯ ЗАНЯТОСТЬ',
        'СЕМЕЙНОЕ ПОЛОЖЕНИЕ',
        'ССЫЛКА НА ПАРТНЁРА',
        'ИМЯ ПАРТНЁРА',
        'ФАМИЛИЯ ПАРТНЁРА',
        'INSTAGRAM',
        'INSTAGRAM-@',
        'INSTAGRAM-ССЫЛКА'],"ТАБЛИЦА.csv")

for link in links:
	users = bot.get_users(link)
	for user_id in users:
		user = bot.get_user_data(user_id)
		table.write_row_to_csv([user['id'],
			user['link'],
			user['first_name'],
			user['last_name'],
			user['sex'],
			user['country'],
			user['city'],
			user['age'],
			user['bdate'],
			user['photo_50'],
			user['photo_100'],
			user['photo_200'],
			user['photo_400_orig'],
			user['last_seen'],
			user['platform'],
			user['online'],
			user['home_town'],
			user['domain'],
			user['link'],
			user['nickname'],
			user['maiden_name'],
			user['site'],
			user['status'],
			user['verified'],
			user['career'],
			user['relation'],
			user['relation_link'],
			user['relation_first_name'],
			user['relation_last_name'],
			user["instagram"],
			user["instagram_tag"],
			user["instagram_link"]
			],"ТАБЛИЦА.csv")
print("Таблица создана.")

