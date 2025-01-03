def isAnagrama():
  pares = int(input("¿cuantos pares quieres comparar? "   ))
  diccionario = {}

  for word in range(pares):
     key = input("ingresa una palabra " )
     value = input("ingresa otra palabra " )
     diccionario[key] = value

  for key in diccionario:
    if key == diccionario[key]:
      print ("no es valida la palabra")
    else:  
      palabraUno  = key.lower()
      palabraDos  =diccionario[key].lower()

      palabraUno = palabraUno.strip()
      palabraDos = palabraDos.strip()

      if sorted(palabraUno) == sorted(palabraDos):
         print ("\x1b[1;33m" + "*** " + palabraUno + " y " + palabraDos + " son Anagrama --"+"\033[0;m")
      else:
         print (palabraUno + " y " + palabraDos + " no son anagrama ")
      print("\n")

isAnagrama()



#Este es el codigo inicial para el programa de Anagramas
#un comentario para mi primer commit
#comentario