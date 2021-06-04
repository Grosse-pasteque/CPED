import CPED

cped = CPED.CPED(True, True, True, True, 3)

cped.configure_alphabet(['v', 'r', 'z', 'h', 'j', 'c', 'b', 'o', 't', 'p', 'd', 'n', 'g', 'q', 'e', 'm', 'a', 'l', 'f', 'w', 'x', 's', 'i', 'y', 'u', 'k'])
cped.configure_caps_alphabet(['V', 'R', 'Z', 'H', 'J', 'C', 'B', 'O', 'T', 'P', 'D', 'N', 'G', 'Q', 'E', 'M', 'A', 'L', 'F', 'W', 'X', 'S', 'I', 'Y', 'U', 'K'])
cped.configure_numbers(['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'])
cped.configure_more_chars(['_', '-', 'é', 'à', '('], ['(', 'à', 'é', '-', '_'])

if cped.check_config():
    encrypt_word = cped.encrypt("hello GOOD -_- 777")
    print(encrypt_word)
    decrypt_word = cped.decrypt(encrypt_word)
    print(decrypt_word)
else:
    print("Configuration not correct !")


my_list_0 = []
my_list_1 = []

mixer = cped.CharsMixer(my_list_0)

random_int_config = CPED.random_config(int, list_size=18, var_config=my_list_0)
random_str_upper_config = CPED.random_config(str, 'lower', list_size=26, var_config=my_list_1)

print(random_int_config)
print(random_str_upper_config)


mixed_word = mixer.mix_chars(encrypt_word)
print(mixed_word)

unravel_word = mixer.unravel_chars(mixed_word)
print(unravel_word)


# example of a multiple times mixer
for loop in range(10):
    mixed_word = mixer.mix_chars(encrypt_word)
print(mixed_word)
