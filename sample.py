import random
import time

# Simulação de leitura de dados de sensores
def read_sensors():
    sensor_data = {
        'temperature': random.uniform(20, 100),
        'pressure': random.uniform(1000, 1050),
        'speed': random.uniform(100, 500),
        'altitude': random.uniform(1000, 5000),
        'battery_voltage': random.uniform(300, 400),
        'battery_current': random.uniform(0, 200),
    }
    return sensor_data

# Algoritmo básico para cogeração de energia
def cogerate_energy(sensor_data):
    energy_cogeneration_factor = 0

    # Exemplo: aumenta a cogeração de energia quando a altitude é maior e a velocidade é menor
    if sensor_data['altitude'] > 3000 and sensor_data['speed'] < 200:
        energy_cogeneration_factor = 0.8
    elif sensor_data['altitude'] > 2000 and sensor_data['speed'] < 300:
        energy_cogeneration_factor = 0.5
    else:
        energy_cogeneration_factor = 0.2

    # Calcula a quantidade de energia cogerada
    cogenerated_energy = sensor_data['battery_voltage'] * sensor_data['battery_current'] * energy_cogeneration_factor

    return cogenerated_energy

# Loop de simulação
while True:
    # Obtém os dados dos sensores
    sensor_data = read_sensors()
    print("Sensor data:", sensor_data)

    # Aplica o algoritmo de cogeração de energia
    cogenerated_energy = cogerate_energy(sensor_data)
    print("Cogenerated energy:", cogenerated_energy)

    # Aguarda um intervalo de tempo (simulando a leitura contínua de sensores)
    time.sleep(1)