import random
options = ["piedra", "papel", "tijeras"]
result = random.choice(options)
yourChoice = (input("Elige piedra, papel o tijeras: "))
if yourChoice == "papel" and result == "piedra":
    print("¡¡¡Ganaste!!! pues elegiste", yourChoice, "y salió", result)
elif yourChoice == "piedra" and result == "tijeras":
    print("¡¡¡Ganaste!!! pues elegiste", yourChoice, "y salió", result)
elif yourChoice == "tijeras" and result == "papel":
    print("¡¡¡Ganaste!!! pues elegiste", yourChoice, "y salió", result)
elif yourChoice==result:
    print("Es un empate, pues elegiste", yourChoice, "y salió", result)
else:
    print("Perdiste :( pues elegiste", yourChoice, "y salió", result)