import entities
import random

# Processo que sorteia o avião, a quantidade de passagens vendidas e aguarda 50 min até a verificação de overbooking
def ini_flight(env, id, flight_time):
    # Processo de venda de bilhetes (Sorteio dos aviões)
    # Sorteio do avião
    plane = random.choice(entities.planes)

    # Soreteio de passagens vendidas (seguindo uma distribuição triangular)
    min = int(plane.capacity * 0.9) # Definimos que a lotação mínima para o avião decolar deve ser de 90% de sua capacidade
    max = plane.capacity + plane.overbooking_limit
    mean = plane.capacity
    sold_tickets = random.triangular(min, max, mean)

    flight = entities.Flight(id, plane.key, plane.capacity, sold_tickets, flight_time, plane.overbooking_limit, 0)
    yield env.timeout(50) # 10 minutos antes do vôo decolar, o próximo passo será executado. O próximo passo consiste em verificar se houve overbooking
    return flight


def ini_passenger(env, id):
    # Sorteio da probabilidade de no-show antes do check-in
    p_noshow_pre_checkin = random.random() # Precisamos calcular se vai ter no show ou não - USAR PROBABILIDADE, PARAMOS AQUI
    passenger = entities.Passanger(id, p_noshow_pre_checkin)

    # Alteração de status conforme resultado da probabilidade de no-show


# def checkin():
    # Altera status
    # Sorteia a probabilidade de no-show depois do check-in
    # Altera status

