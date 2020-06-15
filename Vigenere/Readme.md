"""
  _   ___                                 _      __
 | | / (_)__ ____ ___  ___ _______   ____(_)__  / /  ___ ____
 | |/ / / _ `/ -_) _ \/ -_) __/ -_) / __/ / _ \/ _ \/ -_) __/
 |___/_/\_, /\__/_//_/\__/_/  \__/  \__/_/ .__/_//_/\__/_/
       /___/                            /_/

usage: vigenere.py [-h] -t TEXT -k KEY -o {encrypt,decrypt} [-d [DICTIONARY]]

Vigenere cypher

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  text to encrypt or decrypt
  -k KEY, --key KEY     key to use in the cipher
  -o {encrypt,decrypt}, --option {encrypt,decrypt}
  -d [DICTIONARY], --dictionary [DICTIONARY]
                        dictionary to use in the cipher
                        """
## Help

    ./vigenere.py -h
![img1](/Vigenere/vigenere1.png)

## Encriptar

    ./vigenere.py -t "UNIVERSIDAD NACIONAL DE INGENIERÍA" -k "covidxix" -o encrypt

![img2](/Vigenere/vigenere2.png)

## Desencriptar

    ./vigenere.py -t "XBCCHOAFFOX UDZQLPOF LH FUDGBCMVÍX" -k "covidxix" -o encrypt

![img3](/Vigenere/vigenere3.png)

