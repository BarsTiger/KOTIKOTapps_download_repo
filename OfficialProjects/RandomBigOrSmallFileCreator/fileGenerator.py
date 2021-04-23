import os, shutil, random
slash = '\\'
chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
         'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
         'z', 'x', 'c', 'v', 'b', 'n', 'm']

input("KOTIKOT, all rights reserved \nPress Enter to start...")

nameoffile = input("Enter name of file: ")

mode = int(input("Enter mode of file generating \n "
                 "1 - random numbers and letters \n "
                 "2 - repeating your word or symbol \n "
                 "Enter here: "))
if mode == 1:
    length = int(input('Enter length of file: '))
    fileik = open(nameoffile + '.txt', "w+")
    for i in range(length):
         fileik.write(chars[random.randint(0, len(chars)) - 1])
    fileik.close()

elif mode == 2:
    povtors = int(input('Enter number of repeats in file: '))
    word = input('Enter word or symbol, that will be repeated: ')
    fileik = open(nameoffile + '.txt', "w+")
    for i in range(povtors):
         fileik.write(word * povtors)
    fileik.close()


wheretosave = "D:"
if input('Do you want to save file NOT to D:drive (y/n, y is to enter your path, n - save to D:\): ') == "y":
     wheretosave = input("Print path to your folder: ")
shutil.move(nameoffile + ".txt", wheretosave + slash + nameoffile + ".txt")

input("All worked, press Enter to exit program...")