import os
# With and write function
with open("Sample_File.txt","w")as f:
    f.write("Hello! my name is Joshua.")
f.close()

# Split into words and print
with open("Sample_File.txt","r")as f:
    data = f.readlines()
    for line in data:
        splitter = line.split()
        print(splitter)
f.close()

# Check if the file exists or not
if os.path.exists("My_File.txt"):
    print("File exists.")
else:
    print("File does not exist.")
    My_File = open("My_File.txt","w")
    My_File.write("Hello my name is Joshua. I like to play sports. An example of what I like playing is Football. ")
    My_File.close()

# Deleting the file
os.remove("Sample_File.txt")
f.close()