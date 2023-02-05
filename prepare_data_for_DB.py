from datetime import datetime

# this gives us one dictionary for every single post 
def get_dictionary_from_post_json(post_data): 

		post_dictionary = {}

		post_dictionary['post_id'] = post_data['kind'] + '_' + post_data['data']['id']

		post_data = post_data['data']

		post_text = post_data['selftext']
		post_text = post_text.replace('\n', '')
		post_dictionary['post_text'] = post_text.replace('\\', '')

		post_title = post_data['title']
		post_dictionary['title'] = post_title.replace('\\', '')



		post_dictionary['link'] = post_data['permalink']

		post_dictionary['author'] = post_data['author']

		post_dictionary['post_category'] = post_data['link_flair_css_class']

		post_dictionary['subreditName'] = post_data['subreddit']

		post_dictionary['downs'] = post_data['downs']

		post_dictionary['ups'] = post_data['ups']

		post_dictionary['score'] = post_data['score']

		post_dictionary['commentsNumber'] = post_data['num_comments']

		post_dictionary['upVoteRatio'] = post_data['upvote_ratio']

		ts = int(post_data['created_utc'])
		post_dictionary['timePosted'] = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		post_dictionary['media'] = str(post_data['secure_media_embed'])

		post_dictionary['pinned'] = post_data['pinned']

		#post_dictionary['raw_json'] = post_data


		return post_dictionary

# this gives us comments of a specific post in one dictionary
def get_dictionary_from_comment_json(comment_data_list, post_id, parent_id, comment_level, list_of_dics, list_of_users):

		comment_dictionary = {}

		for comment_data in comment_data_list:

			try:


				if comment_data['data']['replies'] != '' :

					get_dictionary_from_comment_json(comment_data['data']['replies']['data']['children'], post_id,
					comment_data['kind'] + '_' + comment_data['data']['id'], comment_level +1, list_of_dics, list_of_users)

				# todo: if 'Hello, your post was removed' in comment['data']['body']:

				comment_dictionary['comment_id'] =  comment_data['kind'] + '_' + comment_data['data']['id']

				comment_data = comment_data['data']

				ts = int(comment_data['created_utc'])
				comment_dictionary['timePosted'] = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

				# todo: add users

				comment_dictionary['post_id'] = post_id

				comment_dictionary['parent_id'] = parent_id

				comment_dictionary['comment_level'] = comment_level

				comment_dictionary['text'] = comment_data['body']

				comment_dictionary['author'] = comment_data['author']
				list_of_users.append(comment_data['author'])

				comment_dictionary['score'] = comment_data['score']

				comment_dictionary['ups'] = comment_data['ups']

				comment_dictionary['downs'] = comment_data['downs']

				comment_dictionary['raw_json'] = comment_data


			except:
				print('**EXCEPTION ' + comment_data)

			list_of_dics.append(comment_dictionary)



		return list_of_dics, list_of_users


def get_dictionary_from_user_json(user_data):

	user_dictionary = {}
	user_dictionary_other = {}

	ts = int(user_data['created_utc'])
	time_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	user_dictionary['created_date'] = time_date

	user_dictionary['displayName'] = user_data['subreddit']['display_name']

	user_dictionary['title'] = user_data['subreddit']['title']

	user_dictionary['Name'] = user_data['name']

	user_dictionary['userURL'] = user_data['subreddit']['url']

	user_dictionary['public_description'] = user_data['subreddit']['public_description']

	user_dictionary['awardee_karma'] = user_data['awardee_karma']

	user_dictionary['awarder_karma'] = user_data['awarder_karma']

	user_dictionary['link_karma'] = user_data['link_karma']

	user_dictionary['comment_karma'] = user_data['comment_karma']

	user_dictionary['verified'] = user_data['verified']

	user_dictionary['is_gold'] = user_data['is_gold']

	user_dictionary['has_verified_email'] = user_data['has_verified_email']

	user_dictionary_other['restrict_commenting'] = user_data['subreddit']['restrict_commenting']

	user_dictionary_other['subscribers'] = user_data['subreddit']['subscribers']

	user_dictionary_other['is_default_banner'] = user_data['subreddit']['is_default_banner']

	user_dictionary_other['quarantine'] = user_data['subreddit']['quarantine']

	user_dictionary_other['user_is_moderator'] = user_data['subreddit']['user_is_moderator']

	user_dictionary_other['accept_followers'] = user_data['subreddit']['accept_followers']

	user_dictionary_other['link_flair_enabled'] = user_data['subreddit']['link_flair_enabled']

	user_dictionary_other['disable_contributor_requests'] = user_data['subreddit']['disable_contributor_requests']

	user_dictionary_other['user_is_subscriber'] = user_data['subreddit']['user_is_subscriber']

	user_dictionary_other['is_mod'] = user_data['is_mod']

	user_dictionary_other['hide_from_robots'] = user_data['hide_from_robots']

	user_dictionary_other['pref_show_snoovatar'] = user_data['pref_show_snoovatar']

	user_dictionary_other['is_blocked'] = user_data['is_blocked']

	user_dictionary_other['accept_chats'] = user_data['accept_chats']

	user_dictionary_other['snoovatar_img'] = user_data['snoovatar_img']

	user_dictionary_other['has_subscribed'] = user_data['has_subscribed']

	user_dictionary_other['accept_pms'] = user_data['accept_pms']

	user_dictionary_other['default_set'] = user_data['subreddit']['default_set']

	user_dictionary_other['user_is_contributor'] = user_data['subreddit']['user_is_contributor']

	user_dictionary_other['restrict_posting'] = user_data['subreddit']['restrict_posting']

	user_dictionary_other['user_is_banned'] = user_data['subreddit']['user_is_banned']

	user_dictionary_other['free_form_reports'] = user_data['subreddit']['free_form_reports']

	user_dictionary_other['show_media'] = user_data['subreddit']['show_media']

	user_dictionary_other['user_is_muted'] = user_data['subreddit']['user_is_muted']

	user_dictionary_other['over_18'] = user_data['subreddit']['over_18']

	user_dictionary_other['raw_json'] = user_data

	return user_dictionary, user_dictionary_other

			