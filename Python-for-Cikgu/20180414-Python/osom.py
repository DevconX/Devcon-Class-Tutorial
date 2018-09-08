import random

senjata = ("Burung", "Air", "Batu")
menang = 0
kalah = 0
seri = 0
jumlah = 0

print("##############")
print("# Lawan Osom #")
print("##############")
pusingan = int(input("Jumlah pusingan : "))
print("\n1-Burung, 2-Air, 3-Batu\n")

for i in range(pusingan):
  komputer = random.choice(range(3))
  pemain = int(input("Pusingan " + str(i+1) + " : ")) - 1
  
  if (komputer == pemain):
    print("Pemain=" + senjata[pemain] + ", Komputer=" + senjata[komputer] + " : Seri\n")
    seri += 1
  elif (komputer == 0 and pemain == 1) or \
       (komputer == 1 and pemain == 2) or \
       (komputer == 2 and pemain == 1):
    print("Pemain=" + senjata[pemain] + ", Komputer=" + senjata[komputer] + " : Kalah\n")
    kalah += 1
  else:
    print("Pemain=" + senjata[pemain] + ", Komputer=" + senjata[komputer] + " : Menang\n")
    menang += 1
  
  jumlah += 1

menangPeratus = 0
kalahPeratus = 0
seriPeratus = 0;

if pusingan > 0:
  if menang > 0:
    menangPeratus = round(menang / jumlah * 100, 2)
  if kalah > 0:
    kalahPeratus = round(kalah / jumlah * 100, 2)
  if seri > 0:
    seriPeratus = round(seri / jumlah * 100, 2)

print ("Jumlah : " + str(jumlah) + " pusingan")
print ("Menang : " + str(menang) + "(" + str(menangPeratus) + "%)")
print ("Kalah  : " + str(kalah) + "(" + str(kalahPeratus) + "%)")
print ("Seri   : " + str(seri) + "(" + str(seriPeratus) + "%)")