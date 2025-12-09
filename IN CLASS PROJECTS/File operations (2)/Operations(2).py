# Printing a splitted file
with open("FO.txt","w")as File:
    File.write("I am Joshua!")
    File.write("I am 10 years old!")
File.close()

with open("Fo.txt","r")as File:
    My_file = File.readlines()
    for e in My_file:
        Word = e.split()
        print(Word)
File.close()