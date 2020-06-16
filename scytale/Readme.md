```

        ███████╗ ██████╗██╗   ██╗████████╗ █████╗ ██╗     ███████╗
        ██╔════╝██╔════╝╚██╗ ██╔╝╚══██╔══╝██╔══██╗██║     ██╔════╝
        ███████╗██║      ╚████╔╝    ██║   ███████║██║     █████╗
        ╚════██║██║       ╚██╔╝     ██║   ██╔══██║██║     ██╔══╝
        ███████║╚██████╗   ██║      ██║   ██║  ██║███████╗███████╗
        ╚══════╝ ╚═════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝



usage: escitala.py [-h] -t TEXT -e EDGES -o {encrypt,decrypt} [-p [POSITIONS]]

Vigenere cypher

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  text to encrypt or decrypt
  -e EDGES, --edges EDGES
                        set the number of edges of the escitala
  -o {encrypt,decrypt}, --option {encrypt,decrypt}
  -p [POSITIONS], --positions [POSITIONS]
                        A list separated by comas to enter the order in which
                        you are writing on the escitalo
                        
```
## Help

    ./scytale.py -h
![img1](/scytale/scytale1.png)

## Encriptar (orden por defecto)

     ./scytale.py -t VAMOSALEERMUNDOINFORMATICO -e 8 -o encrypt

![img2](/scytale/scytale2.png)

## Encriptar  con un orden especifico

     ./scytale.py -t VAMOSALEERMUNDOINFORMATICO -e 8 -o encrypt

![img3](/scytale/scytale3.png)

## Desencriptar  con un orden especifico

    ./scytale.py -t "NMVS NCEDAAA FOROTML O MIIOE R U" -e 8 -o decrypt -p 3,5,0,1,7,4,6,2

![img4](/scytale/scytale4.png)
