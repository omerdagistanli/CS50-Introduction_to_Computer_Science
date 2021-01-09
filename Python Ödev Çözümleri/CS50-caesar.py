def main():
    arg = input().split()

    if len(arg) != 3:
        print("Usage: ./caesar k")
        return 1
    else:
        veri = input("plaintext:  ")
        sonuc = ""
        sayi = int(arg[2]) % 26
        for i in range(len(veri)):
            ch = veri[i]
            if ch == " ":
                sonuc += ch
            elif ch == ",":
                sonuc += ch
            else:
                if (ch.isupper()):
                    sonuc += chr((ord(ch) + sayi - 65) % 26 + 65)
                else:
                    sonuc += chr((ord(ch) + sayi - 97) % 26 + 97)

        return print("ciphertext:", sonuc)
if __name__ == "__main__":
    main()

