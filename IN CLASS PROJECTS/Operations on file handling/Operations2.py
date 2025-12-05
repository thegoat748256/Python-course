# removing certain lines
This_File = open("File operations.txt","r")
new_File = open("new file.txt","w")

for i in This_File.readlines():
    if not (i.startswith("Coding")):
        print(i)
        new_File.write(i)

This_File.close()
new_File.close()            