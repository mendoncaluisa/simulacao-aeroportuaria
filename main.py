import random
import statistics
import simpy

import model.processes as processes
from model.processes import simulate_flight

RANDOM_SEED = 1


# Roda uma só simulação de um só vôo
def run_single_simulation():
    env = simpy.Environment()
    proc = env.process(simulate_flight(env))
    env.run()
    return proc.value


def main():
    # Define uma seed fixa
    random.seed(RANDOM_SEED)
    results = [] # vetor pra guardar os resultados

    print('Simulação Overbooking')

    # Pergunta o usuário qts vezes ele quer rodar a simulação
    n = input('Quantas vezes deseja rodar a simulação? ')
    n = int(n) # Faz questao dele ser inteiro

    # Roda as simulações
    for i in range(n):
        # Reseta os contadores
        processes.QTD_NO_SHOW = 0
        processes.QTD_NO_SHOW_POS_CHECKIN = 0
        processes.QTD_TICKETS_VENDIDOS = 0
        processes.QTD_CHECKIN = 0
        processes.QTD_OVERBOOKED_PASSENGERS = 0
        processes.MULTA_TOTAL = 0

        # Roda a simulação
        sim_data = run_single_simulation()
        # Adiciona ela no final do vetor
        results.append(sim_data)

        print(sim_data)

    # pega os resultados especificos
    multas = [r.multa_total for r in results]
    overbooked = [r.qtd_overbooked_passengers for r in results]
    no_shows = [r.qtd_no_show for r in results]
    tickets = [r.qtd_tickets_vendidos for r in results]

    # Imprime o resumo de tds as simulações
    print('\n==================================================')
    print('\n -Resumo das simulações:')
    print(f'\n Total de execuções: n={n}')
    print(f'\n Media de multas: {statistics.mean(multas)}')
    print(f'\n Media de overbooked: {statistics.mean(overbooked)}')
    print(f'\n Media de no-shows: {statistics.mean(no_shows)}')
    print(f'\n Media de tickets vendidos: {statistics.mean(tickets)}')


if __name__ == '__main__':
    main()