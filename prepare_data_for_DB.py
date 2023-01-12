from datetime import datetime


def get_dictionary_from_post_json(post_data): 

		post_dictionary = {}

		post_dictionary['post_id'] = post_data['kind'] + '_' + post_data['data']['id']

		post_data = post_data['data']

		post_text = post_data['selftext']
		post_text = post_text.replace('\n', '')
		post_dictionary['text'] = post_text.replace('\\', '')

		post_title = post_data['title']
		post_dictionary['title'] = post_title.replace('\\', '')



		post_dictionary['link'] = post_data['permalink']

		post_dictionary['author'] = post_data['author']

		post_dictionary['post_category'] = post_data['link_flair_css_class']

		post_dictionary['subreditName'] = post_data['subreddit']

		post_dictionary['downs'] = post_data['downs']

		post_dictionary['ups'] = post_data['ups']

		post_dictionary['score'] = post_data['score']

		post_dictionary['CommentsNumber'] = post_data['num_comments']

		post_dictionary['upVoteRatio'] = post_data['upvote_ratio']

		ts = int(post_data['created_utc'])
		post_dictionary['timePosted'] = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		post_dictionary['media'] = post_data['secure_media_embed']

		post_dictionary['pinned'] = post_data['pinned']

		post_dictionary['Raw_json'] = post_data


		return post_dictionary


def get_dictionary_from_comment_json(comment_data_list, post_id, parent_id, comment_level, list_of_dics):

		comment_dictionary = {}

		for comment_data in comment_data_list:




			try:


				if comment_data['data']['replies'] != '' :

					get_dictionary_from_comment_json(comment_data['data']['replies']['data']['children'], post_id,
					comment_data['kind'] + '_' + comment_data['data']['id'], comment_level +1, list_of_dics)

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

				comment_dictionary['score'] = comment_data['score']

				comment_dictionary['ups'] = comment_data['ups']

				comment_dictionary['downs'] = comment_data['downs']

			except:
				print(comment_data)

			list_of_dics.append(comment_dictionary)

		return list_of_dics





			