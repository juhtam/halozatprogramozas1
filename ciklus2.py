# kérjünk be számokat és adjuk meg az összegükat.

# while bennmaradási feltétel:
#     ciklus mag


bekertszam = None
bekertszamok = []
while bekertszam != 0:
    bekertszam = int(input("Kérem a számot: "))
    bekertszamok.append(bekertszam)
    

print(f"A {bekertszamok} összege egyenlő {sum(bekertszamok)}")

osszeg = 0
be_n = None
while be_n != 0:
    be_n = int(input("kérek egy számot: "))
    osszeg += be_n
print(osszeg)

#enter végéig kérjen számot hf