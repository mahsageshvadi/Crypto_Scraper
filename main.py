import argparse

from data_update_handler import DataUpdateHandler



if __name__ == "__main__":


	parser = argparse.ArgumentParser()

	parser.add_argument('--subredditName', type = str , default = 'CryptoCurrency')

	args = parser.parse_args()

	# create update_controller class

	DataUpdateHandler(args.subredditName)
