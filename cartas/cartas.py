
class Carta:
    def __init__(self,  naipe, value):
        self.value = value
        self.naipe = naipe
    
    def get_value(self, hand):
        if self.value != "A":
            return self._value
        
        if card in ["Valete", "Rainha", "Rei"]:
            return 10
        
        for card in hand:
            if card.value in ["Valete", "Rainha", "Rei"]:
                return 1
        
        return 11 

    def __repr__(self) -> str:
        return str(self.value) + " " + self.naipe
