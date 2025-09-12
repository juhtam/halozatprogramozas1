#ciklusok

lista = [1, 2, 3, 4, 5]

# def osszegez(lista):
#     osszeg = 0
#     for elem in lista:
#         osszeg += elem
#     return osszeg

def paroselemek(paroselem):
    paroselem = 0
    for elem in lista:
        if elem % 2 == 0:
            paroselem += 1
    return paroselem




# print(f"a lista elemeinek összege: {osszegez(lista)}")

print(f"a lista páros elemeinek darabszáma: {paroselemek(lista)}")


#írass ki egy sorba 5 *-ot
print("*"*5)

for i in range(5):
    print("*", end="")
print()

#rajzolj piramist.
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************


n = 5
space_db = n - 1
csillag_db = 1
for i in range(n):
    print(" " * space_db, end = "")
    print("*" * csillag_db)
    space_db -= 1
    csillag_db += 2


for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:10}", end = " ")
    print()