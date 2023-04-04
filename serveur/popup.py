import os

file = "./data.txt"
dic = {}

while True:
	# Lire le contenu du fichier de données
	with open(file, 'r') as f:
		for line in f:
			key, value = line.strip().split(':')
			dic[key.strip()] = value.strip()


	stop_data = dic["Virus_actif"]
	data = dic["Compteur"]
	timer = dic["Tic_compteur"]
	if stop_data == "0":
		break

	# Afficher la pop-up avec le contenu du fichier de données
	os.system(f"zenity --info --text=\"{data}\" --timeout={timer}")
