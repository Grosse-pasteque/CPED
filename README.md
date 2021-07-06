# Custom Personal Encrypting and Decrypting {CPED} [3.9.2]

## By Grosse pastèque#6705

-------------

### Configuring the module:

At first, we import and define our configuration:
- What do we want to use
- And how many times we want the module to crypt

```python
import CPED

cped = CPED.CPED('charmap.json', 3)
```

The `charmap.json` file corespong to [charmap](./charmap.json) which contains:
```json
{
    "a":    "v"
    ...
}
```

Here `a` will be transformed in `v` in the first convertion.
*You can also do that `{"a": "vm"}`, so `a` will be transformed into `vm`*

-------------


### Encrypting and Decrypting:

Then we can start encrypting or decrypting:
- encrypt:      `hello GOOD -_- 777`
- decrypt:      the encrypted result

```python
encrypt_word = cped.encrypt("hello GOOD -_- 777")
decrypt_word = cped.decrypt(encrypt_word)

print(encrypt_word)
print(decrypt_word)
```


-------------


### Explanations:
The obtained result is the following :
- encrypt:	`hello GOOD -_- 777` to `jmaap LPPE à(à 222`
- decrypt:	`jmaap LPPE =(= 222` to `hello GOOD -_- 777`


-------------


### Chars encrypting table
    Encrypting transformations

| 0  | h  | e  | l  | l  | o  |  | G  | O  | O  | D  |  | -  | _  | -  |  | 7  | 7  | 7  |
| :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |:------------: |:------------: |
| **1**  | **o** | **j** | **n** | **n** | **e** | | **B** | **E** | **E** | **H** | | **=** | **(** | **=** | | **2** | **2** | **2** |
| **2**  | **e** | **p** | **q** | **q** | **j** | | **R** | **J** | **J** | **O** | | **-** | **_** | **-** | | **7** | **7** | **7** |
| **3**  | **j** | **m** | **a** | **a** | **p** | | **L** | **P** | **P** | **E** | | **=** | **(** | **=** | | **2** | **2** | **2** |



Here we have our charmap :
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
  * `_-+=(`
  * `(=+-_`


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
random_int_config = random_config(
	int,
	list_size=18,
	var_config=my_list_0
)

random_str_lower_config = random_config(
	str,
	'lower',
	list_size=26,
	var_config=my_list_1
)

print(random_int_config)
print(random_str_lower_config)
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
- Our 'random_int_config' mixed int configuration: `[4, 16, 10, 0, 14, 8, 12, 5, 3, 1, 9, 17, 13, 6, 7, 15, 11, 2]`
- Our 'random_str_lower_config' mixed str configuration (not used): `['a', 'n', 'm', 'u', 'v', 'l', 'j', 'q', 'k', 'g', 'x', 'o', 'w', 'i', 'd', 'f', 'e', 't', 'b', 'h', 'y', 'p', 'r', 's', 'c', 'z']`

Mixer will change:
- Our mixed word with 'my_list_0' configuration: `p2 j P( amE2=LP2=a`
- Our unravel word (our crypted word): `jmaap LPPE =(= 222`


And now all indexes are randomized, and the encrypting is even better.

__All code:__ [Complete file example](./example/example.py)


**Infos:**

If you use a charmap with all utf-8 chars which has a lenght of 0x110000: 1114112 and that you shuffled your text, the number of combinaissons for this text will be :

```py
print(cped.proba(text, charmap_len=0x110000 - 1))
```

Aproximately equal to **[Large Number !](./example/combinaissons.txt)**.
*Number lenght is equal to* **10885**