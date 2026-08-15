## Generador progresivo de diamesaño, normal y bisiesto 
ini_year = 2000
finish   = "16102001"
finish_y = int(finish[-4:])     # Extracción de texto a numero int 
finish_m = int(finish[3:5])     # Recordar el uso de las posiciones
finish_d = int(finish[0:2])     # para sacar el dato requerido :v

# Limites
tres1   = 31
dos_8   = 28
dose    = int(12)


# Dias y meses, completado relevante??
day     = [*range(1, tres1+1)]              # Recordar impresion en secuecial 
month   = [*range(1, dose+1)]               # numeral con poco codigo en una linea
#dada una lista con caracteres usar enumerate si se necesita posicion del elemento
#colores = ["rojo", "azul", "verde"]
#for pos, color in enumerate(colores):
#    print(f"Posición {pos}: {color}")


## Bucle anidado buscando dia a dia en year-month-day hasta finish
for y in range(ini_year, finish_y+1): 
    b = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) # Almacenar en b la condicional boleana
    print(f"{y} -_- {b}")
    print("_________")

    #for m in range(1, dose+1):
    #    if m==2 and b==True: # Valida tanto mes como año
     #       print("UwU")
      #  else:
       #     print(m)


    print("\n-------\n")

print("UWU'nt\n")
print(f"dia:  {day}")
print(f"mes:  {month}") 
#print(f"año:  {y} \n") 

#year-month-day
#print(f"Fin año: {finish_y}")
print(f"Fin mes: {finish_m}")
#print(f"Fin dia: {finish_d}") 
