# Custom Personal Encrypting and Decrypting {CPED} [3.8.7]

-------------

## By Grosse pastèque#6705

Free program used for Custom Personal Encrypting and Decrypting (CPED)
You can share this program to whoever you want but don't use it for economics purposes.
-------------
### Configuring the module:
At first, we import and define our configuration:
- What do we want to use
- And how many times we want the module to crypt
```python
import main as CPED

cped = CPED.CPED(True, True, True, True, 3)
```
Then we configure each data list that we chose to use:
- alphabet
- caps alphabet
- numbers
- more chars
```python
cped.configure_alphabet(['v', 'r', 'z', 'h', 'j', 'c', 'b', 'o', 't', 'p', 'd', 'n', 'g', 'q', 'e', 'm', 'a', 'l', 'f', 'w', 'x', 's', 'i', 'y', 'u', 'k'])
cped.configure_caps_alphabet(['V', 'R', 'Z', 'H', 'J', 'C', 'B', 'O', 'T', 'P', 'D', 'N', 'G', 'Q', 'E', 'M', 'A', 'L', 'F', 'W', 'X', 'S', 'I', 'Y', 'U', 'K'])
cped.configure_numbers(['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'])
cped.configure_more_chars(['_', '-', 'é', 'à', '('], ['(', 'à', 'é', '-', '_'])
```
-------------
### Checking, Encrypting and Decrypting:
Then we can verify our configuration by simply checking with the `check_config()` that return `True` if the config is correct.

Then we can start encrypting or decrypting:
- encrypt `hello GOOD -_- 777`
- decrypt the encrypted result 
```python
if cped.check_config():
    encrypt_word = cped.encrypt("hello GOOD -_- 777")
    print(encrypt_word)
    decrypt_word = cped.decrypt(encrypt_word)
    print(decrypt_word)
else:
    print("Configuration not correct !")
```

-------------
### Explanations:
The obtained result is the following :
- encrypt:  `hello GOOD -_- 777`   -(to)>    `jmaap LPPE à(à 222`
- decrypt:  `jmaap LPPE à(à 222`   -(to)>    `hello GOOD -_- 777`
-------------
### Chars encrypting table 
    Encrypting transformations

| 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|
|h|o|e|j|
|e|j|p|m|
|l|n|q|a|
|l|n|q|a|
|o|e|j|p|
|G|B|R|L|
|O|E|J|P|
|O|E|J|P|
|D|H|O|E|
|-|à|-|à|
|_|(|_|(|
|-|à|-|à|
|7|2|7|2|
|7|2|7|2|
|7|2|7|2|

Here we have our configuration compared to the basic lower alphabet :
* #### Alphabet:
    * `abcdefghijklmnopqrstuvwxyz`
    * `vrzhjcbotpdngqemalfwxsiyuk`
* #### Caps Alphabet:    
  * `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
  * `VRZHJCBOTPDNGQEMALFWXSIYUK`
* #### Numbers:
  * `0123456789`
  * `9876543210`
* #### Other chars:
  * `_-éà(`
  * `(àé-_`
-------------
### Random configuration:
We can also use a random configuration and randomize our encrypted text, like that :
- Lists to save our random configurations.
```python
my_list_0 = []
my_list_1 = []
```
- Define the core of our CharsMixer with the `my_list_0` as his configuration.
```python
mixer = cped.CharsMixer(my_list_0)
```
- Define our random configuration
    - **WARNING** : CharsMixer configuration must be a list filled with `int` values (indexes)
    - **WARNING** : Str configuration works only for `configure_alphabet(list)` and `configure_caps_alphabet(list)`
```python
random_int_config = random_config(int, list_size=18, var_config=my_list_0)
random_str_upper_config = random_config(str, 'lower', list_size=26, var_config=my_list_1)

print(random_int_config)
print(random_str_upper_config)
```
- Mix our encrypted word `encrypt_word` to make it even worst to decrypt
```python
mixed_word = mixer.mix_chars(encrypt_word)
print(mixed_word)
```
- Unravel the mixed word `mixed_word` to get `encrypt_word`
```python
unravel_word = mixer.unravel_chars(mixed_word)
print(unravel_word)
```
-------------
#### Obtained results:
Lists will become:
- Our 'my_list_0' mixed int configuration: `[4, 16, 10, 0, 14, 8, 12, 5, 3, 1, 9, 17, 13, 6, 7, 15, 11, 2]`
- Our 'my_list_1' mixed str configuration (not used): `['a', 'n', 'm', 'u', 'v', 'l', 'j', 'q', 'k', 'g', 'x', 'o', 'w', 'i', 'd', 'f', 'e', 't', 'b', 'h', 'y', 'p', 'r', 's', 'c', 'z']`

Mixer will change:
- Our mixed word with 'my_list_0' configuration: `p2 j P( amE2àLP2àa`
- Our unravel word (our crypted word): `jmaap LPPE à(à 222`

| 0 | 1 |
|:---:|:---:|
|j|p|
|m|2|
|a| |
|a|j|
|p| |
| |P|
|L|(|
|P| |
|P|a|
|E|m|
| |E|
|à|2|
|(|à|
|à|L|
| |P|
|2|2|
|2|à|
|2|a|
-------------

And now all indexes are randomized, and the encrypting is even better, we can also do:
```python
for loop in range(10):
    mixed_word = mixer.mix_chars(encrypt_word)
print(mixed_word)
```
But I chose an easy way to show it.

__All the code view in this README file:__ [Complete file example](example_file.py)