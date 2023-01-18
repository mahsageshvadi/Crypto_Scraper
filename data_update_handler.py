import json

from reddit_scraper import SubRedditScraper
from DB import DB
from prepare_data_for_DB import get_dictionary_from_post_json, get_dictionary_from_comment_json, get_dictionary_from_user_json


class DataUpdateHandler:


	def __init__(self, subredditName):

		# create a reddit scraper class 

		reddit_scraper = SubRedditScraper(subredditName)
		self.reddit_scraper = reddit_scraper

		self.DB = DB()

		self.lastPostId = 0


	def update_user(self, username):

		user_data = self.reddit_scraper.get_users_data(username)

		try: 
			user_data = user_data['data']

		except:
			return

		user_dict, user_dict_other = get_dictionary_from_user_json(user_data)


        # todo: if 'is_suspended' in users_json.keys():

	def update_posts(self):

		new_posts = self.reddit_scraper.get_new_posts()


		for post in new_posts:
			post_dict =  get_dictionary_from_post_json(post)

			#self.update_comments(post_dict['link'], 1)


	def update_comments(self, post_url, post_id):

		new_comments = self.reddit_scraper.get_post_comments(post_url)
		comment_dicts, user_list = get_dictionary_from_comment_json(new_comments, post_id, post_id ,1, [], [])

		#for comment_dict in comment_dicts:

		#	self.DB.inset_query_with_dict(comment_dict, 'comments')

		for username in user_list:
			self.update_user(username)

	def start(self):

		
		#self.update_posts()
		#self.update_comments('/r/CryptoCurrency/comments/10fdcki/whats_the_direction_is_this_recovery_or_a_bull/', 1)
		
