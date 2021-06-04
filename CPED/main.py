# -*- coding: UTF-8 -*
# File explanations => file: ./README.md
from .errors import *
from random import randint, choice
from string import ascii_lowercase, ascii_uppercase

# configuration function
class CPED:
    def __init__(self, use_alphabet: bool, use_caps_alphabet: bool, use_numbers: bool, use_more_chars: bool, conversion=1):
        """This function allow you to configure all the parameters to encrypting or decrypting.
        All parameters aren't optional !

        :param use_alphabet:
        :param use_caps_alphabet:
        :param use_numbers:
        :param use_more_chars:
        :param conversion:
        """
        if isinstance(use_alphabet, bool) and isinstance(use_caps_alphabet, bool) and isinstance(use_numbers, bool) and isinstance(use_more_chars, bool) and isinstance(conversion, int):
            self.config_alphabet = False
            self.config_caps_alphabet = False
            self.config_numbers = False
            self.config_more_chars = False

            self.configuration_check = False

            self.use_alphabet = use_alphabet
            self.use_caps_alphabet = use_caps_alphabet
            self.use_numbers = use_numbers
            self.use_more_chars = use_more_chars
            self.conversion = conversion

            self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            self.caps_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            self.more_chars = []

            self.pass_alphabet = []
            self.pass_caps_alphabet = []
            self.pass_numbers = []
            self.pass_more_chars = []
        else:
            raise TypeError(
                "use_alphabet, use_caps_alphabet, use_numbers ,use_more_chars and conversion need to be types: bool, bool, bool, bool, int")

    # configuration for alphabet
    def configure_alphabet(self, alphabet: list):
        """This funtion allow you to configure every singles letters that will corespond to single letters of the :
            :arg
            >>> alphabet

            :param configured_alphabet
            :return:
            >>> argument_1 = configured_alphabet
            """
        if isinstance(alphabet, list):
            if self.use_alphabet:
                if len(alphabet) == len(self.alphabet):  # if length are corrects
                    self.pass_alphabet = alphabet
                    self.config_alphabet = True
                else:
                    raise ListLenError(Error[1])
            else:
                raise UnUsedCharsConfiguration(Error[2])
        else:
            raise TypeError(
                "alphabet need to be type: list")

    # configuration for caps alphabet
    def configure_caps_alphabet(self, caps_alphabet: list):
        """This funtion allow you to configure every singles letters that will corespond to single letters of the :
        :arg
        >>> caps_alphabet

        :param configured_caps_alphabet
        :return:
        >>> argument_1 = configured_caps_alphabet
        """
        if isinstance(caps_alphabet, list):
            if self.use_caps_alphabet:
                if len(caps_alphabet) == len(self.caps_alphabet):  # if length are corrects
                    self.pass_caps_alphabet = caps_alphabet
                    self.config_caps_alphabet = True
                else:
                    raise ListLenError(Error[1])
            else:
                raise UnUsedCharsConfiguration(Error[2])
        else:
            raise TypeError(
                "caps_alphabet need to be type: list")

    # configuration for numbers
    def configure_numbers(self, numbers: list):
        """This funtion allow you to configure every singles numbers that will corespond to single numbers of the :
        :arg
        >>> numbers

        :param configured_numbers:
        :return:
        >>> argument_1 = configured_numbers
        """
        if isinstance(numbers, list):
            if self.use_numbers:
                if len(numbers) == len(self.numbers):  # if length are corrects
                    self.pass_numbers = numbers
                    self.config_numbers = True
                else:
                    raise ListLenError(Error[1])
            else:
                raise UnUsedCharsConfiguration(Error[2])
        else:
            raise TypeError(
                "numbers need to be type: list")

    # configuration for special chars
    def configure_more_chars(self, normal_more_chars: list, more_chars: list):
        """If you have configured that you use special characters, this function will work.

        Don't put two same specials characters as (both of parameters):
        :param more_characters:
        :param configured_more_characters:

        Check if both parameters contains the same characters and if they have the same length:
        :return:
        >>> argument_2 = configured_more_chars
        """
        if isinstance(normal_more_chars, list) and isinstance(more_chars, list):
            if self.use_more_chars:
                for char in normal_more_chars:
                    if normal_more_chars.count(char) > 1:
                        raise CharError(Error[0])
                for char in more_chars:
                    if more_chars.count(char) > 1:
                        raise CharError(Error[0])
                if len(normal_more_chars) == len(more_chars):  # if length are corrects
                    for char in normal_more_chars:
                        if char not in more_chars:
                            raise CharError(Error[0])
                    self.more_chars = normal_more_chars
                    self.pass_more_chars = more_chars
                    self.config_more_chars = True
                else:
                    raise ListLenError(Error[1])
            else:
                raise UnUsedCharsConfiguration(Error[2])
        else:
            raise TypeError(
                "normal_more_chars and more_chars need to be types: list and list")

    def check_config(self, raise_mode=True):
        """Check the configuration you entered:
        :param raise_mode: bool -> optional

        :return: True if configuration is correct
                 False if it is not and raise_mode is False
                 raise ConfigurationUnCompleted if it is not and if raise_mode is default (True)
        """
        if isinstance(raise_mode, bool):
            if self.config_alphabet == self.use_alphabet and self.config_caps_alphabet == self.use_caps_alphabet and self.config_numbers == self.use_numbers and self.config_more_chars == self.use_more_chars:
                self.configuration_check = True
                return True
            if raise_mode:
                raise ConfigurationUnCompleted(Error[3])
            else:
                return False
        else:
            raise TypeError(
                "raise_mode need to be type: bool")

    # encrypt function
    def encrypt(self, text: str):
        """Encrypt text with the configuration you entered:
        :param text: str

        :return: reassembled_word if configuration is correct
        """
        if isinstance(text, str):
            if self.configuration_check:
                all_chars = list(text)  # create a list with every chars of the word to encrypt
                for loop in range(self.conversion):  # the word get change the time that we demand
                    for key in range(len(all_chars)):  # this part changes every chars one by one and reassemble the final word
                        if self.use_alphabet:
                            try: all_chars[key] = all_chars[key].replace(all_chars[key], self.pass_alphabet[self.alphabet.index(all_chars[key])])
                            except: pass
                        if self.use_caps_alphabet:
                            try: all_chars[key] = all_chars[key].replace(all_chars[key], self.pass_caps_alphabet[self.caps_alphabet.index(all_chars[key])])
                            except: pass
                        if self.use_numbers:
                            try: all_chars[key] = all_chars[key].replace(all_chars[key], self.pass_numbers[self.numbers.index(all_chars[key])])
                            except: pass
                        if self.use_more_chars:
                            try: all_chars[key] = all_chars[key].replace(all_chars[key], self.pass_more_chars[self.more_chars.index(all_chars[key])])
                            except: pass
                return ''.join(all_chars)
            else:
                raise ConfigurationUnChecked(Error[4])
        else:
            raise TypeError(
                "text need to be type: str")

    # decrypt function
    def decrypt(self, text: str):
        """Decrypt text with the configuration you entered:
        :param text: str

        :return: reassembled_word if configuration is correct
        """
        if isinstance(text, str):
            if self.configuration_check:
                all_chars = list(text)  # create a list with every chars of the word to decrypt
                for loop in range(self.conversion):  # the word get change the time that we demand
                    for key in range(len(all_chars)):  # this part changes every chars one by one and reassemble the final word
                        if self.use_alphabet:
                            try: all_chars[key] = all_chars[key].replace(self.pass_alphabet[self.pass_alphabet.index(all_chars[key])], self.alphabet[self.pass_alphabet.index(all_chars[key])])
                            except: pass
                        if self.use_caps_alphabet:
                            try: all_chars[key] = all_chars[key].replace(self.pass_caps_alphabet[self.pass_caps_alphabet.index(all_chars[key])], self.caps_alphabet[self.pass_caps_alphabet.index(all_chars[key])])
                            except: pass
                        if self.use_numbers:
                            try: all_chars[key] = all_chars[key].replace(self.pass_numbers[self.pass_numbers.index(all_chars[key])], self.numbers[self.pass_numbers.index(all_chars[key])])
                            except: pass
                        if self.use_more_chars:
                            try: all_chars[key] = all_chars[key].replace(self.pass_more_chars[self.pass_more_chars.index(all_chars[key])], self.more_chars[self.pass_more_chars.index(all_chars[key])])
                            except: pass
                return ''.join(all_chars)
            else:
                raise ConfigurationUnChecked(Error[4])
        else:
            raise TypeError(
                "text need to be type: str")

    # char mixer class
    class CharsMixer:
        def __init__(self, var_config: list):
            if isinstance(var_config, list):
                self.var_config = var_config
            else:
                raise TypeError(
                    "var_config need to be type: list")

        # char mixer function
        def mix_chars(self, text: str):
            if isinstance(text, str):
                mixed_chars = ''
                if len(self.var_config) != len(text):
                    raise ListLenError(Error[1])
                all_chars = list(text)
                for key in range(len(text)):
                    mixed_chars += all_chars[self.var_config[key]]
                return mixed_chars
            else:
                raise TypeError(
                    "text need to be type: str")

        # char unravel function
        def unravel_chars(self, text: str):
            if isinstance(text, str):
                unravel_chars = ''
                if len(self.var_config) != len(text):
                    raise ListLenError(Error[1])
                all_chars = list(text)
                for key in range(len(text)):
                    unravel_chars += all_chars[self.var_config.index(key)]
                return unravel_chars
            else:
                raise TypeError(
                    "text need to be type: str")


# random configuration
def random_config(*list_config, list_size: int, var_config: list):
    if isinstance(list_size, int) and isinstance(var_config, list):
        if list_config[0] == str:
            if list_size <= 26:
                if list_config[1] == 'lower':
                    while list_size != len(var_config):
                        value = choice(list(ascii_lowercase))
                        if value not in var_config:
                            var_config.append(value)
                elif list_config[1] == 'upper':
                    while list_size != len(var_config):
                        value = choice(list(ascii_uppercase))
                        if value not in var_config:
                            var_config.append(value)
                else:
                    raise TypeError(Error[7])
            else:
                raise StrListSizeError(Error[5])
        elif list_config[0] == int:
            while list_size != len(var_config):
                value = randint(0, list_size - 1)
                if value not in var_config:
                    var_config.append(value)
        else:
            raise TypeError(Error[6])
        return var_config
    else:
        raise TypeError(
            "list_size and var_config need to be types: int and list")