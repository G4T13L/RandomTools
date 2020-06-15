#!/usr/bin/python3
# -*- coding: utf-8 -*-

def vigenere_enc(text, key, alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"):
    alphabet=alphabet.upper()
    enc_string = ""

    key = key.upper()

    text = text.upper()

    text_len = len(text)

    new_key = key
    new_key_length = len(new_key)

    while new_key_length < text_len:
        new_key = new_key + key
        new_key_length = len(new_key)

    pos = 0

    for letter in text:
        if letter in alphabet:
    
            position = alphabet.find(letter)
    
            key_character = new_key[pos]
            key_character_position = alphabet.find(key_character)
            pos += 1
    
            new_position = position + key_character_position
            if new_position > len(alphabet)-1:
                new_position = new_position - len(alphabet)
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    
    return(enc_string)


def vigenere_dec(text, key, alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"):
    alphabet=alphabet.upper()    
    dec_string = ""

    key = key.upper()

    text = text.upper()

    text_len = len(text)

    new_key = key
    new_key_length = len(new_key)

    while new_key_length < text_len:
    
        new_key = new_key + key
        new_key_length = len(new_key)

    pos = 0

    for letter in text:
        if letter in alphabet:
    
            position = alphabet.find(letter)
    
            key_character = new_key[pos]
            key_character_position = alphabet.find(key_character)
            pos += 1
    
            new_position = position - key_character_position
            if new_position > len(alphabet)-1:
                new_position = new_position + len(alphabet)
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return(dec_string)



# Testing
# print(vigenere_enc("UNIVERSIDAD NACIONAL DE INGENIERÍA","covidxix" ))
# print(vigenere_dec())
