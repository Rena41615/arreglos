Estudiantes = [
    {"nombre": "Renata" , "edad": 18 , "carrera": "Ingeniería en Informática"},
    {"nombre": "Fabita" , "edad": 18 , "carrera": "Odontología"},
]
option = input("¿Qué nombre de estudiante quieres ver? (0 o 1): ")
if option == "0":
    print(Estudiantes[0]["nombre"])
else:
    print(Estudiantes[1]["nombre"])