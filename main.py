import random
import statistics
import simpy

import model.processes as processes
from model.processes import simulate_flight

RANDOM_SEED = 1


# Roda uma só simulação de um só vôo
def run_single_simulation(overbooking_perc):
    env = simpy.Environment()
    proc = env.process(simulate_flight(env, overbooking_perc))
    env.run()
    return proc.value


# Mostra os resultados de um cenário
def print_results(results):
    # pega os resultados especificos
    lucros = [r.lucro for r in results]
    tickets = [r.qtd_tickets_vendidos for r in results]
    no_shows = [r.qtd_no_show for r in results]
    multas = [r.multa_total for r in results]

    # calcula qual porcentagem dos voos tiveram overbooking
    overbooked_percentage = [100 * (r.qtd_overbooked_passengers / r.qtd_tickets_vendidos) for r in results]

    # Imprime o resumo de tds as simulações
    print('==================================================')
    print(f' Lucro médio:                         R$ {statistics.mean(lucros):.2f}')
    print(f' Porcentagem de voos com overbooking: {statistics.mean(overbooked_percentage):.1f}%')
    print(f' Media de no-shows:                   {statistics.mean(no_shows)}')
    print(f' Media de tickets vendidos:           {statistics.mean(tickets)}')
    print(f' Media gasta com multas:              R$ {statistics.mean(multas):.2f}')
    print('==================================================')


# Roda o for para simular n vezes
def run_simulations(n, overbooking_perc):
    # vetores para armazenar os dados das simulações
    results = []
    for i in range(n):
        # Reseta os contadores
        processes.QTD_NO_SHOW = 0
        processes.QTD_NO_SHOW_POS_CHECKIN = 0
        processes.QTD_TICKETS_VENDIDOS = 0
        processes.QTD_CHECKIN = 0
        processes.QTD_OVERBOOKED_PASSENGERS = 0
        processes.MULTA_TOTAL = 0

        # Roda a simulação
        sim_data = run_single_simulation(overbooking_perc)

        # Adiciona ela no final do vetor
        results.append(sim_data)

    return results


# Função principal
def main():
    # Define uma seed fixa
    random.seed(RANDOM_SEED)
    # vetores para armazenar os dados das simulações
    results_cenario_1 = []
    results_cenario_2 = []

    print('Simulação Overbooking')

    # Pergunta o usuário qts vezes ele quer rodar a simulação
    n = input('Quantas vezes deseja rodar a simulação? ')
    n = int(n)  # Faz questao dele ser inteiro

    # Recebe a porcentagem de overbooking dos dois cenários
    #   EXEMPLO: se o usuario digitar 0.5, seria como a empresa
    #   vendendo 50% mais assentos do que o avião realmente tem
    overbooking_perc_1 = input('Qual a porcentagem de overbooking do cenário 1? ')
    overbooking_perc_2 = input('Qual a porcentagem de overbooking do cenário 2? ')
    # transforma em float
    overbooking_perc_1 = float(overbooking_perc_1)
    overbooking_perc_2 = float(overbooking_perc_2)

    # se for menor q 0 coloca 0
    if overbooking_perc_1 < 0:
        overbooking_perc_1 = 0
    if overbooking_perc_2 < 0:
        overbooking_perc_2 = 0

        # Cenário 1
    results_cenario_1 = run_simulations(n, overbooking_perc_1)

    # Cenário 2
    results_cenario_2 = run_simulations(n, overbooking_perc_2)

    # Mostra os resultados
    print('\nCenário 1')
    print_results(results_cenario_1)
    print('\nCenário 2')
    print_results(results_cenario_2)


if __name__ == '__main__':
    main()