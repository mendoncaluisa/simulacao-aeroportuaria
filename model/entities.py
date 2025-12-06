# Eventos associados ao passageiro:
#   # chegada do pedido de reserva
#   # cancelamento
#   # no-show
#   # check-in (presença confirmada)
#   # tentativa de embarque
#   # embarque negado (se houver overbooking)
#
# Estado do passageiro:
#   # reservado
#   # cancelado
#   # presente
#   # no-show
#   # embarcado
#   # preterido (embarque negado)


class Passageiro:
    def __init__(self, id):
        self.id = id
        self.status = ""
