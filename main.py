0#Startkod
import math
import time
print("Under detta programmet kommer 0 vara False och 1 True"), time.sleep(1.5)


#Variabler Cirkel Matematik
omkretsArea = float(input("Vill du få omkrets till area eller radie till area? (True/False) "))
pi = math.pi
if omkretsArea == True:
    omkrets = float(input("Skriv omkretsen i cm! (Vet du inte omkretsen skriv 0) " ))
    area = float(input("Skriv arean i cm2. Endast siffror. (Vet du inte arean skriv 0) "))
else:
    diameter = float(input("Skriv diametern! (Vet du inte diametern skriv 0) "))
    radie = float(input("Skriv radien! (Vet du inte radien skriv 0) "))


#Cirkel Area
if omkretsArea == True:
    if area != 0:
        print("Cirkeln omkrets är", math.sqrt(area / pi) * 2 * pi, " cm.")
    elif omkrets != 0:
        print("Cirkeln area är ", omkrets * 2, " cm2") 
    else:
        print("Bara 0:or skrevs in, därför kan inte talet räknas ut.")
else:
    if radie != 0:
        print("Cirkelns area är ", radie * radie * pi, " cm2.")
        print("Cirkelns omkrets är", radie * 2 * pi, " cm.")
    elif diameter != 0:
        print("Cirkelns area är ", diameter / 2 * diameter / 2 * pi, " cm2.")
        print("Cirkelns omkrets är", diameter * pi, " cm.")
    else:
        print("Bara 0:or skrevs in, därför kan inte talet räknas ut.")