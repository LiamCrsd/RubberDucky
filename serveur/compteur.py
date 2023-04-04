import time
count = 0
dic = {}
file = "./data.txt"
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
	var = var & (verify_mdp != mdp)
	dic["Compteur"] = "Hack en cours " + "[" + "#"*x + "."*(40-x) + "]"
	with open(file, 'w') as f:
		for key, value in dic.items():
			f.write(f"{key} : {value}\n")
	time.sleep(int(dic["Tic_compteur"]))
