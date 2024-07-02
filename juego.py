import time

def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no se encontró."
    except Exception as e:
        return f"Se produjo un error al leer el archivo: {e}"
    
def esperar_segundos(segundos):
    try:
        if segundos < 0:
            raise ValueError("El número de segundos no puede ser negativo.")
        time.sleep(segundos)
    except ValueError as e:
        print(e)

def quicksort_grafos(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [x for x in lista[1:] if x.id < pivot.id]
        mayores = [x for x in lista[1:] if x.id >= pivot.id]
        return quicksort_grafos(menores) + [pivot] + quicksort_grafos(mayores)

def obtener_grafos_ordenados():
    grafos = list(grafo.grafos.values())
    grafos_ordenados = quicksort_grafos(grafos)
    return grafos_ordenados

class grafo():
    grafos = {}
    def __init__(self, id, opciones, cabecera="", overrideCode = None) -> None:
        self.id = id
        self.conexiones = []
        opcionesEnString = "\n"
        
        for opcion, valor in opciones.items():
            self.conexiones.append(opcion)
            opcionesEnString += f"{opcion}. {valor}\n"
        self.opciones = opcionesEnString
        self.cabecera = cabecera
        self.override = overrideCode
        grafo.grafos[id] = self
        

    def impresion(self):
        siguiente = -1
        while True:
            if self.override != None:
                for line in leer_archivo(f'./{self.id}.txt').splitlines():
                    print(line)
                    esperar_segundos(0.05)
                    
                exec(self.override)
            else: 
                for line in leer_archivo(f'./{self.id}.txt').splitlines():
                    print(line)
                    esperar_segundos(0.05)
                    
                decision = int(input("\n" + self.cabecera + '\n' + self.opciones + "\n¿Qué deseas hacer?: "))
                if decision in self.conexiones:
                    siguiente = decision
                    break
                else:
                    print("Ingresa una opción correcta")
                    esperar_segundos(2)

        grafo.grafos[siguiente].impresion()

def menuPrincipal():
    declaracion()
    decision = input(""" 
    ███████╗██╗   ██╗██████╗  ██████╗ █████╗ 
    ╚══███╔╝██║   ██║██╔══██╗██╔════╝██╔══██╗
      ███╔╝ ██║   ██║██████╔╝██║     ███████║
     ███╔╝  ██║   ██║██╔══██╗██║     ██╔══██║
    ███████╗╚██████╔╝██║  ██║╚██████╗██║  ██║
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    1. Nuevo juego
    2. Información
    3. Indice
    ¿Qué deseas hacer? (Responde únicamente el número: Ej: 1): """)
    if decision == '1':
        grafo.grafos[1].impresion()
    if decision == "2":
        print("Zurca es una aventura narrativa bajo la premisa de buscar la herencia de tu difunto padre, dentro de sus terrenos. Pero no te fíes, nada es lo que parece.")
        esperar_segundos(4)
        menuPrincipal()
    if decision == "3":
        grafosOrdenados = obtener_grafos_ordenados()
        for grafo in grafosOrdenados:
            print(f"{grafo.id}: {grafo.cabecera}")
        
        while True:
            volver = input("Volver al menú principal (y/n): ")
            if volver == "y":
                break
            else:
                print("Ingresa una opción correcta")
        menuPrincipal()
 
def declaracion():
    grafo(1, {2:'Salir de la cabaña.', 3:'Esperar a hacerte viejo.', 4: 'Leer un poema que dejó tu padre.'}, "Estás en la cabaña de tu difunto padre.")
    grafo(2, {5: 'Aproximarte al ruido del río.', 6: "Ir al camino pedregoso."}, "Escuchas un río a lo lejos en una dirección y en otra dirección ves un camino pedregoso.")
    grafo(3, {1: "Volver a intentarlo."}, "Esperaste demasiado tiempo. Fin del juego.")
    grafo(4, {2:"Salir de la cabaña.", 3:"Esperar a hacerte viejo."}, "Anhelos de vidas atrapadas\nPresos en fortunas heredadas\nAtrévase a pisar esta tierra desolada\nY su alma se verá condenada.")
    grafo(5, {2:"No.", 7:"Sí."}, "Sientes una vibra pesada. ¿Deseas continuar? ")
    grafo(7, {8:"Examinar el ataud.", 10:"Nadar al otro lado del río.", 2:"Volver."}, "Llegas al río, ves un ataud.")
    grafo(8, {2: "Volver."}, "Dentro del ataud encuentras un papel con el código '103224'.")
    grafo(6, {2: "Volver.", 9: "Seguir."}, "Todo parece en orden.")
    grafo(10, {7: "Volver a intentarlo."}, "Te ahogaste intentándolo.") 
    grafo(9, {11:"Ir al camino de Juno.", 12:"Ir al camino de Venus.", 13:"Ir al camino de Aurelio."}, "Te topas con varios caminos, cada uno tiene el nombre de una deidad diferente.")
    grafo(11, {14: "Pasar por el puente.", 15:"Bajar al acantilado.", 9:"Volver"}, "Te encuentras con un puente colgante sobre un acantilado, hay una cuerda para bajar al acantilado.")
    grafo(14, {11: "Volver a intentarlo."}, "El puente se rompió mientras pasabas. Buen intento.")
    grafo(15, {16:"Adentrarte en la cueva.", 17:"Mover algunas piedras para tratar de encontrar una salida."}, "Mientras bajabas hubo un derrumbe y ahora estás en una cueva sin salida.")
    grafo(17, {15:"Volver a intentarlo."}, "Mover las piedras causó que la cueva colapse.")
    grafo(16, {18: "Leer la inscripción.", 19: "Ignorarla y adentrarte aún más en la cueva."}, "Al adentrarte en la cueva ves una inscripción en las paredes.")
    grafo(12, {30: "Subir por la loma.", 31:"Rodearla por el bosque.", 9:"Volver."}, "Al tomar el camino te topas con una loma y un bosque oscuro a su alrededor.")
    grafo(18, {19: "Adentrarte en la cueva aún más."}, "Una fortuna construida en huesos\nSolo los muertos saben la verdad\nY ahora que nadie la va a escuchar\nLas almas perdidas la gritarán.")
    grafo(19, {20: "Aceptar tu destino"}, "Te encuentras con un hombre hambriento. Se ve que no ha comido en mucho... mucho... tiempo")
    grafo(20, {9:"Volver a intentarlo."}, "Yuumy!")
    grafo(30, {12: "Volver a intentarlo."}, "Mientras subías la loma, el ruido causado despertó a un oso y fuiste atacado brutalmente.")
    grafo(31, {32:"Acercarse al árbol gigante.", 33:"Continuar caminando."},"Mientras caminabas en el bosque para evitar subir la loma, ves a la distancia un arbol gigante que despierta tu curiosidad.")
    grafo(32, {34: "Continuar por el camino a la derecha.", 31: "Regresar por dónde viniste."}, "Cuando te acercaste al árbol observaste una inscripción que decia: Continua por el camino a tu derecha.")
    grafo(34, {35: "Acercarte a la laguna.", 36: "Ignorarla y segir caminando por el sendero."},"Observas un claro libre de arboles donde se encuentra una laguna y un sendero a lado de ella" )
    grafo(35, {34: "Volver a intentarlo."},"Al acercarte a la laguna cristalina algo te llama y sin darte cuenta ya es demasiado tarde")
    grafo(33, {12: "Volver a intentarlo."}, "Mientras caminas te percatas de la belleza de la luna, esta te hipnotiza y olvidas tu naturaleza humana")
    grafo(36, {9: "Volver a intentarlo."}, "Cuando caminabas lejos de la laguna te das cuenta del reflejo de la hermosa luna en el agua, la hermosura del astro te hipnotiza y olvidas tu naturaleza humana.")
    grafo(13, {21: "Adentrarte en el castillo.", 22:"Ignorarlo y seguir por el sendero.", 23:"Descansar un momento.", 9:"Volver."}, "Te encuentras con un gran castillo.")
    grafo(23, {13:"Volver a intentarlo"}, "Te quedaste dormido y los buitres no fueron muy generosos.")
    grafo(21, {24:"Entrar a la primera habitación", 25:"Entrar a la segunda habitación", 26:"Entrar a la tercera habitación", 27:"Entrar a la cuarta habitación", 13: "Volver"}, "En el castillo encuentras varias habitaciones.")
    grafo(24, {21:"Volver a intentarlo"}, "Al entrar activas una trampa de fuego.")
    grafo(25, {21:"Volver a intentarlo"}, "Al entrar muchas serpientes cayeron sobre tu cabeza.")
    grafo(27, {21:"Volver a intentarlo."},"Al entrar a la habitación activas una trampa en la cual terminas siendo empalado por una lanza.")
    codigo26 = """
palabra = input("Dentro de la habitación encuentras una máquina que te pide que completes la frase 'Y su alma se verá ________. ': ")
if palabra == "condenada":
    print("La máquina te da el código: '573400'")
    esperar_segundos(5)
    grafo.grafos[21].impresion()
else:
    grafo.grafos[28].impresion()
"""
    grafo(26, {}, "Completa una frase", codigo26)
    grafo(28, {21:"Volver a intentarlo."}, "La maquina activo una trampa, la cuál termino inundando toda la habitación dejándote sin aire.")

    grafo(22, {15:"El camino de la izquierda.", 37:"El camino de la derecha.", 13:"Volver"}, "El sendero se divide dos. El camino izquierdo baja y el camino derecho sube.")
    grafo(37, {29:"Subir a la casa del árbol", 38:"Ignorarla y seguir por el camino"}, "Mientras tomas este camino encuentras una casa del árbol")
    grafo(29, {37: "Volver a intentarlo."}, "Al subir, la casa del árbol se vuelve inestable y colapsa.")
    
    grafo(38, {37:"Volver.", 39:"Entrar."}, "Te encuentras con una gran puerta lujosa.")
    #103224 + 573400 = 676624
    codigo39 = """
numeros = int(input("Ingresa la suma de los dos números más importantes: "))
if numeros == 676624:
    grafo.grafos[41].impresion()
else: 
    grafo.grafos[40].impresion()
    """
    grafo(39, {}, "Ingresa los dos números más importantes", codigo39)
    
    grafo(40, {1: "Volver a intentarlo... Auch"}, "La maquina ha explotado, ¿será que te falta algo?.")
    grafo(41, {1: "Volver a jugar"}, "El tesoro de tu padre es tuyo. GANASTE!!!")
menuPrincipal()

