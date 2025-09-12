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