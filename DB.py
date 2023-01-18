import config 



class DB:

	def __init__(self):

		self.tables_name = config.tables_name


	def inset_query_with_dict(self, insert_dict, table_name):

		insert_query = "INSERT INTO {} (".format(self.tables_name[table_name])

		insert_query = insert_query + ') values ('



		for key, value in insert_dict.items():

			insert_query_split = insert_query.split(') values')
			insert_query = insert_query_split[0] + '{}, '.format(key) + ') values' + insert_query_split[1] + '{} '.format(value) + ','


		

		insert_query_split = insert_query.split(', ) values (')
		insert_query = insert_query_split[0] + ') values (' 
		insert_query = insert_query + insert_query_split[1].removesuffix(',') + ')'


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



















