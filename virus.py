import os
import time
if os.name == "nt":
  for i in range(50):
    os.system("start python script2/script3.py")
    time.sleep(1)
else:
  for i in range(20):
    os.system("gnome-terminal -- hollywood")
    time.sleep(1)
