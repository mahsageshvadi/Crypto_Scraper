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


	def update_user(self, username):

		user_data = self.reddit_scraper.get_users_data(username)

		try: 
			user_data = user_data['data']

		except:
			return

		user_dict, user_dict_other = get_dictionary_from_user_json(user_data)


        # todo: if 'is_suspended' in users_json.keys():

    def get_last_valid_post_id(self, limit= 2):

        before_last_id = self.DB.get_last_post_id(limit)
        if before_last_id is not None:
            before_last_id = before_last_id[limit-1][0]

            if self.reddit_scraper.get_new_posts(before_last_id).json()['data']['children']:
                return before_last_id
            else:
                before_last_id = get_last_valid_post_id(limit+1)
                return before_last_id

	def update_posts(self, last_post_id):

		new_posts = self.reddit_scraper.get_new_posts(last_post_id)

		# we should check if new-posts exists maybe the post related to last_post_id has been deleted

		if not new_posts.json()['data']['children']:

			last_post_id_candidate = self.get_last_valid_post_id()
            if last_post_id_candidate is not None:
                last_post_id = last_post_id_candidate
                new_posts = self.reddit_scraper.get_new_posts(last_post_id)

				for post in new_posts:
					post_dict =  get_dictionary_from_post_json(post)

					################Start DB

			#self.update_comments(post_dict['link'], 1)


	def update_comments(self, post_url, post_id):

		new_comments = self.reddit_scraper.get_post_comments(post_url)
		comment_dicts, user_list = get_dictionary_from_comment_json(new_comments, post_id, post_id ,1, [], [])

		#for comment_dict in comment_dicts:

		#	self.DB.inset_query_with_dict(comment_dict, 'comments')

		for username in user_list:
			self.update_user(username)

	def start_post_update(firsttime):

		if !firsttime:
			last_post_id = self.DB.get_last_post_id()
			if last_post_id is not None:
	            last_post_id = last_post_id[0][0]
	            if last_post_id is not None:	
	            	update_posts(last_post_id)

	    else:
	    	self.updata_posts(None)

		
