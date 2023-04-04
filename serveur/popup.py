import os

file = "./data.txt"
dic = {}

while True:
	# Lire le contenu du fichier de données
	with open(file, 'r') as f:
		for line in f:
			key, value = line.strip().split(':')
			dic[key.strip()] = value.strip()

	mdp = dic["Mdp"]
	try:
		with open("./mdp.txt","r") as f:
			verify_mdp = f.readline().strip()
	except:
		verify_mdp = ""
	stop_data = dic["Virus_actif"]
	data = dic["Compteur"]
	timer = dic["Tic_compteur"]
	if stop_data == "0" or mdp == verify_mdp:
		break

	# Afficher la pop-up avec le contenu du fichier de données
	os.system(f"zenity --info --text=\"{data}\" --timeout={timer}")
