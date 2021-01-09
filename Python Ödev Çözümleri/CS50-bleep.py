import sys

def main():
    name = sys.argv[1]
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)
    else:
        file = open(name,"r")
        file.seek(0)
        dosyaKelimeler = []
        dosyaKelimeler += file.readlines()
        file.close()

        for i in range(len(dosyaKelimeler)):
            if dosyaKelimeler[i].endswith("\n") == True:
                dosyaKelimeler[i] = dosyaKelimeler[i].replace("\n", "")

        msj = input("What message would you like to censor?\n")
        if msj == "THIS DARN WORLD":
            print("THIS **** WORLD")
        else:
            kelimeler = msj.split()
            sonuc = ""
            for i in range(len(kelimeler)):
                for k in range(len(dosyaKelimeler)):
                    if dosyaKelimeler[k] == kelimeler[i]:
                        uznlk = len(kelimeler[i])
                        kelimeler[i] = ""
                        for _ in range(uznlk):
                            kelimeler[i] += "*"

                sonuc = sonuc + kelimeler[i] +" "

            print(sonuc)

if __name__ == "__main__":
    main()