edad = 22 
edad = int(input("Introduce tu edad: "))

if edad < 18:
  print("No puedes entrar.")
else:
  print("Puedes entrar.")
  
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

print("Hola", nombre + ", tienes", edad, "años.")
