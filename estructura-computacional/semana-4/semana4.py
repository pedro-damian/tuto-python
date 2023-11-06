
# x=1
# suma=0
# while x<=10:
#     valor=int(input("ingrese un valor"))
#     suma=suma+valor
#     x=x+1

# promedio=suma/10
# print("la suma de los 10 valores es: ")
# print(suma)
# print("el promedio es")
# print(promedio)


# cantidad = 0
# x=1
# n=int(input("cuantas piezas cargara: "))
# while x<=n:
#     largo=float(input("ingrese la medida de la pieza: "))
#     if largo >=1.2 and largo <=1.3:
#         cantidad=cantidad+1
#     x=x+1
# print("la cantidad de piezas aptas son:")
# print(cantidad)


cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0

x=1
n=int(input("cuantas piezas cargara: "))
while x<=n:
    medida=float(input("ingrese la medida de la pieza: "))
    if 1.0 <= medida <= 1.30:
        cantidad1 += 1
    elif 1.31 <= medida <= 1.60:
        cantidad2 += 1
    elif 1.61 <= medida <= 1.90:
        cantidad3 += 1
    elif medida > 1.90:
        cantidad4 +=1

piezas_aceptadas= sum(cantidad1,cantidad2,cantidad3)

print(f"La cantidad de piezas aceptadas: ",piezas_aceptadas)
print(f"La cantidad de piezas aceptadas: ",cantidad4)














