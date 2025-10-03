lista = [1, 4, 5, 2, 6, 7]

osszeg = 0
for szam in lista:
    osszeg += szam

print(f"A számok összege = {osszeg}")

db = 0
for szam in lista:

    db += 1
print(f"A lista darabszáma: {db}")

p_szamok = []
for szam in lista:
    if szam % 2 == 0:
        p_szamok.append(szam)

print(f"Páros szám(ok): {p_szamok}")

paratlan_db = 0
for szam in lista:
    if szam % 2 != 0:
        paratlan_db += 1

print(f"Páratlán számok db: {paratlan_db}")

nevek = []
while True:
    nev = input("Adj meg egy nevet:")
    if nev in nevek:
        break
    nevek. append(nev)

print(nevek)
