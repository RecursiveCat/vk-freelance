import config
import vk_api
from time import strftime


num  = config.number
pwd  = config.pwd
post = "https://vk.com/wall612976792_6"


class VkBot:

	def __init__(self, number, password):
		vk_session = vk_api.VkApi(number,password)
		vk_session.auth()
		self.vk = vk_session.get_api()

	def get_users(self,post):
		return self.vk.likes.getList(type="post",item_id=6)['items']

	def get_user_data(self,user_id):
		need_data = self.vk.users.get(user_ids=user_id,fields=
			"""
			photo_id, verified,
			home_town, has_photo,
			photo_50, photo_100,
			photo_200_orig, photo_200,
			photo_400_orig, photo_max,
			photo_max_orig, domain,
			has_mobile, contacts, site, education, 
			universities, schools, status, last_seen, 
			followers_count, common_count, occupation, 
			nickname, relatives, relation,
			personal, connections, exports, 
			activities, interests, music, 
			movies, tv, books, games, about, 
			quotes, can_post, can_see_all_posts, 
			can_see_audio, can_write_private_message, can_send_friend_request, 
			is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, 
			crop_photo, is_friend, friend_status, career, military, blacklisted, 
			blacklisted_by_me, can_be_invited_group
			""")[0]
		return {
			"id":user_id,
			"link_id": f"https://vk.com/id{user_id}",
			"first_name": need_data['first_name'],
			"last_name": need_data['last_name'],
			"sex": need_data['sex'],
			"country": need_data['country'],
			"city": need_data['city'],
			"age": str(int(strftime("%Y")) - int(need_data['bdate'][5::])),
			"bdate": need_data['bdate'],
			"photo_50": need_data['photo_50'],
			"photo_100": need_data['photo_100'],
			"photo_200": need_data['photo_200'],
			"photo_400": need_data['photo_400'],
			"visit": need_data['last_seen'],
			"device": need_data['has_mobile'],
			'online': need_data['online'],
			"nickname": need_data['nickname'],
			"link_url": f"https://vk.com/{need_data['nickname']}",
			"site": need_data['site'],
			"status": need_data['status'],
			"verified": need_data['verified'],
			"career": need_data['career'],
			""
		}


vk = VkBot(num, pwd)
print(vk.get_user_data("612976792"))


