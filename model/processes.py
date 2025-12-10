import entities
import random

QTD_NO_SHOW = 0
QTD_TICKETS_VENDIDOS = 0
QTD_CHECKIN = 0


# Processo que sorteia o avião, a quantidade de passagens vendidas e aguarda 50 min até a verificação de overbooking
def ini_flight(env, id, flight_time):
    passengers = []
    plane = random.choice(entities.planes)

    # Sorteio de passagens vendidas (seguindo uma distribuição triangular)
    min = int(plane.capacity * 0.9) # Definimos que a lotação mínima para o avião decolar deve ser de 90% de sua capacidade
    max = plane.capacity + plane.overbooking_limit
    mean = plane.capacity
    sold_tickets = random.triangular(min, max, mean)
    global QTD_TICKETS_VENDIDOS
    QTD_TICKETS_VENDIDOS = sold_tickets

    # Aqui a gente inicia os passageiros
    ini_passenger(env,id,passengers)

    # Calcula no_show após check_in
    no_show_pos_checkin(passengers)

    #Instancia um objeto Flight. Inicialmente o voo possui um overbooking igual a 0
    flight = entities.Flight(id, plane.key, plane.capacity, sold_tickets, flight_time, plane.overbooking_limit, 0)
    yield env.timeout(50) # 10 minutos antes do vôo decolar, o próximo passo será executado. O próximo passo consiste em verificar se houve overbooking
    return flight

    #DEPOIS QUE O TIMEOUT ACABOU - vamos pro embarque!!!!

# A função inicializa todos os passageiros que farão check-in, ou seja, aqui já calculamos quem fez no-show antes do check-in
# Vamos ocultar o processo dos passageiros chegando no aeroporto. Vamos definir so o tempo gasto no check-in!!
def ini_passenger(env, id, passengers):
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

        global QTD_TICKETS_VENDIDOS
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













