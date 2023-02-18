import os
import time
if os.name == "nt":
  for i in range(50):
    os.system("start")
else:
  for i in range(20):
    os.system("gnome-terminal -- hollywood")
    time.sleep(1)
