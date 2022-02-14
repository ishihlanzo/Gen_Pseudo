from random import randint		#Import the package random

def generateur_pseudo(longueur) :		#the program
	
	#all the 'thing' you need for the program
	
	voyelle = ['a','e','i','o','u']
	pseudo = ''
	consone = 1
	pseudo_upper = ''
	pseudo_final =''
	
	#the actual program
	
	for i in range(longueur) :
		pseudo += chr(randint(97, 122))		#add a new letter
		if pseudo[len(pseudo)-1] not in voyelle :		#if it's not a voyelle
			consone +=1			#add 1 to consone
		if consone >= 2 : 		#if there is 2 consone d'affilé
			pseudo+=voyelle[randint(0,4)]		#add a voyelle
			consone = 0			#set 'consone' to 0
	
	#make the pseudo look nicer
	
	pseudo_upper = pseudo.upper()
	pseudo_final += pseudo_upper[0]
	pseudo_final += pseudo[1:]
	
	#print the pseudo
	
	print(f'Your new pseudo is {pseudo_final}')

LEN_PSEUDO = 5		#set the len of your pseudo here

generateur_pseudo(LEN_PSEUDO)		#do you really ask you what tha thing do x) ?




