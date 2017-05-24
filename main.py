# main.py

import csv

from random import randint

from PIL import Image 
from PIL import ImageDraw
import cStringIO

from textToImage import TextToImage


class QuoteIT(object):

	def __init__(self):
		pass

	def get_random_quote_from_csv(self):
		quotes = []
		rownum = 0;
		file_name = "top_100_quotes.csv"
		with open(file_name, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if rownum == 0:
					header = row
				else:
					text = row[0]
					author = row[1]
					quote = { 'text' : text, 'author' : author }
					quotes.append(quote)
				rownum += 1
			quotes_count = len(quotes)
			random_count = randint(0, quotes_count)
			random_quote = quotes[random_count]
			return random_quote


if __name__ == '__main__':
	image_name = 'quote.png'
	obj = QuoteIT()
	quote = obj.get_random_quote_from_csv()
	image_conv = TextToImage(quote['text'], image_name)
	image_conv.create_image()
