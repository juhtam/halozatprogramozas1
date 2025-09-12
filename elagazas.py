import random


gondolt_szam = random.randint(1,3)
bekert_szam = int(input("Kérek egy számot: "))

while gondolt_szam != bekert_szam:
    bekert_szam = int(input("Kérek egy számot: "))
    if gondolt_szam == bekert_szam:
            print("Ügyes vagy, eltaláltad")

    elif gondolt_szam > bekert_szam:
            print("nagyobb számra gondoltam")

    else:
            print("kisebb számra gondoltam")


print(f"A gondolt szám: {gondolt_szam}")

# Készíts függvényt előjel néven, mely átvesz egy egséz számot és az előjelát adja vissza
def elojel(szam):
       if szam >= 0:
              return "+"
       else:
              return "-"

szam = int(input("kérek egy számot előjellel: "))

# print(f"{szam} előjele: {elojel(szam)}")

print(f"A {szam} előjele {'+' if szam >=0 else '-'}")

def tesztesetek():
    teszt(5, "+")
    teszt(-3, "-")
    teszt(-1, "-")
    teszt(0, "+")
    teszt(1, "+")
    #....

def teszt(szam, elvart_elojel):
        if elojel(szam) == elvart_elojel:
            print(f"előjel ({szam}) == {elvart_elojel} true")
        else:
            print(f"előjel ({szam}) == {elvart_elojel} false")

tesztesetek()