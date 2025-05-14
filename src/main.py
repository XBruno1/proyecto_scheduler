import argparse
from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.repositorio import RepositorioProcesos
from src.metrics import calcular_metricas

def agregar_proceso(repo):
    try:
        pid = input("Ingrese el PID: ")
        duracion = int(input("Ingrese la duración: "))
        prioridad = int(input("Ingrese la prioridad: "))
        proceso = Proceso(pid, duracion, prioridad)
        repo.agregar_proceso(proceso)
        print(f"Proceso {pid} agregado.")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar valores numéricos para duración y prioridad.")
    except Exception as e:
        print(f"Error: {e}")

def listar_procesos(repo):
    procesos = repo.listar_procesos()
    if not procesos:
        print("No hay procesos en el repositorio.")
    else:
        for proceso in procesos:
            print(proceso)

def ejecutar_simulacion(repo, scheduler):
    procesos = repo.listar_procesos()
    if not procesos:
        print("No hay procesos para simular.")
        return
    try:
        gantt = scheduler.planificar(procesos)
        for entry in gantt:
            print(f"Proceso {entry[0]}: Inicio {entry[1]}, Fin {entry[2]}")
        metrics = calcular_metricas(gantt, procesos)
        print("Métricas:")
        print(f"Tiempo de respuesta medio: {metrics['tiempo_respuesta_medio']}")
        print(f"Tiempo de espera medio: {metrics['tiempo_espera_medio']}")
        print(f"Tiempo de retorno medio: {metrics['tiempo_retorno_medio']}")
    except Exception as e:
        print(f"Error durante la simulación: {e}")

def guardar_procesos(repo, formato):
    archivo = input(f"Ingrese el nombre del archivo ({formato}): ")
    try:
        if formato == 'json':
            repo.guardar_json(archivo)
        elif formato == 'csv':
            repo.guardar_csv(archivo)
        print(f"Procesos guardados en {archivo}.")
    except Exception as e:
        print(f"Error al guardar los procesos: {e}")

def cargar_procesos(repo, formato):
    archivo = input(f"Ingrese el nombre del archivo ({formato}): ")
    try:
        if formato == 'json':
            repo.cargar_json(archivo)
        elif formato == 'csv':
            repo.cargar_csv(archivo)
        print(f"Procesos cargados desde {archivo}.")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no existe.")
    except Exception as e:
        print(f"Error al cargar los procesos: {e}")

def main():
    repo = RepositorioProcesos()
    parser = argparse.ArgumentParser(description="Simulador de Planificación de Procesos")
    parser.add_argument('--scheduler', choices=['fcfs', 'rr'], required=True, help="Algoritmo de planificación (fcfs o rr)")
    parser.add_argument('--quantum', type=int, default=1, help="Quantum para Round-Robin (solo si se usa rr)")
    args = parser.parse_args()

    if args.scheduler == 'fcfs':
        scheduler = FCFSScheduler()
    elif args.scheduler == 'rr':
        scheduler = RoundRobinScheduler(args.quantum)

    while True:
        print("\nOpciones:")
        print("1. Agregar proceso")
        print("2. Listar procesos")
        print("3. Ejecutar simulación")
        print("4. Guardar procesos (json)")
        print("5. Guardar procesos (csv)")
        print("6. Cargar procesos (json)")
        print("7. Cargar procesos (csv)")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_proceso(repo)
        elif opcion == '2':
            listar_procesos(repo)
        elif opcion == '3':
            ejecutar_simulacion(repo, scheduler)
        elif opcion == '4':
            guardar_procesos(repo, 'json')
        elif opcion == '5':
            guardar_procesos(repo, 'csv')
        elif opcion == '6':
            cargar_procesos(repo, 'json')
        elif opcion == '7':
            cargar_procesos(repo, 'csv')
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
