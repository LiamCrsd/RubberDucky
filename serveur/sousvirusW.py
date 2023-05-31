import random
import time

"""
Il s'agit du script du sous virus pour windows 
Le but est pour l'instant d'ouvrir un maximum de fenetre de cmd en affichant des message dedans 
"""

dic = {}
file = "./data.txt"

def generate_random_text():	#Actuellement on génére des phrase random a afficher
    words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
    sentence = ' '.join(random.sample(words, random.randint(3, 8)))
    return " " * random.randint(0,10) + sentence

with open(file, 'r') as f:
    for line in f:
        key, value = line.strip().split(':')
        dic[key.strip()] = value.strip()

mdp = dic["Mdp"]
var = bool(int(dic["Virus_actif"])) #On vérife toujours que le virus est bien actif 
try:
	with open("./mdp.txt","r") as f:
		verify_mdp = f.readline().strip()
except:
	verify_mdp = ""
var = var & (verify_mdp != mdp)

while var:
	with open(file, 'r') as f:
		for line in f:
			key, value = line.strip().split(':')
			dic[key.strip()] = value.strip()
	mdp = dic["Mdp"]
	var = bool(int(dic["Virus_actif"]))
	try:
		with open("./mdp.txt","r") as f:
			verify_mdp = f.readline().strip()
	except:
		verify_mdp = ""
	var = var & (verify_mdp != mdp)
	random_text = generate_random_text()
	print(random_text)
	time.sleep(1)
