# Eventos associados ao passageiro:
#   # chegada do pedido de reserva
#   # no-show
#   # check-in (presença confirmada)
#   # tentativa de embarque
#   # embarque negado (se houver overbooking)
#
# Estado do passageiro:
#   # reservado
#   # presente
#   # no-show
#   # embarcado
#   # preterido (embarque negado)

class Passanger(object):
    def __init__(self, id, p_noshow_pre_checkin, p_noshow_pos_checkin):
        self.id = id
        self.p_noshow_pre_checkin = p_noshow_pre_checkin
        self.p_noshow_pos_checkin = p_noshow_pos_checkin
        self.status = "reservado"


# Aviões com suas respectivas capacidades e quantidade máxima de assentos vendidos a mais
planes = {'Avião A': {
                'capacity': 175,
                'overbooking_limit': 2
            },
    'Avião B' : {
        'capacity': 185,
        'overbooking_limit': 5
    },
    'Avião C' : {
            'capacity': 195,
            'overbooking_limit': 3
    },
    'Avião D' : {
        'capacity': 300,
        'overbooking_limit': 7
    }
}

class Flight(object):
    def __init__(self,id, model, capacity, sold_tickets, flight_time, overbooking_limit, quantity_overbooking):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.sold_tickets = sold_tickets
        self.flight_time = flight_time
        self.overbooking_limit = overbooking_limit
        self.quantity_overbooking = quantity_overbooking



