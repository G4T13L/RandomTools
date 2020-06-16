#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
posicional_1 edges
posicional_2 text
opcional_1 positions
opcional_2 option encrypt decrypt
"""
print (str(GreenColor)+"""

	███████╗ ██████╗██╗   ██╗████████╗ █████╗ ██╗     ███████╗
	██╔════╝██╔════╝╚██╗ ██╔╝╚══██╔══╝██╔══██╗██║     ██╔════╝
	███████╗██║      ╚████╔╝    ██║   ███████║██║     █████╗  
	╚════██║██║       ╚██╔╝     ██║   ██╔══██║██║     ██╔══╝  
	███████║╚██████╗   ██║      ██║   ██║  ██║███████╗███████╗
	╚══════╝ ╚═════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                                          
	                                                            
	"""+str(ResetColor))

parser = argparse.ArgumentParser(description='Vigenere cypher')

parser.add_argument('-t', '--text', required=True,help='text to encrypt or decrypt')
parser.add_argument('-e', '--edges', required=True,help='set the number of edges of the escitala')

parser.add_argument('-o', '--option', required=True, choices=['encrypt', 'decrypt'], default="encrypt")

parser.add_argument('-p', '--positions', help='A list separated by comas to enter the order in which you are writing on the escitalo', nargs='?')

args = parser.parse_args()

text = args.text
edges = int(args.edges)
option = args.option
positions = args.positions

from math import *
def escitala(n,v,l,texto,orden1,orden2):
    M = []
    k=0
    for i in range(n):
        f = []
        for j in range(v):
            if( l > i*v+j ):
                f.append( texto[k]) #str(i)+","+str(j)+" -> "+str(i*v+j)  ) #
                k+=1
            else:
                f.append(" ")
        M.append(f)
    salida = ""
    lista = []
    print ()
    for i in orden1:
        for j in orden2:
            print (str(M[j][i]), end=", ")
            salida=salida+M[j][i]
            lista.append(M[j][i])
        print ()
    # print (salida)
    print ()
    # print(M)
    return salida

def encrypt(n,texto,orden2=""):
    l = len(texto)
    v = ceil(l/n)
    # print(texto)
    if(orden2==""):
        # print("defecto")
        orden2=range(n)
    orden1=range(v)
    return escitala(n,v,l,texto,orden1,orden2)

def decrypt(v,texto,orden1=""):
    l = len(texto)
    n = ceil(l/v)
    if(orden1==""):
        # print("defecto")
        orden1=range(v)
    else:
        c = []
        for i in range(len(orden1)):
            c.append(orden1.index(i))
        orden1=c
    orden2=range(n)
    return escitala(n,v,l,texto,orden1,orden2)

# salida = encrypt(8,"VAMOSALEERMUNDOINFORMATICO")
# salida = encrypt(8,"VAMOSALEERMUNDOINFORMATICO",[3,5,0,1,7,4,6,2])
# decrypt(8,'NMVS NCEDAAA FOROTML O MIIOE R U',[3,5,0,1,7,4,6,2])

print (str(CyanColor)+"[*] Text: "+str(ResetColor)+str(YellowColor)+text+str(ResetColor))
print (str(CyanColor)+"[*] Edges: "+str(ResetColor)+str(YellowColor)+str(edges)+str(ResetColor))
print (str(CyanColor)+"[*] Option: "+str(ResetColor)+str(YellowColor)+str(option.upper())+str(ResetColor))
if positions!=None:
	# print (positions.split(","))
	pos = []
	positions= positions.split(",")
	for i in positions:
		pos.append(int(i))
	print (str(CyanColor)+"[*] Positions:"+str(ResetColor)+str(YellowColor)+str(pos)+str(ResetColor))

	if option=="encrypt":
		print (str(GreenColor)+'\t[*] Result:'+ str(ResetColor) + encrypt(edges,text,pos))
	else:
		print (str(GreenColor)+'\t[*] Result:'+ str(ResetColor) + decrypt(edges,text,pos))
else:
	print (str(CyanColor)+"[*] Positions:"+str(ResetColor)+str(RedColor)+'DEFAULT'+str(ResetColor))
	if option=="encrypt":
		print (str(GreenColor)+'\t[*] Result:'+ str(ResetColor) + encrypt(edges,text))
	else:
		print (str(GreenColor)+'\t[*] Result:'+ str(ResetColor) + decrypt(edges,text))

print()