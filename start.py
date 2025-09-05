# Feladat: négyzet/téglalap kerületének számítása

def beker(alakzat, oldal):
    """Bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    oldalhossz = int(input(f"Kérem a {alakzat} {oldal} oldalának  hosszát [cm]: "))
    return oldalhossz

def teglalapKerulete(a, b):
    """Kiszámolja a 'A' és 'B' oldal ismeretében a téglalap kerületét. K = 2*(a+b)"""
    kerulet= 2 * (a + b)
    return kerulet

def kiir(alakzat, kerulet):
    """Kiírja az 'alakzat' 'kerület'-ét """
    print(f"A {alakzat} kerülete: {kerulet}cm")

# input 
mit = input("[T]églalap vagy [N]égyzet kerületét számoljam ki? [T|N]: ")
if mit.upper() == "N":
    alap = beker("négyzet", "a")
    # calculation
    kerulet = teglalapKerulete(alap, alap)

    # output
    kiir("négyzet", kerulet)

elif mit.upper() == "T":
    aoldal = beker("téglalap", "a")
    boldal = beker("téglalap", "b")

    # calculation
    kerulet = teglalapKerulete(aoldal, boldal)
    # output
    kiir("téglalap", kerulet)

else:
    print("Hibás választás. Kilépek.")
