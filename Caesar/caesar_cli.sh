#!/bin/bash
# caesar y pa' dentro

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function helpPanel(){
	echo -e "${grayColour} ▄████████    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████ "
	echo -e "███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ "
	echo -e "███    █▀    ███    ███   ███    █▀    ███    █▀    ███    ███   ███    ███ "
	echo -e "███          ███    ███  ▄███▄▄▄       ███          ███    ███  ▄███▄▄▄▄██▀ "
	echo -e "███        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀███████████ ▀▀███▀▀▀▀▀   "
	echo -e "███    █▄    ███    ███   ███    █▄           ███   ███    ███ ▀███████████ "
	echo -e "███    ███   ███    ███   ███    ███    ▄█    ███   ███    ███   ███    ███ "
	echo -e "████████▀    ███    █▀    ██████████  ▄████████▀    ███    █▀    ███    ███ "
	echo -e "                                                                 ███    ███ ${endColour}"

	echo -e "\n${yellowColour}[*]${endColour}${grayColour} Uso: ./caesar_cli.sh${endColour}"
	echo -e "\n\t${blueColour}a)${endColour}${greenColour} abcedario${endColour}"
	echo -e "\t${blueColour}w)${endColour}${greenColour} word (palabra a encriptar o desencriptar)${endColour}"
	echo -e "\t${blueColour}n)${endColour}${greenColour} numero de rotaciones${endColour}"
	echo -e "\t${blueColour}o)${endColour}${greenColour} opciones${endColour}"
	echo -e "\t\t${turquoiseColour}*${endColour}${turquoiseColour} encrypt${endColour}"
	echo -e "\t\t${turquoiseColour}*${endColour}${turquoiseColour} decrypt${endColour}"
	echo -e "\t${blueColour}i)${endColour}${greenColour}  incluir '\\\n','\\\t',' '(opcional)${endColour}"
	echo -e "\t\t${turquoiseColour}*${endColour}${turquoiseColour} True${endColour}"
	echo -e "\t\t${turquoiseColour}*${endColour}${turquoiseColour} False${endColour}"
	echo -e "\t${blueColour}h)${endColour}${greenColour} Mostrar este panel de ayuda${endColour}\n"
	exit 0
}

function start_caesar(){

	if [ $activado == 0 ]; then
		ignore="False"
	else
		if ! [[ "$ignore" ==  "True" || "$ignore" == "False" ]]; then
			echo -e "\n${redColour} Mal uso del argumento -i${endColour}\n"
			return 1
		fi
	fi
		
	if [[ "$abc" == "" ]]; then
		if [[ "$option" == "encrypt" ]]; then			
			res=$(echo $(python3 -c "from caesar import *; test=Caesar(); print (test.encrypt('$word',$number,$ignore))"))
		else
			if [[ "$option" == "decrypt" ]]; then
				res=$(echo $(python3 -c "from caesar import *; test=Caesar(); print (test.decrypt('$word',$number,$ignore))"))
			else
				echo -e "\n${redColour}Opcion incorrecta${endColour}\n"
				return 1
			fi
		fi
	else
		if [[ "$option" == "encrypt" ]]; then
			res=$(echo $(python3 -c "from caesar import *; test=Caesar('$abc'); print (test.encrypt('$word',$number,$ignore))"))
		else
			if [[ "$option" == "decrypt" ]]; then
				res=$(echo $(python3 -c "from caesar import *; test=Caesar('$abc'); print (test.decrypt('$word',$number,$ignore))"))
			else
				echo -e "\n${redColour}Opcion incorrecta${endColour}\n"
				return 1
			fi
		fi
	fi
	echo -e "\n${blueColour}[*] Palabra Original:${endColour}${grayColour}$word${endColour}"
	echo -e "\n${blueColour}[*] Numero de rotaciones:${endColour}${grayColour}$number${endColour}"
	echo -e "\n${blueColour}[*] Opcion:${endColour}${grayColour}$option${endColour}"
	echo -e "\n${blueColour}[*] Resultado:${endColour}${grayColour}$res${endColour}\n"
}

declare -i parameter_counter=0; declare -i activado=0; while getopts ":a:w:n:o:i:h:" arg; do
	case $arg in
		a) abc=$OPTARG;;
		w) word=$OPTARG; let parameter_counter+=1 ;;
		n) number=$OPTARG; let parameter_counter+=1 ;;
		o) option=$OPTARG; let parameter_counter+=1 ;;
		i) ignore=$OPTARG; let activado=1 ;;
		h) helpPanel;;
	esac
done

if [ $parameter_counter -lt 3 ]; then
	helpPanel
else
	if [[ "$abc" == "" ]]; then
		echo -e "${purpleColour}[*] abcdario seleccionado por defecto${endColour}"
	else
		echo -e "${turquoiseColour}[*] abcdario escogido:$abc ${endColour}"
	fi
	start_caesar
fi
