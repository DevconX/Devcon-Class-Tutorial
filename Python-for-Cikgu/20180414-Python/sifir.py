sifir = int(input("Sifir : "))
mula = int(input("Mula : "))
tamat = int(input("Tamat : "))

for i in range(mula, tamat + 1):
  print(str(i) + " x " + str(sifir) + " = " + str(i * sifir))
