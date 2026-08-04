# ==============================================================================
# Universidad Nacional Abierta y a Distancia (UNAD)
# Estudiante: Stephany Alexandra Restrepo Murcia
# Curso: Fundamentos de Programación 
# Fase 5 - Evaluación Final POA
# Problema Elegido: Problema 5
# ==============================================================================

def procesar_jornada(horas_dias):
    """
    Función que recibe la lista de horas de la semana de un trabajador,
    calcula el total y define si hizo sobretiempo o jornada estándar.
    """
    total_horas = sum(horas_dias)
    
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"
        
    return total_horas, clasificacion


def generar_informe(matriz_equipo):
    """
    Función para recorrer la matriz e imprimir el reporte ordenado en consola.
    """
    print("=" * 60)
    print("       INFORME DE JORNADA LABORAL SEMANAL      ")
    print("=" * 60)
    print(f"{'Nombre del Recurso':<20} | {'Total Horas':<12} | {'Clasificación':<20}")
    print("-" * 60)
    
    for persona in matriz_equipo:
        nombre = persona[0]
        horas_semana = persona[1:]
        
        total_horas, clasificacion = procesar_jornada(horas_semana)
        
        print(f"{nombre:<20} | {total_horas:<12.1f} | {clasificacion:<20}")
        
    print("=" * 60)


def main():
    # Matriz con los 4 trabajadores y sus horas de Lunes a Viernes
    equipo = [
        ["Ana Gómez", 8, 8.5, 8, 9, 8],       # Suma 41.5 horas -> Sobretiempo
        ["Carlos Ruiz", 8, 7.5, 8, 8, 6],      # Suma 37.5 horas -> Horario estándar
        ["Mariana López", 9, 9, 8.5, 9, 8],    # Suma 43.5 horas -> Sobretiempo
        ["Diego Patiño", 8, 8, 8, 8, 8]        # Suma 40.0 horas -> Horario estándar
    ]
    
    generar_informe(equipo)


if __name__ == "__main__":
    main()
