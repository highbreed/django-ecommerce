import string
import random

def randominvice(stringlength=15):
	"""
	Generate a random string of fixed length
	:param stringlength:
	:return:
	"""
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringlength))

