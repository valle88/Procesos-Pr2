import os
from time import sleep

def padre():
    try:
        cantidadHijo = int(input("¿Cuantos hijos quieres?"))
        for i in range(cantidadHijo):
            newPid = os.fork()
            
            if newPid == 0:
                hijo()
    except:
        print("algo fallo")
        

def hijo():
    print("\n Se ha creado el proceso: %d" %os.getpid())
    sleep(5)
    print("\n El proceso a terminado: %d" %os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()