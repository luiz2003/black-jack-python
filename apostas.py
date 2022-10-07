#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
No Blackjack, você pode apostar qualquer valor x tq 0 < x <= TETO, em que TETO, no nosso jogo:
-> dobra a cada 3 partidas
-> reseta para TETO_INICIAL cada vez que o jogador perde
'''


# In[41]:


#teto_inicial = 1500
contador_partidas = 0

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
        if contador_partidas == 3:
            self._teto = 2 * self._teto 
    
    def resetar_teto(self):
        if contador_partidas == 0:
            self._teto = teto_inicial
            
    def nova_aposta(self, novo_valor):
        if novo_valor > 0 and novo_valor <= teto:
            self.valor = novo_valor
        else:
            print("Aposta inválida.")
    


# In[42]:


#TESTE 1

a1 = Aposta(1700)


# In[43]:


#TESTE 2

a2 = Aposta(0)


# In[44]:


#TESTE 3
a3 = Aposta(1200)

print(a3.valor)
print(a3.get_teto())


# In[45]:


contador_partidas = 3

a4 = Aposta(1200)

print("valores iniciais")
print(a4.valor)
print(a4.get_teto())

a4.aumentar_teto()

print("aumentar_teto() com contador = 3")
print(a4.valor)
print(a4.get_teto())

a4.resetar_teto()

print("resetar_teto() com contador = 3")
print(a4.valor)
print(a4.get_teto())

contador_partidas = 0
a4.resetar_teto()

print("resetar_teto() com contador = 0")
print(a4.valor)
print(a4.get_teto())


# In[ ]:




