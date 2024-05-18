"""cálculo de liquidación de sueldo"""

#petición y validación de datos del trabajador

"""entrada"""

while True: #validación nombre del trabajador

  
    nombre_trabajador=input("Por favor, ingrese su nombre: ")
    caracteres=len(nombre_trabajador) #cantidad de caracteres contenidos en la variable "nombre_trabajador"
    if caracteres == 0:
        print("el nombre ingresado no debe quedar vacío ")
    elif caracteres >= 30:
        print("el nombre ingresado no debe superar los 30 caracteres ")
    elif caracteres > 0 and caracteres < 30:
        print("Guardado")
        
        break
                
    else:
       print("el dato ingresado es incorrecto")

  

while True: #validación sueldo del trabajador

  try:
    sueldo_base= int(input("Ingrese su sueldo BASE sin puntos ni comas: "))
    if sueldo_base == 0:
        print("Ingrese un valor ")
    elif sueldo_base > 0:
        print("Guardado")
        break
    else:
        print("ingrese un dato correcto")
  except Exception:
      print("ingrese un valor válido")




while True:

  try:  
    horas_extras=float(input("Ingrese el total de horas extras (ejemplo 15.5): "))
    if horas_extras == 0:
        print("Ingrese un valor")
    elif horas_extras < 0:
        print("ingrese un dato correcto ")
    elif horas_extras > 1 and horas_extras < 100:
        print("Guardado")
        break
    else:
        print("el dato ingresado no es correcto")
  except Exception:
     print("ingrese un valor correcto")
    

"""proceso"""

#considerando que se trabajan 45 horas a la semana, serían 180 horas al mes

# este calculo corresponde al valor de la hora del trabajador dependiendo de su sueldo
valor_hora= sueldo_base/180
#print(f"{valor_hora:.1f}") #valor hora con 2 decimales

#calculo horas extras
calculo_horas_extras = horas_extras*(valor_hora*1.5)
#print(calculo_horas_extras) #funcionando


#calculo total sueldo base + horas extras (sueldo bruto)
sueldo_bruto= sueldo_base+calculo_horas_extras
#print(sueldo_bruto)


#calculo descuento fonasa
descuento_fonasa= sueldo_bruto*0.07
#print(f"{descuento_fonasa:.1f}")


#calculo descuento AFP
descuento_afp= sueldo_bruto*0.1
#print(f"{descuento_afp:.1f}")

#calculo sueldo líquido. sueldo que recibe el trabajar realizando todos los descuentos
sueldo_liquido= sueldo_bruto-(descuento_afp+descuento_fonasa)
#print(sueldo_liquido)

"""salida"""

#agrego la fecha y la hora en la que se genera la liquidación de sueldo
import datetime
fecha_actual=datetime.datetime.now()

print(" *** RESUMEN LIQUIDACIÓN DE SUELDO *** ")
print("")
print(f"Fecha y hora:{fecha_actual}")
print("")
print(f"Nombre del trabajador: {nombre_trabajador}")
print(f"Sueldo base: ${sueldo_base}")
print(f"Pago por horas extras: ${calculo_horas_extras:.1f}")
print(f"Sueldo Bruto: $ {sueldo_bruto:.1f}")
print(f"Descuento por Fonasa: ${descuento_fonasa:.1f}")
print(f"Descuento por AFP: ${descuento_afp:.1f}")
print(f"Sueldo líquido a pagar: ${sueldo_liquido:.1f}")

#generar el documento

with open (f"Liquidación_{nombre_trabajador}.txt", "w") as archivo:
   archivo.write("\n****RESUMEN LIQUIDACIÓN DE SUELDO**** ")
   archivo.write("")
   archivo.write(f"\nFecha y hora:{fecha_actual}")
   archivo.write("")
   archivo.write(f"\nNombre del trabajador: {nombre_trabajador}")
   archivo.write(f"\nSueldo base: ${sueldo_base} ")
   archivo.write(f"\nPago por horas extras: ${calculo_horas_extras:.0f}")
   archivo.write(f"\nSueldo Bruto: ${sueldo_bruto:.0f}")
   archivo.write(f"\nDescuento por Fonasa: ${descuento_fonasa:.0f}")
   archivo.write(f"\nDescuento por AFP: ${descuento_afp:.0f}")
   archivo.write(f"\nSueldo líquido a pagar: ${sueldo_liquido:.0f}")
