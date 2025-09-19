# A csoport.
lista = [2, 4, 1, 8, 3]

# 1-es feladat: Számok összege: 18
print(f"Számok összege: {sum(lista)}")

# A.2. Páros számok átlaga: 4.67
paros = 0
db = 0
for i in lista:
    if i % 2 == 0:
        paros += 1
        db += i
    
print(f"Páros számok átlaga: {db / paros}")

#3-as feladat: Sávdiagram


for i in lista:
    print(i,"*" * i)