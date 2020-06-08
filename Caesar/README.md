
 ▄████████    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
███    █▀    ███    ███   ███    █▀    ███    █▀    ███    ███   ███    ███ 
███          ███    ███  ▄███▄▄▄       ███          ███    ███  ▄███▄▄▄▄██▀ 
███        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀███████████ ▀▀███▀▀▀▀▀   
███    █▄    ███    ███   ███    █▄           ███   ███    ███ ▀███████████ 
███    ███   ███    ███   ███    ███    ▄█    ███   ███    ███   ███    ███ 
████████▀    ███    █▀    ██████████  ▄████████▀    ███    █▀    ███    ███ 
                                                                 ███    ███ 

[*] Uso: ./caesar_cli.sh
      	a) abcedario
        w) word (palabra a encriptar o desencriptar)
        n) numero de rotaciones
        o) opciones
               * encrypt
               * decrypt
        i) incluir "\n","\t"," "(opcional)
        		* True
        		* False
        h) Mostrar este panel de ayuda

example: ./caesar_cli.sh -w "hola que tal" -n 13 -o encrypt

	El script requiere del archivo caesar.py

!(/RandomTools/Caesar/caesar1.png)
!(/RandomTools/Caesar/caesar2.png)
!(/RandomTools/Caesar/caesar3.png)


	Esta herramienta esta orientada a un entorno de terminal (CLI command line interpreter)
	Mayormente las herramientas informaticas, al menos las de seguridadestan siendo desarrolladas
	en lenguajes como python, perl, C, js, bash, etc.

	En este caso he utilizado bash con el fin de mejorar mis habilidades en bash, esto me facilita
	el poder utilizar parametros en la misma aplicacion.
	Esta herramienta puede ser utilizada junto con otras usando comandos de bash para filtrar la 
	salida como por ejemplo:
	"./caesar_cli.sh -w "hola" -o encrypt -n 13 | grep Resultado| cut -d ":" -f 2"
	
