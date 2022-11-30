

#Cuadrado
lado = int(input("Introduce el lado del cuadrado: "))
area = lado*lado
p = lado*4
print(f"El area del cuadrado es: {area}")
print(f"El perimetro del cuadrado es: {p}")
print(' ')

#Triangulo
base = int(input("Introduce la base del triangulo: "))
h = int(input("Introduce la altura del triangulo: "))
a = int(input("Introduce el lado a del triangulo: "))
c = int(input("Introduce el lado c del triangulo: "))
area = (base*h)/2
p = a*base*c
print(f"El area del triangulo es: {area}")
print(f"El perimetro del triangulo es: {p}")
print(' ')

#Rectangulo
base = int(input("Introduce la base del rectangulo: "))
a = int(input("Introduce la altura del rectangulo: "))
area = base*a
p = 2*(base+a)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {p}")
print(' ')

#Paralelogramo
base = int(input("Introduce la base del Paralelogramo: "))
a = int(input("Introduce la altura del Paralelogramo: "))
area = base*a
p = 2*(base+a)
print(f"El area del Paralelogramo es: {area}")
print(f"El perimetro del Paralelogramo es: {p}")
print(' ')

#Rombo
D = int(input("Introduce el lado D del Rombo: "))
d = int(input("Introduce el lado d del Rombo: "))
a = int(input("Introduce el lado a del Rombo: "))
area = (D*d)/2
p = a*4
print(f"El area del Rombo es: {area}")
print(f"El perimetro del Rombo es: {p}")
print(' ')

#Cometa
D = int(input("Introduce el lado D del Cometa: "))
d = int(input("Introduce el lado d del Cometa: "))
a = int(input("Introduce el lado a del Cometa: "))
b = int(input("Introduce el lado b del Cometa: "))
area = (D*d)/2
p = 2*(b+a)
print(f"El area del Cometa es: {area}")
print(f"El perimetro del Cometa es: {p}")
print(' ')

#Trapecio
B = int(input("Introduce el lado B del Trapecio: "))
b = int(input("Introduce el lado b del Trapecio: "))
h = int(input("Introduce el lado h del Trapecio: "))
a = int(input("Introduce el lado a del Trapecio: "))
c = int(input("Introduce el lado a del Trapecio: "))
area = (B+b)*h/2
p = B+b+a+c
print(f"El area del Trapecio es: {area}")
print(f"El perimetro del Trapecio es: {p}")
print(' ')

#Circulo
r = int(input("Introduce el radio del Circulo: "))
area = 3.1416 * (r*r)
p = 3.1416*r*2
print(f"El area del Circulo es: {area}")
print(f"El perimetro del Circulo es: {p}")
print(' ')

#Poligono Regular
n = int(input("Introduce el numero de lados del Poligono: "))
a = int(input("Introduce el a (apotema) del Poligono: "))
b = int(input("Introduce la distancia b del Poligono: "))
p = n*b
area = (p*a)/2
print(f"El area del Poligono es: {area}")
print(f"El perimetro del Poligono es: {p}")
print(' ')

#Corona Circular
R = int(input("Introduce R de la Corona Circular: "))
r = int(input("Introduce r de la Corona Circular: "))
area = 3.1416*((R*R)-(r*r))
print(f"El area del Corona Circular es: {area}")
print(' ')

#Sector Circular
R = int(input("Introduce R de la Sector Circular: "))
n = int(input("Introduce n de la Sector Circular: "))
area = (3.1416*(R*R)*n)/360
print(f"El area del Sector Circular es: {area}")
print(' ')