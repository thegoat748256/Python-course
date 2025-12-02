# Locating
counter = 0
File = open("File handling.txt")
content_File = File.read()
splitted_file = content_File.split("\n")

for i in splitted_file:
    if i:
        counter = counter + 1

print(counter)        