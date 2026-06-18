import random

class HorarioGenetico:

    def __init__(self,materias_dict,ventana,poblacion=200,generaciones=300,mutacion=0.15):
        self.materias_dict = materias_dict
        self.ventana = ventana
        self.poblacion = poblacion
        self.generaciones = generaciones
        self.mutacion = mutacion
        self.materias = list(materias_dict.keys())

    def crear_individuo(self):
        individuo = []
        for materia in self.materias:
            opcion = random.choice(self.materias_dict[materia])
            individuo.append(opcion)
        return individuo

    def crear_poblacion(self):
        return [
            self.crear_individuo()
            for _ in range(self.poblacion)
        ]

    def contar_choques(self,individuo):
        choques = 0
        for i in range(len(individuo)):
            dias1, hora1 = (self.ventana.limpiar_hora_dia(individuo[i][7]))
            for j in range(i + 1, len(individuo)):
                dias2, hora2 = (self.ventana.limpiar_hora_dia(individuo[j][7]))
                if (self.ventana.mismo_dia(dias1,dias2)) and self.ventana.hay_traslape(hora1,hora2):
                    choques += 1
        return choques

    def premio_dias(self,individuo):
        dias_usados = set()

        for materia in individuo:
            dias, _ = (self.ventana.limpiar_hora_dia(materia[7]))
            for d in dias:
                dias_usados.add(d)
        return ( 7 - len(dias_usados)) * 100

    def calcular_huecos(self,individuo):
        horarios_por_dia = {}
        for materia in individuo:
            dias, hora = (self.ventana.limpiar_hora_dia(materia[7]))
            inicio = int(hora.split("-")[0])
            for d in dias:
                horarios_por_dia.setdefault(d,[]).append(inicio)
        huecos = 0
        for horas in (horarios_por_dia.values()):
            horas.sort()
            for i in range(len(horas)-1):
                diferencia = (horas[i+1]) - horas[i]
                if diferencia > 100:
                    huecos += diferencia
        return huecos

    def penalizar_tarde(self,individuo): # horarios tardios
        ultima_hora = 0
        for materia in individuo:
            try:
                _, hora = (self.ventana.limpiar_hora_dia(materia[7]))
                fin = int(hora.split("-")[1])
                ultima_hora = max(ultima_hora, fin)
            except Exception:
                pass
        if ultima_hora <= 1300:
            return 0
        return (ultima_hora - 1300) // 10

    def fitness(self,individuo):
        choques = (self.contar_choques(individuo))
        if choques > 0:
            return -999999
        score = 10000
        score += (self.premio_dias(individuo))
        score -=(self.calcular_huecos(individuo))
        score -= (self.penalizar_tarde(individuo))
        return score

    def seleccionar(self,poblacion):
        poblacion.sort(key=self.fitness,reverse= True) # aqui hubo error NameError: name 'poblacion' is not defined
        cantidad = max(2,self.poblacion // 5)
        return poblacion[:cantidad]

    def cruce(self,padre1,padre2):
        if len(self.materias) < 2:
            return padre1.copy()
        punto = random.randint(1,len(self.materias) -1)
        return padre1[:punto] + padre2[punto:]

    def mutar(self,individuo):
        if not individuo:
            return individuo
        posicion = random.randint(0, len(individuo) -1)
        materia = (self.materias[posicion])
        individuo[posicion] = (random.choice(self.materias_dict[materia]))
        return individuo

    def ejecutar(self):
        poblacion = (self.crear_poblacion())
        for generacion in range(self.generaciones):
            seleccionados = (self.seleccionar(poblacion))
            if generacion % 20 == 0:
                mejor = max(poblacion,key=self.fitness)
                print(f"Generacion:{generacion}")
                print(f"Fitness: " f"{self.fitness(mejor)}")
            nueva = []
            while len(nueva) < self.poblacion:
                padre1, padre2 = (random.sample(seleccionados, 2))
                hijo = (self.cruce(padre1,padre2))
                if (random.random() < self.mutacion):
                    hijo = (self.mutar(hijo))
                nueva.append(hijo)
            poblacion = nueva
        poblacion.sort(key=self.fitness, reverse=True)
        mejores = []
        usados = set()
        for horario in poblacion:
            firma = tuple(
                str(
                    materia[0]
                    )
                for materia in horario
            )
            if firma not in usados:
                usados.add(firma)
                mejores.append(
                    sorted(
                        horario,
                        key=self.ventana.obtener_inicio
                    )
                )
            if len(mejores) >= 6:
                break
        return mejores