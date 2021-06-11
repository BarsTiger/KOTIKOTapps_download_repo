import time, sys

name1 = []
name2 = []

flames = ["F lame", "f L ame", "fl A me", "flam E"]
flame = ["f", "l", "a", "m", "e"]
biglettersflame = {"f": "Ḟ", "l": "Ḷ", "a": "Ḁ", "m": "Ṃ", "e": "Ẹ"}
biglettersflame2 = {"f": "F", "l": "L", "a": "A", "m": "M", "e": "E"}

def printinator(spisok, probeli):
    slovo = ""
    if probeli == True:
        for bukva in spisok:
            slovo = slovo + bukva
            slovo = slovo + " "
    else:
        for bukva in spisok:
            slovo = slovo + bukva
    print(slovo)

def comparator():
    for o in name1:
        while o in name2:
            name2.remove(o)
            printinator(name2, False)
            while o in name1:
                name1.remove(o)
                printinator(name1, False)
    for o in name2:
        while o in name1:
            name1.remove(o)
            printinator(name1, False)
            while o in name2:
                name2.remove(o)
                printinator(name2, False)

def printflame(index):
    slovo = ""
    for o in range(len(flame)):
        if o != index - 1:
            slovo = slovo + flame[o]
        else:
            slovo = slovo + biglettersflame[flame[o]]
    print('\b' * 10, end=' ')
    print(format(slovo), end=' ')
    sys.stdout.flush()

name1str = input("Enter name of first person (all letters should be small): ")
name2str = input("Enter name of second person (all letters should be small): ")

for letter in name1str:
    name1.append(letter)

printinator(name1, False)

for letter in name2str:
    name2.append(letter)

printinator(name2, False)

print("")
print("Deleting letters, that both names contain")
comparator()
print("")
print("Now we have:")
printinator(name1, False)
printinator(name2, False)

dlina = len(name1) + len(name2)
print("Lengths of two names is: " + str(dlina))
print("Now check:")
printinator(flame, False)
print("")

i = -1
j = -1
peredudaleniemi = 0



while len(flame) > 1:
    while j < dlina:
        i = i + 1
        j = j + 1
        if i > len(flame):
            i = -1
        printflame(i)
        time.sleep(0.4)
    if len(flame) > 1:
        if dlina <= len(flame):
            del flame[dlina - 1]
        else:
            del flame[(dlina % len(flame)) - 1]
            j = 0
            i = 0


print('\b' * 10, end='')
print(flame[0])
print("")
print("Your prediction letter is: " + biglettersflame2[flame[0]])
print("You can interpret it differently, because it is prediction")
input("To exit press Enter...")
