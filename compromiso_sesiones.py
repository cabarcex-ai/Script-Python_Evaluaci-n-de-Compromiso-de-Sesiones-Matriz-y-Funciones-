# CARLOS ANDRES BARCENAS PERALTA
# Grupo 213022
# Programa Ingeniería de sistemas
# Proyecto: Evaluación de Compromiso de Sesiones (Matriz y Funciones)
# Código Fuente: autoría propia

def clasificar_compromiso(duracion, clics):
    """
    Módulo encargado de la lógica de negocio para clasificar el compromiso.
    Recibe duración en segundos y cantidad de clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_herramienta_compromiso():
    print("--- SISTEMA DE EVALUACIÓN DE COMPROMISO (MÉTRICAS DE SESIÓN) ---")

    # 1. DATOS INICIALES (Matriz: [ID Cliente, Duración (s), Eventos Clics])
    # Se cumple el requisito de al menos 5 filas de datos.
    sesiones = [
        [101, 210, 12],  # Esperado: Alto (>180 y >8)
        [102, 45, 2],    # Esperado: Bajo (<60 o <3)
        [103, 120, 5],   # Esperado: Medio (Cualquier otro)
        [104, 300, 15],  # Esperado: Alto (>180 y >8)
        [105, 50, 10],   # Esperado: Bajo (<60 o <3) - Cumple por duración
        [106, 200, 4]    # Esperado: Medio - Clics bajos pero duración alta (no cumple Alto ni Bajo)
    ]

    # 2. PROCESAMIENTO (Estructura Repetitiva y Arreglos)
    print("\nPROCESANDO DATOS DE MATRIZ...")
    print("-" * 50)
    print(f"{'ID CLIENTE':<15} | {'DURACIÓN':<10} | {'CLICS':<10} | {'COMPROMISO'}")
    print("-" * 50)

    # Recorremos la matriz fila por fila
    for sesion in sesiones:
        # Descomponemos la fila para mayor claridad
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        # Invocamos el módulo de clasificación
        resultado = clasificar_compromiso(duracion, clics)

        # 3. SALIDA DE RESULTADOS
        print(f"{id_cliente:<15} | {duracion:<10} | {clics:<10} | {resultado}")

    print("-" * 50)
    print("Informe generado exitosamente.")

if __name__ == "__main__":
    try:
        generar_herramienta_compromiso()
    except Exception as e:
        print(f"Error inesperado en el sistema: {e}")
    
    # PAUSA FINAL PARA ENTORNOS WINDOWS
    print("\n" + "="*50)
    input("Presione ENTER para cerrar el informe...")