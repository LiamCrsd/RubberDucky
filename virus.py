import os
import time
import random
listeCommandeLinux = ["gnome-terminal -- script2/sousvirus.py", "gnome-terminal -- hollywood"]
if os.name == "nt":
  for i in range(50):
    os.system("start python script2/sousvirus.py")
    time.sleep(1)
else:
  for i in range(20):
    os.system(random.choice(listeCommandeLinux))
    time.sleep(1)
