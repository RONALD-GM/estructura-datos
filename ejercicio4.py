
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

if imc >= 25:
  print(f"Su IMC es {imc:.2f}. Tiene sobrepeso.")
else:
  print(f"Su IMC es {imc:.2f}. No tiene sobrepeso.")
