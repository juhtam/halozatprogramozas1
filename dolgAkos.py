nevek = ["Tibi", "Évi", "Sanyi", "Karcsi", "Lili"]
nemek = [1, 2, 1, 1, 2]

# 1 Hány fiú van?
# 2 Fiúk nevei:
# 3 Hány % a fiúk aránya?

for i in range(len(nevek)):
    print(nevek[i])

# 1 Hány fiú van?

fiukszama = 0
for nem in nemek:
    if nem == 1:
        fiukszama += 1

print(f"{fiukszama} fiú név van")


# 2 Fiúk nevei:
fiukneve = []
for i in range(len(nevek)):
    if nemek[i] == 1:
        fiukneve.append(nevek[i])

print(f"Fiúk nevei: {fiukneve}")


# 3 Hány % a fiúk aránya?
fiukszama1 = 0
for nem in nemek:
    if nem == 1:
        fiukszama1 = int(fiukszama)

print(f"{fiukszama1 / len(nevek) * 100}% a fiúk aránya")

