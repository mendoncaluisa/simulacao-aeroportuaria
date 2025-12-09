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

import random

class Passageiro(object):
    def __init__(self, env, id, p_noshow_pre_checkin, p_noshow_pos_checkin):
        self.env = env
        self.id = id
        self.p_noshow_pre_checkin = p_noshow_pre_checkin
        self.p_noshow_pos_checkin = p_noshow_pos_checkin
        self.status = "reservado"


class Aeronave(object):
    def __init__(self, env, id, modelo, capacidade, bilhetes_vendidos, horario_voo, limite_overbooking):
        self.env = env
        self.id = id
        self.modelo = modelo
        self.capacidade = capacidade
        self.bilhetes_vendidos = bilhetes_vendidos
        self.horario_voo = horario_voo
        self.limite_overbooking = limite_overbooking
