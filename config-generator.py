config = {
	"use-chars": {
		"all": False,

		"alphabet": {
			"lower": True,
			"upper": True
		},
		"digits": True,
		"punctuation": True,
		"whitespace": False
	},
	"random-chars-per-char": (1, 1) # not working for now :/
}

import string
from random import randint, choice


charmap = ""
if config['use-chars']['all']:
	for i in range(0x110000 - 1):
		charmap += chr(i)

else:
	if config['use-chars']['alphabet']['lower']: charmap += string.ascii_lowercase
	if config['use-chars']['alphabet']['upper']: charmap += string.ascii_uppercase
	if config['use-chars']['digits']: charmap += string.digits
	if config['use-chars']['punctuation']: charmap += string.punctuation
	if config['use-chars']['whitespace']: charmap += string.whitespace


base = ["{"]
chosed = []
for char in list(charmap):
	while True:
		n = randint(*config['random-chars-per-char'])
		r = ''
		for i in range(n):
			r += choice(list(charmap))

		r = r.replace('\\', '\\\\').replace('"', '\\"')

		if r not in chosed and char not in r:
			chosed.append(r)

			b = char.replace('\\', '\\\\').replace('"', '\\"')
			c = f'"{b}"'

			base.append(f'{c}: "{r}",')
			break

base = '\n\t'.join(base)
base = base[:-1]
base += '\n}'

with open('config.json', 'w') as f:
	f.write(base)
	f.close()