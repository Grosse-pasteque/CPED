import sys
sys.path.insert(0, '../')

import CPED

cped = CPED.CPED('charmap.json', 3)


encrypted = cped.encrypt("hello GOOD -_- 777")
decrypted = cped.decrypt(encrypted)

print(encrypted)
print(decrypted)



random_int_config = CPED.random_config(int, list_size=18)
random_str_lower_config = CPED.random_config(str, 'lower')

print(random_int_config)
print(random_str_lower_config)



mixer = cped.CharsMixer(random_int_config)



mixed_word = mixer.mix_chars(encrypted)
unravel_word = mixer.unravel_chars(mixed_word)

print(mixed_word)
print(unravel_word)


# LARGE !
# print(cped.combinaissons('hello'))