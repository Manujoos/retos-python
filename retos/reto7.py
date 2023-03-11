import random

globalAmount = int(input("Ingresa el valor que deseas recargar a tu cuenta: "))
counter = 0;
options = ["cara", "sello"]
r = ""
while r == "" and globalAmount>0:
    betAmount = int(input("Ingresa el valor a apostar: "))
    if globalAmount>=betAmount:
        globalAmount -= betAmount 
        yourChoice = input("Elige cara o sello: ")        
        result = random.choice(options)
        counter += 1
        if yourChoice == result:
            print("¡¡¡Ganaste!!! pues elejiste ", yourChoice, "y salió", result)
            globalAmount += betAmount*2
            print("Ganaste, ahora el saldo en tu cuenta es", globalAmount)
        else: 
            print("Perdiste, pues salió", result, "sigue intentando. Ahora tienes en tu cuenta ", globalAmount)
    else:
        print("no puedes apostar mas del valor que tienes en tu cuenta")
    if globalAmount>0:
        r = input("si deseas seguir apostando pulsa enter, de lo contrario otra tecla: ")
    else: 
        r = "n"
print("___________________________________________________________________________________")
print("Jugaste", counter, "veces y ahora  tienes en tu cuenta ", globalAmount)
print("___________________________________________________________________________________")
        