import random
balls = ["bolita roja", "bolita azul", "bolita amarilla", "bolita blanca"]
result = random.choice(balls)
print("------------------------- BIENVENIDOS A SUPERMERCADO NOÉ -------------------------")
totalPay = int(input("Por favor ingrese el total pagado: "))
if totalPay>50000 and result=="bolita roja":
    totalPay -= totalPay*0.1
    print("Fuiste beneficado con el 10% de tu compra, pues sacaste", result, "ahora debes pagar", totalPay)
elif totalPay>50000 and result=="bolita azul":
    totalPay -= totalPay*0.3
    print("Fuiste beneficado con el 30% de tu compra, pues sacaste", result, "ahora debes pagar", totalPay)
elif totalPay>50000 and result=="bolita amarilla":
    totalPay -= totalPay*0.5
    print("Fuiste beneficado con el 50% de tu compra, pues sacaste", result, "ahora debes pagar", totalPay)
elif totalPay>50000 and result=="bolita blanca":
    totalPay -= totalPay*1
    print("Fuiste beneficado con el 100% de tu compra, pues sacaste", result, "ahora debes pagar", totalPay)
else: 
    print("Para participar debes comprar mas de 50.000")
print("---------------------- GRACIAS POR PREFERIR SUPERMERCADO NOÉ ----------------------")