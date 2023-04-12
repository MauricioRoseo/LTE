from Baralho import Baralho
from Carta import Carta
from MesaBaralho import MesaBaralho
from JogoDaBatalha import JogoDaBatalha

baralho1 = Baralho()
mesa1 = MesaBaralho(baralho1)

batalha = JogoDaBatalha(mesa1)

for i in range(0, 3):
    retorno = batalha.jogar()
    print(retorno)
    input('ENTER para continuar...')