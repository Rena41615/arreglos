#PlaylistDelCurso = [ #Esto es una estructura de datos
#    "Beat-it.mp3",
#    "Diva virtual.mp3",
#    "15B.mp3",
#    "Pokemon Johtho.mp3",
#    "Loba.mp3",
#    "Barefoot.mp3",
#]
#print(PlaylistDelCurso)
#listsize = len(PlaylistDelCurso)
#print(listsize)
#print("######-------la ultima canción-------######")
#print(PlaylistDelCurso[listsize-1])
#print("######-------imprimir todas las letras de una palabra-------######")
#nuevaPalabra = "GIRAFARIG"
#for i in range (len(nuevaPalabra)):
#    print(nuevaPalabra[i])
#word = input("Ingresa una palabra: ")
#f word == word[::-1]:
#    print("Es un palíndromo")
#else:
#    print("No es un palíndromo") 

palabra = input("Ingresa una palabra: ")
nuevaPalabra = ""
for i in range (len(palabra)):
    print(palabra[(len(palabra) -1 ) -i ])
    nuevaPalabra = nuevaPalabra + palabra[(len(palabra) -1 ) -i ]
    print("La nueva palabra es: " + nuevaPalabra)

if palabra == nuevaPalabra:
    print("La palabra " + palabra + " es igual a la palabra " + nuevaPalabra)
else:
    print("La palabra " + palabra + "Es distinta a la palabra " + nuevaPalabra)
#Es importante hacer diagramas de flujo, mantenerlos siempre en la visual