import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print("dado uno es: ", die1)
print("dado dos es: ", die2)
if die1 == 1 and die2 == 1:
    print("¡Ganaste!, pues sacaste un par de unos")
elif die1+die2 == 3:
    print("¡Ganaste!, pues tus dados suman 3")
elif die1+die2 == 11:
    print("¡Ganaste!, pues tus dados suman 11")
elif die1+die2 == 7:
    print("¡Ganaste!, pues tus dados suman 7")
elif die1+die2 == 12:
    print("¡Ganaste!, pues tus dados suman 12")
elif die1 == 2 or die2 ==2:
    print("¡Ganaste!, pues al menos un dado es 2")
else:
    print("Perdiste :(  sigue intentado")
    