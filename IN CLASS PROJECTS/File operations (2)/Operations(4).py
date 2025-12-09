# Search existing file
File_Read = open("Football.txt","r")
File_Write = open("Johusa.txt","w")

lines_ssf = set()

for lines in File_Read:
    if lines not in lines_ssf:
        File_Write.write(lines)
        lines_ssf.add(lines)

File_Read.close()
File_Write.close()        