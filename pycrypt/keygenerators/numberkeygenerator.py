from keygenerator import *
from ..translators.numberedalphabettranslator import *
import random

class NumberKeyGenerator(KeyGenerator):
	def __init__(self, max_number=26, rand_func=lambda x: x ** 6):
		"""To be used with CaesarTranslator"""
		KeyGenerator.__init__(self)
		self.max_number = max_number
		self.rand_func = rand_func

	def getRandomKey(self):
		return random.randint(0, self.max_number - 1)

	def getAllKeys(self):
		return xrange(self.max_number)

	def mutateKey(self, key):
		"""Change rand_func for different transformation number after random.random"""
		return (key + int(self.rand_func(random.random() + 1))) % self.max_number
