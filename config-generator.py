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
	"use-separators": True,
	"separators": 4,
	"separators-lenght": (2, 4),
	"separators-charmap": "charmap",
	"random-chars-per-char": (1, 4) # not working for now :/
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

if config['use-separators']:
	separators = '\n\t"separators": ['
	seps = []
	m = list(eval(config['separators-charmap']))
	for i in range(config['separators']):
		sep = ""
		r = randint(*config['separators-lenght'])
		for i in range(r):
			sep += choice(m)

		seps.append(f'"{sep}"')

	separators += ', '.join(seps) + '],'

	base[0] += separators


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