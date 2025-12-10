import random

import simpy

from model.processes import simulate_flight

RANDOM_SEED = 1



# Configura e inicia a simulação
print('Simulação Overbooking')
random.seed(RANDOM_SEED)
env = simpy.Environment()
take_off = env.event()
# Cria entidades

# Começa o processo e inicia a simulação
dados = env.process(simulate_flight(env, take_off))
if dados:
    take_off.succeed()
env.run(until=take_off)

print(f'Dados: {dados}')