#Importation des modules
from os import system

#Selectionner une option
print('[1] scan 1 ip\n\n[2] scan an ip range\n')

s = input('Select your option  > ')
if s == '1':
	#Scan 1 ip
	ip = input('Select your ip > ')
	system('ping -c 1 {}'.format(ip)) #ICMP protocol

elif s == '2':
	cycle = input('select your ip network : (192.168.1.1) > ')#Choisi l'addresse ip de ton reseau
	a = input('Select the range to start > ')#choisi le debut d'une addresse ip machine, qui sera le debut de la boucle for
	a = int(a)#Convertion en int pour pouvoir l'introduire dans la range/boucle for
	
	b = input('Select tthe range to finish > ')#Choisi la fin d'une addresse ip machine qui sera la fin de la boucle for
	b = int(b)#Convertion en int, sans la variable cycle b et a = 192.168.1.{}, ce n'est pas un nombre donc
	#une erreur va se produire, b et a ne sont pas des nombres entier !
	#Donc a et b sont a l'ip machine de debut et de fin et cycle l'ip reseau, pour eviter l'erreur
	long = a#long egale a car long nous servira a definir l'ip etant donner que 'a' est statique, et qui si je fais bouger 'a' je vais modifier la boucle for
	for ping in range(a, b):
		system('ping -c 1 {}{}'.format(cycle, long))#Ici on donne d'abord cycle qui est l'addresse ip reseau
		#et ensuite long qui est egale a 'a' long permet
		long = long + 1#repete l'action mais avec l'addresse ip suivante
