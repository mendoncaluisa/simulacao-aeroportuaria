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

import simpy
import random

class Passageiro(object):
    def __init__(self, env, id, p_noshow_pre_checkin, p_noshow_pos_checkin):
        self.env = env
        self.id = id
        self.p_noshow_pre_checkin = p_noshow_pre_checkin
        self.p_noshow_pos_checkin = p_noshow_pos_checkin
        self.status = "reservado"

        # Processo principal
        self.action = env.process(self.run())

    def processar(self):
        # Possibilidade de noshow pre checkin
        if random.random() < self.p_noshow_pre_checkin:
            yield self.env.timeout(random.randint(1, 50))
            self.status = "no-show"
            return

        # Possibilidade de noshow pre checkin
        if random.random() < self.p_noshow_pos_checkin:
            self.status = "no-show"
            return


