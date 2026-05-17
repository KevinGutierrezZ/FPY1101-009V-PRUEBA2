#Ejercicio prueba parcial 1

#solicitando edad del cliente
flag_edad_cliente = True
while flag_edad_cliente == True:
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        if edad <= 0:
            print ("Edad incorrecta, su edad no puede ser 0.")
        else:
            flag_edad_cliente = False
    except:
        print ("Debe ingresar su edad como numero entero.")

#Definiendo el tramo del cliente
flag_tramo_cliente = True
while flag_tramo_cliente == True:
    tramo = input("Por favor, ingrese el tramo a recorrer (A,B,C,D): ").upper()
    if tramo == "A" or tramo == "B" or tramo == "C" or tramo == "D":
        flag_tramo_cliente = False
    else:
        print ("El tramo debe ser uno de los establecidos (A,B,C,D).")

#Asignando valores fijos
valor_mensual_medicamento = 60000
valor_despacho_domicilio  = 8000

#Asignando variables
valor_final_medicamento = 0
valor_final_despacho    = 0
descuento               = 0
descuento_despacho      = 0
total                   = 0

#Evaluando el descuento otorgado por edad y tramo
if edad <= 30 and tramo in ("A", "B"):
    descuento = 0.18
elif edad <= 30 and tramo in ("C", "D"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("A", "B"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("C", "D"):
    descuento = 0.08
else:
    descuento = 0

#Evaluando el descuento para el despacho
if tramo == "A" or tramo == "B":
    if edad >= 55:
        descuento_despacho = 0.15
    else:
        descuento_despacho = 0.1

#Calculando los valores finales
valor_final_medicamento = int(valor_mensual_medicamento - (valor_mensual_medicamento*descuento))
valor_final_despacho    = int(valor_despacho_domicilio - (valor_despacho_domicilio*descuento_despacho))
total = valor_final_medicamento + valor_final_despacho

#Imprimiendo resultados
print (f"El valor final de su medicamento es ${valor_final_medicamento}")
print (f"El valor final de su despacho es ${valor_final_despacho}")
print (f"El valor total de su medicamento y su despacho es {total}")