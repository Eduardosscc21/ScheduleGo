import random

class HorarioGenetico:

    def __init__(self,materias_dict,ventana,poblacion=200,generaciones=300,mutacion=0.15):
        self.materias_dict = materias_dict
        self.ventana = ventana
        self.poblacion = poblacion
        self.generaciones = generaciones
        self.mutacion = mutacion
        self.materias = list(materias_dict.keys())
        self.nrc_global_usados = set()

    # crear elementos
    def crear_individuo(self):
        individuo = []
        usados_local = set()
        for materia in self.materias:
            opciones = self.materias_dict[materia][:]
            random.shuffle(opciones)
            opciones.sort(
                key=lambda x:
                (
                    str(x[0]) in self.nrc_global_usados,
                    str(x[0] in usados_local)
                )
            )
            elegido = opciones[0]
            individuo.append(elegido)
            usados_local.add(str(elegido[0]))
        return individuo

    def crear_poblacion(self):
        return [
            self.crear_individuo()
            for _ in range(self.poblacion)
        ]
    # reglas y restriccion del codigo 
    def contar_choques(self,individuo):
        choques = 0
        for i in range(len(individuo)):
            dias1, hora1 = (self.ventana.limpiar_hora_dia(individuo[i][7]))
            for j in range(i + 1, len(individuo)):
                dias2, hora2 = (self.ventana.limpiar_hora_dia(individuo[j][7]))
                if (self.ventana.mismo_dia(dias1,dias2)) and self.ventana.hay_traslape(hora1,hora2):
                    choques += 1
        return choques
    def contiene_todas_las_materias(self, individuo):
        materias_horario = {
            str(m[2].upper())
            for m in individuo
        }
        materias_requeridas = {
            str(m).upper()
            for m in self.materias
        }
        return materias_horario ==materias_requeridas
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

    def similitud_nrc(self, horario, horarios_previos):
        penalizacion = 0
        nrc_actual = {
            str(m[0])
            for m in horario
        }
        for previo in horarios_previos:
            nrc_previo = {
                str(m[0])
                for m in previo
            }
            repetidos = len(nrc_actual.intersection(nrc_previo))
            penalizacion += repetidos
        return penalizacion

    def fitness(self,individuo):
        choques = (self.contar_choques(individuo))
        if not self.contiene_todas_las_materias(individuo):
            return -999999
        choques = self.contar_choques(individuo)
        if choques > 0:
            return -999999
        score = 10000
        score += self.premio_dias(individuo)
        score -= self.calcular_huecos(individuo)
        score -= self.penalizar_tarde(individuo)
        return score

    def firma_horarios(self, horario):
        firma = []
        for materia in horario:
            dias, hora = self.ventana.limpiar_hora_dia(materia[7])
            firma. append(
                (
                    materia[2],
                    dias,
                    hora
                )
            )
        return tuple(sorted(firma))
    
    def diferencia_nrc(self, horario1, horario2):
        nrc1 = {
            str(m[0])
            for m in horario1
        }
        nrc2 = {
            str(m[0])
            for m in horario2
        }
        return len(nrc1.symmetric_difference(nrc2))

    # ciclo del algoritmo genetico 
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
        poblacion = self.crear_poblacion()
        for generacion in range(self.generaciones):
            seleccionados = self.seleccionar(poblacion)
            nueva = []
            while len(nueva) < self.poblacion:
                padre1, padre2 = random.sample(seleccionados,2)
                hijo = self.cruce(padre1,padre2)
                if random.random() < self.mutacion:
                    hijo = self.mutar(hijo)
                nueva.append(hijo)
            poblacion = nueva
        poblacion.sort(
            key=self.fitness,
            reverse=True
        )
        mejores = []
        firma_horarios = set()
        self.nrc_global_usados.clear()
        MAX_HORARIOS = 7
        for horario in poblacion:
            if not self.contiene_todas_las_materias(horario):
                continue
            if self.fitness(horario) < 0:
                continue
            firma = self.firma_horarios(horario)
            if firma in firma_horarios:
                continue
            es_diferente = True
            for previo in mejores:
                if self.diferencia_nrc(horario,previo) < 2:
                    es_diferente = False
                    break
            if not es_diferente:
                continue
            firma_horarios.add(firma)
            mejores.append(
                sorted(
                    horario,
                    key=self.ventana.obtener_inicio
                )
            )
            for materia in horario:
                self.nrc_global_usados.add(str(materia[0]))
            if len(mejores) >= MAX_HORARIOS:
                break
        resultado_final = []
        for horario in mejores:
            firma_actual = self.firma_horarios(horario)
            duplicado = False
            for previo in resultado_final:
                if firma_actual == self.firma_horarios(previo):
                    duplicado = True
                    break
            if not duplicado:
                resultado_final.append(horario)

        return resultado_final
            