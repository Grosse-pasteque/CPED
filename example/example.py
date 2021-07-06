import sys
sys.path.insert(0, '../')

import CPED

cped = CPED.CPED('charmap.json', 3)


encrypt_word = cped.encrypt("hello GOOD -_- 777")
decrypt_word = cped.decrypt(encrypt_word)

print(encrypt_word)
print(decrypt_word)



random_int_config = CPED.random_config(int, list_size=18)
random_str_lower_config = CPED.random_config(str, 'lower')

print(random_int_config)
print(random_str_lower_config)



mixer = cped.CharsMixer(random_int_config)



mixed_word = mixer.mix_chars(encrypt_word)
print(mixed_word)

unravel_word = mixer.unravel_chars(mixed_word)
print(unravel_word)


# LARGE !
# print(cped.combinaissons('hello'))