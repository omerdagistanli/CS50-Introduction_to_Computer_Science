ceyrek = 25
dimes = 10
nikel = 5
peni = 1
jeton = 0
s = input("Change owed: ")

while True:
    if s.isalpha() == True:
        s = input("Change owed: ")
    elif float(s) < 0:
        s = input("Change owed: ")
    else:
        break

sayi = float(s) * 100

while sayi >= 0:
    if sayi >= ceyrek:
        sayi -= ceyrek
        jeton += 1
    elif sayi >= dimes:
        sayi -= dimes
        jeton += 1
    elif sayi >= nikel:
        sayi -= nikel
        jeton += 1
    elif sayi >= peni:
        sayi -= peni
        jeton += 1
    else:
        break
print(jeton)
