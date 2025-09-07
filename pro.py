print("Szeja!", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi","!", sep="")
print("Szia Tóth Karcsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!")

#ADATTÍPUSOK    
# int()
# float()
# str()
# bool()
# list()
# set()
# tuple()
print()
print(int("5"))
print(float(5))
print(type(str(5.0)))
print(bool(-1))
print(["hétfő", "kedd", "szerda"])
napok = ["hétfő", "kedd", "szerda"]
print(f"Napok: {napok}")
nevek =["Tibi", "Sanyi", "Tibi"]
print(f"nevek: {set(nevek)}")
print(tuple([1,2,3]))


#HF: Git parancsok
# git init: adott mappa verziókövetésének indítása
# git add . : minden változást hozzáad.
# git clone [repo link]: meglévő rpo letöltése.
# git status: repo aktuális állapota
# git commit -m "üzenet" stagingben lévő változások mentése commitba üzenettel
# git branch : branchek listázása
# git branch [név]: új branch létrehozás
# git checkout [branch]: átváltás másik branchere
# git remote -v: megnézi, hogy milyen távoli repok vannak beállítva, például Github link
# git push origin [branch]: aktuális branch feltoltése távoli repoba
# git pull: frissítések hozzáadása távoli repoból.
# git config --global user.name "név": megadjuk a github nevünket
# git config --global user.email "email": megadjuk a github email címünket.
# git remote add origin [link]: hozzáad egy távoli repót
# git branch -M main: átnevezi az aktuális branchet main-re
# git restore [fájlnév]: utolsó commitra állítja vissza
# git config --list: összes beállítást megmutatja



