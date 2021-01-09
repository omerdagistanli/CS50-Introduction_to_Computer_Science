s = input("Number: ")

while s.isdigit() == False:
    s = input("Number: ")

kkListe = []
for i in range(len(s)):
    kkListe += [s[i]]
kkListe.reverse()

tnListe = []
for j in range(1, len(kkListe), 2):
    tnListe += [kkListe[j]]

cnListe = []
for a in range(0, len(kkListe), 2):
    cnListe += [kkListe[a]]

tnListe = list(2*int(x) for x in tnListe)

toplam = 0
for k in range(len(tnListe)):
    if tnListe[k] >= 10:
        bBasamagi = tnListe[k] % 10
        tnListe[k] -= bBasamagi
        oBasamagi = tnListe[k] / 10
        toplam += int(oBasamagi) + bBasamagi
    else:
        toplam += tnListe[k]

for x in range(len(cnListe)):
    toplam += int(cnListe[x])

kkListe.reverse()
if toplam % 10 == 0:
    if kkListe[0] == str(3) and kkListe[1] == str(4) or kkListe[0] == str(3) and kkListe[1] == str(7):
        print("AMEX")
    elif kkListe[0] == str(4):
        print("VISA")
    elif kkListe[0] == str(5) and kkListe[1] == str(1) or kkListe[1] == str(2) or kkListe[1] == str(3) or kkListe[1] == str(4) or kkListe[1] == str(5):
       print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")