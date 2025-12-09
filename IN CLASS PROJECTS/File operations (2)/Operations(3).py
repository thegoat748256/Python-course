# Creating a new file
new_file = open("Johusa.txt","x")
new_file.close()

import os
if os.path.exists("FO.txt"):
    os.remove("FO.txt")
else:
    print("No such file exists.")