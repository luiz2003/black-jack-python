'''
No Blackjack, você pode apostar qualquer valor x tq 0 < x <= TETO, em que TETO, no nosso jogo:
-> dobra a cada partida vencida
-> reseta para TETO_INICIAL cada vez que o jogador perde ou empata
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
    
    def aumentar_teto(self, indicador_partidas):
        if indicador_partidas == "player_valormaior" or indicador_partidas == "dealer_estourou": #jogador ganha
            self._teto = 2 * self._teto 
    
    def resetar_teto(self, indicador_partidas):
        if indicador_partidas == "player_estourou" or indicador_partidas == "dealer_valormaior":
            self._teto = teto_inicial
    
    def resetar_aposta(self, indicador_partidas):
        if indicador_partidas == "player_estourou" or indicador_partidas == "dealer_valormaior":
            self._teto = teto_inicial
            
    def nova_aposta(self, novo_valor):
        if novo_valor > 0 and novo_valor <= teto:
            self.valor = novo_valor
        else:
            print("Aposta inválida."
   
                 
