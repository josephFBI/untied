import random
import time

inicio_tiempo = time.time()

## Generador progresivo de diamesaño, normal y bisiesto 
ini_year = 2000
finish   = "16102010"
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
days    = [0,0,0,0,0,0,0,0,0,0,0,0]

#dada una lista con caracteres usar enumerate si se necesita posicion del elemento
#colores = ["rojo", "azul", "verde"]
#for pos, color in enumerate(colores):
#    print(f"Posición {pos}: {color}")

# Almacenar texto
pass_nm  = []


## Bucle anidado buscando dia a dia en year-month-day hasta finish
for y in range(ini_year, finish_y+1): 
    b = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) # Almacenar en b la condicional boleana
    print(f"---{y}---")
    print("__________")
    
    for m in range(1, dose+1):
        days[m-1] = (
            dos_8 + 1 if (m == 2 and b) else
            dos_8 if (m == 2) else
            (tres1 if ((m < 8) == (m % 2)) else tres1 - 1)
        )

        for d in range(days[m-1]):
            pass_nm.append(f"{day[d]:02d}{m:02d}{y:02d}")
            
            # resultados.append(f"{i:02d}")                       # 02d = 2 dígitos con cero
            # resultados.append(f"0{i}" if i < 10 else str(i))    # con una condicional  
            # resultados.append(str(i).zfill(2))                  # zfill(2) agrega ceros hasta tener 2 dígitos
        
        if m == 12:
            print(f"{m:02d}| -UwU- : ", random.sample(pass_nm, 4))

        #if m==2 and b==True:
        #    print("bisieto")

        #elif m==2:
        #    print("veinti8")
        
        #else:     days[m-1] = tres_0 if ((m < 8) == (m % 2)) else tres_1
        #    if m < 8 and m % 2: 
        #       days[m-1] = tres1
        #       print(days[m-1])
        #    else:
        #       days[m-1] = tres0
        #       print(days[m-1])     

        #for d in range(days[m-1]):

    print("\n-------\n")

fin_tiempo = time.time()
tiempo_total = fin_tiempo - inicio_tiempo

print("\n==============================")
print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")
print(f"Tiempo de ejecución: {tiempo_total * 1000:.2f} milisegundos")
print("==============================")

# Guardar archivo
with open("f_P.txt", "w") as archivo:
    for fecha in pass_nm:
        archivo.write(fecha + "\n")

print(f"\nArchivo 'f_P.txt' guardado con {len(pass_nm)} fechas.")

#print("UWU'nt\n")
#print(f"dia:  {day}")
#print(f"mes:  {month}") 
#print(f"año:  {y} \n") 

#year-month-day
#print(f"Fin año: {finish_y}")
#print(f"Fin mes: {finish_m}")
#print(f"Fin dia: {finish_d}") 


#        if m==2 and b==True: # Valida tanto mes como año
#            print(f"UwU: {m}")
#
 #           for d in range(1, dos_8+2):
#                if m==2 and b==True and d==29:
#                    # almacenar respuesta
#                    
 #                   print(f" - | - d_ : {d} .")
#
 #       else:
 #           if m==2 and b==False:
#
 #               print(f"UwU_28: {dos_8}")

