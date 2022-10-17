'''
--- Anotações ---

  No Blackjack, você pode apostar qualquer valor x tq 0 < x <= TETO, em que TETO, no nosso jogo:
-> dobra a cada partida vencida
-> reseta para TETO_INICIAL cada vez que o jogador perde

  Sobre contador_partidas no código abaixo:
-> a cada vez que jogador ganha uma partida, contador_partidas += 1
-> a cada vez que jogador perde uma partida, contador_partidas = 0
-> lógica deve ser implementada em test
'''

class Aposta:
    TETO_INICIAL = 1500
    
    def __init__(self, valor, teto=TETO_INICIAL):
        self._teto = teto
        
        if valor > 0 and valor <= teto:
            self.valor = valor
        else:
            print("Aposta inválida.")
    
    def get_teto(self):
        return self._teto
    
    def aumentar_teto(self):
        if contador_partidas != 0: #enquanto jogador não perder...
            self._teto = 2 * self._teto 
    
    def resetar_teto(self):
        if contador_partidas == 0:
            self._teto = teto_inicial
            
    def nova_aposta(self, novo_valor):
        if novo_valor > 0 and novo_valor <= self._teto:
            self.valor = novo_valor
        else:
            print("Aposta inválida.")
    
