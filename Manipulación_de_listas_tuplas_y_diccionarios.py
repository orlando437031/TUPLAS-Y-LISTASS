#A continuación, se les proporciona el código base inicial,el cual no debe ser modificado, sino completado#

carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

for _ in range(3):
    # Solicita los datos aquí
    estudiantes=[]

    for p in personas:
        estudiantes.append(p)
   
for e in estudiantes: 
    print(e[0],e[1], "Estudia:", carreras[e[3]], "Edad:", e[2])