fic = open("script2/data.txt","r")
var = bool(fic.readline())
fic.close()
while var:
  fic = open("script2/data.txt","r")
  var = bool(fic.readline())
  fic.close()
  print("Hack en cours",var)
