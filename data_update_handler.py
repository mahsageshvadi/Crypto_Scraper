import json

from reddit_scraper import SubRedditScraper
from prepare_data_for_DB import get_dictionary_from_post_json, get_dictionary_from_comment_json


class DataUpdateHandler:


	def __init__(self, subredditName):

		# create a reddit scraper class 

		reddit_scraper = SubRedditScraper(subredditName)

		self.reddit_scraper = reddit_scraper


	def update_user(self, username):

		user_data = self.reddit_scraper.get_users_data(username)

		try:
            user_data = user_data['data']
        except:
            return
        # todo: if 'is_suspended' in users_json.keys():

        

	def update_posts(self):

		new_posts = self.reddit_scraper.get_new_posts()


		for post in new_posts:
			post_dict =  get_dictionary_from_post_json(new_posts[0])


	def update_comments(self, post_url, post_id):

		new_comments = self.reddit_scraper.get_post_comments(post_url)

		comment_dics = get_dictionary_from_comment_json(new_comments, post_id, post_id ,1, [])



	def start(self):

		self.update_posts()
		self.update_comments()
		
