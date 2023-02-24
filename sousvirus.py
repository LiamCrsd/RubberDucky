import time
fic = open("script2/data.txt","r")
var = int((fic.readline())[14:])
fic.close()
count = 0
while var:
  count +=1
  x = int((count/50)*40)
  fic = open("script2/data.txt","r")
  var = int((fic.readline())[14:])
  fic.close()
  print("Hack en cours " + "[" + "#"*x + "."*(40-x) + "]" )
  time.sleep(1)
print("Echec du Hack")
