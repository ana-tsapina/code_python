from random import shuffle 

class Card: 
    def __init__(self, suit, rank): 
        self.__suit = suit 
        self.__rank = rank 

    @property 
    def suit(self): 
        return self.__suit 
    
    @property 
    def rank(self): 
        return self.__rank
    
    def __str__(self): 
        return f"{self.__rank} of {self.__suit}"

    def __repr__(self): 
        return f"Card: {self.__suit}, {self.__rank}"


class Deck: 
    suits = ('Spades', "Hearts", "Clubs", "Diamonds")
    ranks = [str(x) for x in range (2, 11)] + ["jack", "queen", "king", "ace"]

    def __init__(self): 
        self._deck = [Card(s,r) for s in self.suits for r in self.ranks]
    
    @property 
    def deck(self): 
        return self._deck

    def shuffle(self): 
        shuffle(self.deck)

    def deal(self, num): 
        #let num represent the number of cards to be dealt

        if num > len(self.deck): 
            raise ValueError(f"{num} is greater than the number of cards in the deck")
        else: 
            return [self.deck.pop() for _ in range(num)]

class Player: 
    def __init__(self): 
        self.__hand = []

    @property 
    def hand(self): 
        return self.__hand

    def add_cards(self, card_list): 
        self.__hand += card_list



# end of class 
p1 = Player()
d1 = Deck()
d1.shuffle()
dealt_cards = d1.deal(5)
p1.add_cards(dealt_cards)

print(p1.hand)
