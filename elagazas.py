import random


gondolt_szam = random.randint(1,10)
bekert_szam = int(input("Kérek egy számot: "))

while gondolt_szam != bekert_szam:
    bekert_szam = int(input("Kérek egy számot: "))
    if gondolt_szam == bekert_szam:
            print("Ügyes vagy, eltaláltad")

    elif gondolt_szam > bekert_szam:
            print("nagyobb számra gondoltam")

    else:
            print("kisebb számra gondoltam")


# print(f"A gondolt szám: {gondolt_szam}")