import os
if os.name == "nt":
  for i in range(50):
    os.system("start")
else:
  for i in range(10):
    os.system("gnome-terminal")
