import sys
sys.path.insert(0, '../')



import CPED

cped = CPED.CPED('charmap-0.json', 3)
# charmap-0:	all the values have a lenght of 1
# charmap-1:	all the values have a lenght between 1 and 4
#				(require separators included see the first key)


encrypted = cped.encrypt("hello GOOD -_- 777")
decrypted = cped.decrypt(encrypted)

print('encrypt :\t', repr(encrypted))
print('decrypted :\t', repr(decrypted))

print('\n\n')


random_int_config = CPED.random_config(int, list_size=18)
random_str_lower_config = CPED.random_config(str, 'lower')

print(random_int_config)
print(random_str_lower_config)



mixer = cped.CharsMixer(random_int_config)

mixed_word = mixer.mix_chars(encrypted)
unravel_word = mixer.unravel_chars(mixed_word)

print('encrypted + mixed text :\t', repr(mixed_word))
print('encrypted + unravel text :\t', repr(unravel_word))


# LARGE !
# print(cped.combinaissons('hello'))