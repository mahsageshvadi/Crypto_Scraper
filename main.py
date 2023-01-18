import argparse

from data_update_handler import DataUpdateHandler



if __name__ == "__main__":


	parser = argparse.ArgumentParser()

	parser.add_argument('--subredditName', type = str , default = 'CryptoCurrency')
	parser.add_argument('--firsttime', type = bool, default = False)

	args = parser.parse_args()

	# create update_controller class

	data_update_handler = DataUpdateHandler(args.subredditName)
	data_update_handler.start_post_update(args.firsttime)
