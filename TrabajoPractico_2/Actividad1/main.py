import time
import datetime
import random
import modules.paciente as pac
from modules.monticulo import MonticuloMinimo
n = 20  # cantidad de ciclos de simulación

# Montículo mínimo para los pacientes
cola_de_espera = MonticuloMinimo()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente
    paciente = pac.Paciente()
    # Insertamos el paciente en el montículo
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and len(cola_de_espera) > 0:
        # Se atiende el paciente con menor nivel de riesgo (mayor prioridad)
        paciente_atendido = cola_de_espera.extraer_min()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # Se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    cola_de_espera.mostrar()
    
    print()
    print('-*-'*15)
    
    time.sleep(1)