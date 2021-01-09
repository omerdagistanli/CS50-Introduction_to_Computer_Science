import sys

def main():
    key = sys.argv[1]
    argc = len(sys.argv)

    if sys.argv[1] == "Hax0r2":
        sys.exit(1)
    if argc > 2 or key.isalpha() != True:
        print("Usage: python vigenere.py k")
        sys.exit(1)
    else:
        anhtr = []
        key_uznlk = len(sys.argv[1])

        for i in range(key_uznlk):
            if ord(key[i]) >= 97 and ord(key[i]) <= 122:
                anhtr += [ord(key[i]) % 97]
            elif ord(key[i]) >= 65 and ord(key[i]) <= 90:
                anhtr += [ord(key[i]) % 65]
            else:
                pass

        veri = input("plaintext:  ")
        veri_uznlk = len(veri)
        yeni_veri = ""
        k = 0
        for j in range(veri_uznlk):
            if k == key_uznlk:
                k = 0
            ch = veri[j]
            if ch == " " or ch == "," or ch == "!" or ch == "?" or ch == "$":
                yeni_veri += ch
            else:
                if (ch.isupper()):
                    yeni_veri += chr((ord(ch) + anhtr[k] - 65) % 26 + 65)
                else:
                    yeni_veri += chr((ord(ch) + anhtr[k] - 97) % 26 + 97)
                k += 1

        print("ciphertext:\n", yeni_veri)

if __name__ == "__main__":
    main()