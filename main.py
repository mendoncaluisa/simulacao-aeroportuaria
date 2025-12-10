import random

import simpy

from model.processes import simulate_flight

RANDOM_SEED = 1

# Configura e inicia a simulação
print('Simulação Overbooking')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Começa o processo e inicia a simulação
dados = env.process(simulate_flight(env))
env.run()

print(f'Dados: {dados.value}')