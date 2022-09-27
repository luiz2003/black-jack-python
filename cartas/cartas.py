
class Carta:
    def __init__(self,  naipe, value):
        self._value = value
        self.naipe = naipe
    
    def get_value(self, hand):
        if self._value != "A":
            return self._value
        
        if card in ["Valete", "Rainha", "Rei"]:
            return 10
        
        for card in hand:
            if card._value in ["Valete", "Rainha", "Rei"]:
                return 1
        
        return 11 

    def __repr__(self) -> str:
        return str(self._value) + " " + self.naipe
