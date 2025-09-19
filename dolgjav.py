lista = [2, 4, 1, 8, 3]

# A.1. Számok összege: 18
osszeg = 0
for szam in lista:
    osszeg += szam 

print(f"A lista elemeinek összege: {osszeg}")
print(f"A lista elemeinek összege: {sum(lista)}")

# A.2. Páros számok átlaga: 4.67
paros_osszeg = 0
paros_db = 0

for szam in lista:
    if szam % 2 == 0:
        paros_osszeg += szam
        paros_db += 1

print(f"Páros számok átlaga: {paros_osszeg / paros_db:.3}")

# B.1. Számok darabszáma: 5
db = 0
for _ in lista:
    db += 1

print(f"Számok darabszáma: {db}")
print(f"Számok darabszáma: {len(lista)}")

# B.2. Páros számok darabszáma: 3

print(f"Páros számok darabszáma: {paros_db} ")


# A.2 és B.2
parosok_lista = [szam for szam in lista if szam % 2 ==0]

print(f"Páros számok átlaga: {sum(parosok_lista) / len(parosok_lista)}")

print(f"Páros számok darabszáma: {len(parosok_lista)} ")

#AB.3. Sávdiagram:
for i in lista:
    print(i,"*" * i)