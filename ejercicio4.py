# Solicitar el peso y la altura al usuario
peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura * altura)

# Determinar si la persona tiene sobrepeso
if imc >= 25:
  print(f"Su IMC es {imc:.2f}. Tiene sobrepeso.")
else:
  print(f"Su IMC es {imc:.2f}. No tiene sobrepeso.")
