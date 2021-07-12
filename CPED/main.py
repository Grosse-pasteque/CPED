# -*- coding: UTF-8 -*
from string import ascii_lowercase, ascii_uppercase
from random import randint, choice
from math import factorial
import itertools
import json
import os


class ListLenghtError(Exception): pass
class ConfigurationError(Exception): pass


class CPED:
	def __init__(self, charmap: list or str, conversion=1):
		if not isinstance(conversion, int):
			raise TypeError(
				f"conversion need to be {int} not {type(conversion)} !")
		
		self._conversion = conversion

		if isinstance(charmap, list):
			self._charmap_file = []
			self._charmap = {}

			for file in charmap:
				
				if not os.path.exists(file):
					raise SyntaxError(
						f"Path: {file} does not exists !")

				self._charmap_file.append(file)

				c = json.loads(open(file).read())
				for key, item in c.items():
					self._charmap[key] = item

		else:
			if not os.path.exists(charmap):
				raise SyntaxError(
					f"Path: {charmap} does not exists !")
			
			self._charmap_file = charmap
			self._charmap = json.loads(open(charmap).read())

		if "separators" not in list(self._charmap.keys()):
			for key, value in self._charmap.items():
				if len(value) > 1:
					raise ConfigurationError(
						"if you want to be able to use more than 1 char per key you need to configure separators.")

		self._separators = None

		if "separators" in list(self._charmap.keys()):
			if not isinstance(self._charmap['separators'], list):
				raise TypeError(
					f"The 'separators' key value need to be {list} not {type(self._charmap['separators'])}")

			self._separators = self._charmap['separators']
			self._charmap.pop('separators')


	@property
	def charmap(self):
		return self._charmap
	

	@property
	def charmap_file(self):
		return self._charmap_file


	@property
	def conversion(self):
		return self._conversion


	@property
	def separators(self):
		return self._separators


	def combinaissons(self, text: str, charmap_len=None, shuffle=True):
		if charmap_len == None:
			charmap_len = sum([len(k) for k in self._charmap.values()])
					
		if charmap_len >= 0x110000:
			raise ValueError(
				'chr() arg not in range(0x110000)')

		combinaissons = charmap_len ** len(text)
		combinaissons **= self._conversion

		if shuffle:
			combinaissons **= factorial(len(self.encrypt(text)))

		return combinaissons


	def encrypt(self, text: str):
		if not isinstance(text, str):
			raise TypeError(
				"text need to be type: str")

		all_chars = list(text)

		for loop in range(self._conversion):
			for i, char in enumerate(all_chars):
				
				try:
					all_chars[i] = all_chars[i].replace(char, self._charmap[char])

				except:
					pass

			if self._separators != None:
				seps = [
					choice(self._separators)
					for i in range(len(all_chars) - 1)
				]

				new_text = ""
				for i, char in enumerate(all_chars):
					new_text += char

					if i != len(seps):
						new_text += seps[i]

				all_chars = list(new_text)

			all_chars = list(''.join(all_chars))

		return ''.join(all_chars)


	def decrypt(self, text: str):
		if not isinstance(text, str):
			raise TypeError(
				"text need to be type: str")

		all_chars = text

		for loop in range(self._conversion):
			
			if self._separators != None:
				for sep in self._separators:
					all_chars = all_chars.replace(sep, '<-0->')
					# WARNING: please don't use this string '<-0->' as a value in your config (charmap)

				all_chars = all_chars.split('<-0->')

			else:
				all_chars = list(all_chars)

			for i, char in enumerate(all_chars):
				try:
					all_chars[i] = all_chars[i].replace(char, list(self._charmap.keys())[list(self._charmap.values()).index(char)])

				except (IndexError, ValueError):
					pass

			all_chars = ''.join(all_chars)

		return all_chars


	class CharsMixer:
		def __init__(self, var_config: list):
			if not isinstance(var_config, list):
				raise TypeError(
					"var_config need to be type: list")

			self.var_config = var_config


		def mix_chars(self, text: str):
			if not isinstance(text, str):
				raise TypeError(
					"text need to be type: str")

			mixed_chars = ''

			if len(self.var_config) != len(text):
				raise ListLenghtError(
					"List has not the same length as his linked list/word.")

			all_chars = list(text)

			for key in range(len(text)):
				mixed_chars += all_chars[self.var_config[key]]

			return mixed_chars


		def unravel_chars(self, text: str):
			if not isinstance(text, str):
				raise TypeError(
					"text need to be type: str")

			unravel_chars = ''

			if len(self.var_config) != len(text):
				raise ListLenghtError("List has not the same length as his linked list/word.")

			all_chars = list(text)

			for key in range(len(text)):
				unravel_chars += all_chars[self.var_config.index(key)]

			return unravel_chars



def random_config(*config, list_size=26):
	if not isinstance(list_size, int):
		raise TypeError(
			"list_size need to be types: int")

	var_config = []

	if config[0] == str:
		
		if list_size != 26:
			raise ListLenghtError(
				"Maximum list size for type: str <= 26 !")

		if config[1] == 'lower':
			while list_size != len(var_config):
				value = choice(list(ascii_lowercase))

				if value not in var_config:
					var_config.append(value)

		elif config[1] == 'upper':
			while list_size != len(var_config):
				value = choice(list(ascii_uppercase))

				if value not in var_config:
					var_config.append(value)
		
		else:
			raise TypeError(
				"Type: Str has only attributes: 'lower' and 'upper'.")

	elif config[0] != int:
		raise TypeError(
			"Type isn't supported.")
	
	while list_size != len(var_config):
		value = randint(0, list_size - 1)
		
		if value not in var_config:
			var_config.append(value)
	
	return var_config