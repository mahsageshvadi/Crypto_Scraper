import config 
import mysql.connector

from prepare_data_for_DB import get_dictionary_from_post_json


class DB:

	def __init__(self):

		self.tables_name = config.tables_name
		self.data_types_in_posts_table_not_need_qotation = config.data_types_in_posts_table_not_need_qotation
		self.DB_config = config.DB_config

		self.DB =  mysql.connector.connect(

		        host= self.DB_config['host'],
		        user= self.DB_config['user'],
		        passwd= self.DB_config['passwd'],
		        database= self.DB_config['database']


        	)
		self.mycursor = self.DB.cursor()




	def insert_query_with_dict(self, insert_dict, table_name):

		insert_query = "INSERT INTO {} (".format(self.tables_name[table_name])

		insert_query = insert_query + ') values ('



		for key, value in insert_dict.items():

			insert_query_split = insert_query.split(') values')
			if key in self.data_types_in_posts_table_not_need_qotation:
				insert_query = insert_query_split[0] + '`{}`, '.format(key) + ') values' + insert_query_split[1] + '{} '.format(value) + ','
			else:
				if "'" in value:
					value = value.replace("'", "''")
					print('111111111111111111111111111111111111')
				if "\"" in value:
					value = value.replace('"', '\"')
					print("222222222222222222222222222222222222")
					print(value)
				print('33333333333333333333333333333333')

				insert_query = insert_query_split[0] + '`{}`, '.format(key) + ') values' + insert_query_split[1] + '"{}" '.format(value) + ','



		

		insert_query_split = insert_query.split(', ) values (')
		insert_query = insert_query_split[0] + ') values (' 
		insert_query = insert_query + insert_query_split[1].removesuffix(',') + ');'


		return insert_query 


	def get_last_post_id(self, limit=1):

		sql =  """SELECT id  FROM posts 
                    ORDER BY date_and_time DESC
                    LIMIT
                    """ + str(limit)

		try:
			self.cursorObject.execute(sql)
			last_id = self.cursorObject.fetchall()

			return last_id
		except:
			return None

	def insert_posts_to_db(self, posts):

		for post in posts.json()['data']['children']:
			post_dict =  get_dictionary_from_post_json(post)
			insert_query = self.insert_query_with_dict(post_dict, 'posts')
			print("***********************************************************************************")
			print(insert_query)
			self.mycursor.execute(insert_query)
			self.DB.commit()





















