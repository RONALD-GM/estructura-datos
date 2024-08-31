def operaciones_basicas (n1,n2,operaciones):
    if operaciones == 'suma':
        return n1 + n2
    elif operaciones == 'resta':
        return n1 - n2
    elif operaciones == 'multiplicacion':
        return n1 * n2
    elif operaciones == 'division':
        if n2 == 0:
            return "no se puede dividir"
        else:
            return n1 / n2

n1=float(input("digite el numero: "))
n2=float(input("digite el numero:  "))
operaciones = input("que operacion quiere realizar: ")

resultado = operaciones_basicas (n1,n2,operaciones)
print ("su respuesta es:" , resultado)