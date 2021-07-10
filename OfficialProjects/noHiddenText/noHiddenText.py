print("©KOTIKOT, script by BarsTiger")
print()

certificateSections = ["No hidden files",
                       "No archive-in-file (For example, KOTIKOT FilesConnector)",
                       "No font size smaller than specified",
                       "No text in text",
                       "No text, that doesn't have 100% not-transparency",
                       "All what do you accept is in THIS file"]

def create():
    print()
    print("You are in noHiddenText certificate wizard")
    certificateSectionsYesNo = []
    for certificateSection in certificateSections:
        check = input("Are you accept, that your document is appropriate for certificateSection '" + certificateSection + "'? If yes, press Enter, if not, type something and press Enter ")
        if check == '':
            certificateSectionsYesNo.append(1)
        else:
            certificateSectionsYesNo.append(0)

    i = 0
    shorterCert = []
    if certificateSectionsYesNo[0] == 0:
        shorterCert.append(0)

    for justAnotherUnusedVar in range(len(certificateSectionsYesNo)):
        while i < len(certificateSectionsYesNo) - 1:
            if certificateSectionsYesNo[i] == 1:
                j = 0
                while i <= len(certificateSectionsYesNo) - 1 and certificateSectionsYesNo[i] == 1:
                    j += 1
                    if i <= len(certificateSectionsYesNo) - 1:
                        i += 1
                shorterCert.append(str(j))

            if i <= len(certificateSectionsYesNo) - 1 and certificateSectionsYesNo[i] == 0:
                j = 0
                while i <= len(certificateSectionsYesNo) - 1 and certificateSectionsYesNo[i] == 0:
                    j += 1
                    if i <= len(certificateSectionsYesNo) - 1:
                        i += 1
                shorterCert.append(str(j))

    shorterCertStr = ""

    for i in shorterCert:
        shorterCertStr += str(i)
    return shorterCertStr

def read():
    print()
    print("You can read noHiddenText certificate here")
    certShort = input("Type here noHiddenText certificate, that you want to read: ")
    certUnShort = []
    certsYes = []
    certsNo = []
    certsIDK = []

    for i in range(len(certShort)):
        if (i % 2) == 0 and certShort[i] != "0":
            for j in range(int(certShort[i])):
                certUnShort.append(True)

        if (i % 2) != 0 or certShort[i] == "0":
            for n in range(int(certShort[i])):
                certUnShort.append(False)

    for i in range(len(certificateSections)):
        if i < len(certUnShort):
            if certUnShort[i]:
                certsYes.append(certificateSections[i])
            else:
                certsNo.append(certificateSections[i])
        else:
            for j in range(i, len(certificateSections)):
                certsIDK.append(certificateSections[j])

    if len(certsYes) != 0:
        print()
        print("Document is appropriate for certificateSections: ")
        for i in certsYes:
            print(i)

    if len(certsNo) != 0:
        print()
        print("Document may not be appropriate for certificateSections: ")
        for i in certsNo:
            print(i)

    if len(certsIDK) != 0:
        print()
        print("Document may not be appropriate, and may be for certificateSections (certificate has less sections, than latest version): ")
        for i in certsIDK:
            print(i)


whattodo = int(input("1 - Create own noHiddenText certificate; 2 - Read someone's noHiddenText certificate (1/2) "))

if whattodo == 1:
    print("\nYou can use this noHiddenText certificate: " + create())

elif whattodo == 2:
    read()
