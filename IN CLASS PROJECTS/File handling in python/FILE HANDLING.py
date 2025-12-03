# reading
File = open("File handling.txt")
print(File.read())
File.close()

# writing
File_writing = open("File handling.txt","w")
File_writing.write("I have lots of friends here in Chennai.")
File_writing.close()

# appending
File_appending = open("File handling.txt","a")
File_appending.write("I have lots of friends here in Chennai.")
File_appending.close()