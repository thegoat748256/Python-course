# File open read close
print("_____________________________________________")
file = open("Sample_File.txt")
print(file.read())
file.close()
print("_____________________________________________")

# file print 10 character
file = open("Sample_File.txt")
print(file.read(10))
file.close()
print("_____________________________________________")

print("_____________________________________________")
# File print first line
file = open("Sample_File.txt")
print(file.readline())
file.close()
print("_____________________________________________")

# File print 4 lines
print("_____________________________________________")
file = open("Sample_File.txt")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
print("_____________________________________________")


# file looping
print("_____________________________________________")
file = open("Sample_File.txt")
for a in file:
    print(a)
file.close()
print("_____________________________________________")