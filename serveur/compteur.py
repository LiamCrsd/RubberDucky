import time

"""
Ce sript gére le compteur, ie le message qui sera affiché dans la pop up (ca permet d'avoir deux parametre reglable pour la pop up : 
																			le temps d'actualisation (ie combien de temps elle reste affichée avant d'etre actualisée
																			et la vitesse de progression de la barre de chargement))
"""

count = 0
dic = {}
file = "./data.txt"

with open(file, 'r') as f:
	for line in f:
		key, value = line.strip().split(':')
		dic[key.strip()] = value.strip()
mdp = dic["Mdp"]
#On ouvre le fichier et on vérifie si le virus est actif ou non 
var = bool(int(dic["Virus_actif"]))
try:
	with open("./mdp.txt","r") as f:
		verify_mdp = f.readline().strip()
except:
	verify_mdp = ""
var = var & (verify_mdp != mdp)
while var:
	count +=1
	x = int((count/50)*40)
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
	var = var & (verify_mdp != mdp) #On vérifie si le virus est toujour actif
	dic["Compteur"] = "Hack en cours " + "[" + "#"*x + "."*(40-x) + "]" #On fait avancer la barre de chargement
	with open(file, 'w') as f:
		for key, value in dic.items():
			f.write(f"{key} : {value}\n")
	time.sleep(int(dic["Tic_compteur"])) #On attend le temps nécessaire en fonction de la vitesse souhaitée 
