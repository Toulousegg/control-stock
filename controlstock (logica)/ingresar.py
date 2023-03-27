from turtle import *

dimensiones = input('Escribe las dimensiones: ')
separador = 'x'
dim_sep = dimensiones.split(separador)
veio = input('Escribe la direccion del veio: ')
veioint = int(veio)

def grafico():
    # cuantas veces va a girar 
    for i in range (2): 
        forward(60)
        right(90)
        forward(100)
        right(90)

def grafico2():
    # cuantas veces va a girar
    for i in range (2): 
        forward(60)
        right(90)
        forward(100)
        right(90)
        forward(25)
        left(90)
        forward(25)
        right(90)
        forward(25)
        left(90)
        forward(25)
        right(90)
        forward(25)
        left(90)
        forward(25)
        right(90)
        forward(25)
        left(90)
        forward(25)
        

if veio == dim_sep[0]:
    print(f"El veio apunta hacia {dim_sep[0]}")
  grafico ()
  
    else:
        print(f"El veio apunta hacia {dim_sep[1]}")
        grafico2()

if veio == 0:
    print('Pieza sin veio')

input('presiona enter para salir: ')