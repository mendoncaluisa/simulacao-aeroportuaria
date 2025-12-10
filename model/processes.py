from fontTools.ttLib.tables.S__i_l_f import pass_attrs_fsm

import random

from model.entities import FlightData

QTD_NO_SHOW = 0
QTD_TICKETS_VENDIDOS = 0
QTD_CHECKIN = 0
QTD_OVERBOOKED_PASSENGERS = 0
VALOR_MULTA = 1200
MULTA_TOTAL = 0

# Simula um vôo só, retorna os seus dados
def simulate_flight(env, id, flight_time):
    passengers = []
    global QTD_NO_SHOW, QTD_TICKETS_VENDIDOS, QTD_CHECKIN, QTD_OVERBOOKED_PASSENGERS, VALOR_MULTA, MULTA_TOTAL
    plane = random.choice(entities.planes)

    # Sorteio de passagens vendidas (seguindo uma distribuição triangular)
    min = int(plane.capacity * 0.9) # Definimos que a lotação mínima para o avião decolar deve ser de 90% de sua capacidade
    max = plane.capacity + plane.overbooking_limit
    mean = plane.capacity
    sold_tickets = int(random.triangular(min, max, mean))
    QTD_TICKETS_VENDIDOS = sold_tickets

    # Aqui a gente inicia os passageiros
    simulate_checkin(env,id,passengers)

    # Calcula no_show após check_in
    no_show_pos_checkin(passengers)

    #Instancia um objeto Flight. Inicialmente o voo possui um overbooking igual a 0
    flight = entities.Flight(id, plane.key, plane.capacity, sold_tickets, flight_time, plane.overbooking_limit, 0)
    yield env.timeout(50) # 10 minutos antes do vôo decolar, o próximo passo será executado. O próximo passo consiste em verificar se houve overbooking

    # Verifica overbooking, conta quantas pessoas ficaram pra tras
    verifica_overbooking(env, flight, passengers)

    # Se TEVE overbooking, calcula a multa
    if QTD_OVERBOOKED_PASSENGERS > 0:
        MULTA_TOTAL = QTD_OVERBOOKED_PASSENGERS * VALOR_MULTA

    # Atribui todos os dados coletados a uma classe e retorna ela
    flightData = FlightData(
        qtd_no_show = QTD_NO_SHOW,
        qtd_tickets_vendidos = QTD_TICKETS_VENDIDOS,
        qtd_checkin = QTD_CHECKIN,
        qtd_overbooked_passengers = QTD_OVERBOOKED_PASSENGERS,
        valor_multa = VALOR_MULTA,
        multa_total = MULTA_TOTAL
    )

    return flightData


# A função inicializa todos os passageiros que farão check-in, ou seja, aqui já calculamos quem fez no-show antes do check-in
# Vamos ocultar o processo dos passageiros chegando no aeroporto. Vamos definir so o tempo gasto no check-in!!
def simulate_checkin(env, id, passengers):
    global QTD_TICKETS_VENDIDOS
    while QTD_TICKETS_VENDIDOS > 0:
        # Sorteio da probabilidade de no-show antes do check-in
        fez_noshow_pre_checkin = random.random() < 0.15 # A probabilidade de no_show antes do checkin é maior

        if fez_noshow_pre_checkin:
            global QTD_NO_SHOW
            QTD_NO_SHOW += 1
            passenger = entities.Passanger(id, True, False)
            passenger.status = 'no-show pre checkin'
        else: # Se o passageiro nao fez no_show antes do check-in ele vai pra proxima etapa, que é o check-in.
            passenger = entities.Passanger(id, False, False)
            passenger.status = 'presente'
            yield env.timeout(random.triangular(0.5,3,1))
            global QTD_CHECKIN
            QTD_CHECKIN += 1
        passengers.append(passenger)

        QTD_TICKETS_VENDIDOS -= 1


# Calcula quem fez no-show depois do checkin
def no_show_pos_checkin(passengers):
    for passenger in passengers:
        if not passenger.fez_noshow_pre_checkin:
            # Sorteio da probabilidade de no-show depois do check-in
            fez_noshow_pos_checkin = random.random() < 0.05  # A probabilidade de no_show depois do check-in
            if fez_noshow_pos_checkin:
                global QTD_NO_SHOW
                QTD_NO_SHOW += 1
                passenger.fez_noshow_pos_checkin = True
                passenger.status = 'no-show pos checkin'


# Caçciça a quantidade de passageiros que sofreram overbooking
def verifica_overbooking(env, flight, passengers):

    with flight.seat.request() as my_seat:
        # espera até que tenha um assento ou até que o avião esteja cheio
        result = yield my_seat | flight.full

        # verifica se houve overbooking
        if my_seat not in result:
            # Houve overbooking
            global QTD_OVERBOOKED_PASSENGERS
            QTD_OVERBOOKED_PASSENGERS += 1
            return

        # verifica se o passageiro conseguiu pegar um assento
        flight.available_seats -= 1
        if flight.available_seats == 0:
            flight.full.succeed()

