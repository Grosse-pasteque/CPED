# Custom Personal Encrypting and Decrypting {CPED} [3.9.4]

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
__**ADVICE**__: If you use this feature you will need to use separators.


-------------


### Encrypting and Decrypting:

Then we can start encrypting or decrypting:
- encrypt:      `hello GOOD -_- 777`
- decrypt:      the encrypted result

```python
encrypted = cped.encrypt("hello GOOD -_- 777")
decrypted = cped.decrypt(encrypted)

print(encrypted)
print(decrypted)
```


-------------


### Separators:

Separators can be used if you want but if your config values does not all have a lenght of 1, you must use separators.
To use them, add a key `separators` like below:
```json
{
    "separators": ["separator", ...]
}
```

The list contains all the separators you want to use.
A separator can't be equel to a key value otherwise the module will not work.

Example:
```json
{
    "separators": ["cba", "aba"],

    "a": "bc",
    "b": "ac",
    "c": "ba"
}
```

```py
print(cped.encrypt('abc'))

```

The result can be ( **[separator]** ):
bc[aba]ac[cba]ba : bcabaaccbaba
bc[cba]ac[aba]ba : bccbaacababa

Because separators a placed randomly, but there a decrypted the same way so the decrypted result is always `abc`, *Great !*

__**WARNING**__: Make sure that separators have no letters in common, like that ["as", "dz", "zk"] `z` is common to `dz` and `zk`


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
random_int_config = CPED.random_config(int, list_size=18)
random_str_lower_config = CPED.random_config(str, 'lower')

print(random_int_config)
print(random_str_lower_config)
```
- Define the core of our CharsMixer with the `random_int_config` as his configuration.


```python
mixer = cped.CharsMixer(random_int_config)
```

- Define our random configuration
    - **WARNING** : CharsMixer configuration must be a list filled with `int` values (indexes)


- Mix our encrypted word `encrypted` to make it even worst to decrypt

```python
mixed_word = mixer.mix_chars(encrypted)
print(mixed_word)
```
- Unravel the mixed word `mixed_word` to get `encrypted`

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
- Our mixed word with 'random_int_config' configuration: `p2 j P( amE2=LP2=a`
- Our unravel word (our crypted word): `jmaap LPPE =(= 222`


And now all indexes are randomized, and the encrypting is even better.

__All code:__ [Complete file example](./example/example.py)


**Infos:**

If you use a charmap with all utf-8 chars which has a lenght of 0x110000: 1114112 and that you shuffled your text, the number of combinaissons for this text will be :

```py
print(cped.combinaissons(text, charmap_len=0x110000 - 1))
```

Aproximately equal to **[Large Number !](./example/combinaissons.txt)**.
*Number lenght is equal to* **10885**