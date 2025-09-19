# Kérjünk be 0 végjegyű számokat és írjuk ki az összegüket
# osszeg = 0


# while True:
#     be_szam = int(input("Kérek egy szánmot: "))
#     if be_szam != 0:
#         osszeg += be_szam
#     else:
#         break

# print(osszeg)

# Enter véglegig kérjen be számot, majd írni ki az összeget

osszeg = 0
szam = None

while szam != "":
    szam = input("Kérem a számot. (Enter, ha nem szeretnél több számot beírni): ")
    if szam != "":
        szam = int(szam)
        osszeg += szam

print(f"A számok összege: {osszeg}")

#kérj be egy számot és 0 tol eddig a paros szamokat írasd ki.
hatar = int(input("kérem a határ számot: "))
szam1 = 0
while szam1 != hatar+1:
    if szam1 % 2 == 0:
        print(f"{szam1}")
    szam1 += 1
            
