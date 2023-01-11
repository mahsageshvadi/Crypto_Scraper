
import requests
import config

class SubRedditScraper:

	def __init__(self, subreddit_name):

		self.subreddit_name = subreddit_name
		self.set_header()

	# sets headers for request, this is based on reddit API documentation
	def set_header(self):

		CLIENT_ID = config.CLIENT_ID
		SECRET_KEY = config.SECRET_KEY

		auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

		self.headers = config.initial_header

		data = {
	            'grant_type': 'password',
	            'username': config.username,
	            'password': config.password
	        }
		res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=self.headers)
		TOKEN = res.json()
		Acces_Token = TOKEN['access_token']

		self.headers['Authorization'] = f'bearer {Acces_Token}'


	#Gets new posts, if use Last_post_ID to avoid getting redunant data when scraping 

	def get_new_posts(self, Last_post_ID = None):

		if Last_post_ID is not None:

			params = {'before': Last_post_ID}

		else:
			params = {}

		new_posts = requests.get('https://oauth.reddit.com/r/{}/new'.format(self.subreddit_name), headers= self.headers, 
			params= params)

		if new_posts.status_code !=200:
			self.set_header()
			self.get_new_posts()


		return new_posts.json()

	def get_users_data(self, username):

		user_data = requests.get("https://oauth.reddit.com/user/{}/about.json".format(username), headers=self.headers)

		return user_data.json()


	def get_post_comments(self, post_link):

		comments =  requests.get('https://oauth.reddit.com' + post_link, headers=self.headers)

		return comments.json()[1]['data']['children']




