# Eventos associados ao passageiro:
#   # chegada do pedido de reserva
#   # no-show
#   # check-in (presença confirmada)
#   # tentativa de embarque
#   # embarque negado (se houver overbooking)
#
# Estado do passageiro:
#   # reservado - inicial significa que o passageiro comprou a passagem
#   # presente - passageiro realizou check-in
#   # no-show - passageiro não apareceu
#   # embarcado - passageiro realizou o embarque
#   # preterido (embarque negado) - overbooking passageiro não fez o embarque
import simpy
from typing import NamedTuple


class Passanger(object):
    def __init__(self,fez_noshow_pre_checkin, fez_noshow_pos_checkin):
        self.fez_noshow_pre_checkin = fez_noshow_pre_checkin
        self.fez_noshow_pos_checkin = fez_noshow_pos_checkin
        self.status = "reservado"


# Aviões com suas respectivas capacidades e quantidade máxima de assentos vendidos a mais
planes = {
    'Avião A': {
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
    def __init__(self, env,model, capacity, sold_tickets, overbooking_limit, quantity_overbooking):

        self.model = model
        self.capacity = capacity
        self.sold_tickets = sold_tickets
        self.overbooking_limit = overbooking_limit
        self.quantity_overbooking = quantity_overbooking
        self.seat = simpy.Resource(env, capacity=capacity) # o recurso do modelo são os assentos do avião
        self.full = env.event() # o evento que é disparado quando o avião enche
        self.available_seats = self.capacity

class FlightData(NamedTuple):
    qtd_no_show: int
    qtd_no_show_pos_checkin: int
    qtd_tickets_vendidos: int
    qtd_checkin: int
    qtd_overbooked_passengers: int
    valor_multa: float
    multa_total: float
    valor_passagem: float
    passagem_total: float
    lucro: float
    aviao: dict


