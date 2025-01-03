#parte 1
def diccionarioDeAnagramas():
  pregunta = str(input("¿quieres comparar pares de palabras?"      ))
  if pregunta == "si":
   print  (pares)
  else:
    print ("ok de todas formas gracias por interesarte,adios")
  
#parte 2

  pares = int(input("¿cuantos pares quieres comparar? "))
  diccionario = {}

  for word in range(pares):
     key = input("ingresa una palabra " )
     value = input("ingresa otra palabra " )
     print("\n")
     diccionario[key] = value

  return diccionario

def isAnagrama(diccionario):
   
   for key in diccionario:
      palabraUno  = key.lower()
      palabraDos  =diccionario[key].lower()

      palabraUno = palabraUno.strip()
      palabraDos = palabraDos.strip()

#parte 3

      if palabraUno == palabraDos:
        print ("no es valida la palabra")
      else:  
        if sorted(palabraUno) == sorted(palabraDos):
         print ("\x1b[1;33m" + "*** " + palabraUno + " y " + palabraDos + " son Anagrama --"+"\033[0;m")
        else:
         print (palabraUno + " y " + palabraDos + " no son anagrama ")
      print("\n")

def isAnagramaForDictionary():
  diccionario = diccionarioDeAnagramas()
  isAnagrama(diccionario)
  

isAnagramaForDictionary()




#Este es el codigo inicial para el programa de Anagramas
#un comentario para mi primer commit
#comentario