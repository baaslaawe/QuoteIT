"""
textToImage.py
Converts the given text into an image
"""

import PIL	# Python Image Lib
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


class TextToImage(object):

	def __init__(self, text, full_path, color = "#000", bgcolor = "#FFF", font_full_path = None, left_padding = 3, right_padding = 3, width = 200):
		self.text = text
		self.full_path = full_path
		self.color = color
		self.bgcolor = bgcolor
		self.font_full_path = font_full_path
		self.left_padding = left_padding
		self.right_padding = right_padding
		self.width = width
		self.image_font = ImageFont.truetype('Roboto/Roboto-Light.ttf', 15)

	def create_image(self):
		lines = []
		line = u""

		for word in self.text.split():
			print word
			self.image_font.getsize(line + ' ' + word)[0] <= (self.width - self.right_padding - self.left_padding)
			line += ' ' + word
		if len(line) != 0:
			lines.append(line[1:])
		print lines

		line_height = self.image_font.getsize(self.text)[1]
		img_height = line_height * (len(lines) + 1)
		print line_height
		print img_height

		img = Image.new("RGBA", (self.width, img_height), self.bgcolor)
		draw = ImageDraw.Draw(img)

		y = 0
		for line in lines:
			draw.text( (self.left_padding, y), line, self.color, font = self.image_font)
			y += line_height

		img.save(self.full_path)
		

if __name__ == '__main__':
	obj = TextToImage("This is awesome", "test.png")
	obj.create_image()
	
