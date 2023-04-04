import random
import time

dic = {}
file = "./data.txt"

def generate_random_text():
    words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
    sentence = ' '.join(random.sample(words, random.randint(3, 8)))
    return " " * random.randint(0,10) + sentence

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
