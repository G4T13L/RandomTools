#!/usr/bin/python3
import sys
import argparse

BlackColor = '\u001b[30m'
RedColor = '\u001b[31m'
GreenColor = '\u001b[32m'
YellowColor = '\u001b[33m'
BlueColor = '\u001b[34m'
MagentaColor = '\u001b[35m'
CyanColor = '\u001b[36m'
WhiteColor = '\u001b[37m'
ResetColor = '\u001b[0m'

"""
posicional_1 texto
posicional_2 clave
opcional_1 diccionario
opcion: desencryptar encryptar
"""
print (str(YellowColor)+"""
  _   ___                                 _      __          
 | | / """+str(RedColor)+"""(_)"""+str(YellowColor)+"""__ ____ ___  ___ _______   ____"""+str(RedColor)+"""(_)"""+str(YellowColor)+"""__  / /  ___ ____
 | |/ / / _ `/ -_) _ \\/ -_) __/ -_) / __/ / _ \\/ _ \\/ -_) __/
 |___/_/\\_, /\\__/_//_/\\__/_/  \\__/  \\__/_/ .__/_//_/\\__/_/   
       /___/                            /_/                  
	"""+str(ResetColor))

parser = argparse.ArgumentParser(description='Vigenere cypher')

parser.add_argument('-t', '--text', required=True,help='text to encrypt or decrypt')
parser.add_argument('-k', '--key', required=True,help='key to use in the cipher')

parser.add_argument('-o', '--option', required=True, choices=['encrypt', 'decrypt'], default="encrypt")

parser.add_argument('-d', '--dictionary', help='dictionary to use in the cipher', nargs='?')

args = parser.parse_args()

text = args.text
key = args.key

from vigenere_lib import *
if (args.dictionary == None):
	print (str(YellowColor)+"[*] Default dictionary")
else:
	print (str(MagentaColor)+"[*] Dictionary:"+args.dictionary.upper())
print (str(MagentaColor)+"[*] Text: "+args.text)
print (str(MagentaColor)+"[*] Key: "+args.key)
print (str(MagentaColor)+"[*] Option: "+args.option)

print (str(CyanColor)+"\nResult:"+str(ResetColor), end='')
if (args.option == 'encrypt'):
	if (args.dictionary == None):
		print( vigenere_enc(text, key) )
	else:
		print( vigenere_enc(text, key, args.dictionary) )
else:
	if (args.dictionary == None):
		print( vigenere_dec(text, key) )
	else:
		print( vigenere_dec(text, key, args.dictionary) )
	
print()
