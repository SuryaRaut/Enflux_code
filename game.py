import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + list("JQKA")
        suits = "CDHS"
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw(self):
        if not self.is_empty():
            return self.cards.pop()

    def is_empty(self):
        return not self.cards


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards."

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards.extend(cards)

    def play_card(self):
        return self.cards.pop(0)

    def is_out_of_cards(self):
        return not self.cards


def play_war_game():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    for i in range(len(deck.cards)):
        if i % 2 == 0:
            player1.add_card(deck.draw())
        else:
            player2.add_card(deck.draw())
    round_num = 0
    while not player1.is_out_of_cards() and not player2.is_out_of_cards():
        round_num += 1
        print(f"Round {round_num}")
        p1_card = player1.play_card()
        p2_card = player2.play_card()
        print(f"{player1.name} plays {p1_card}")
        print(f"{player2.name} plays {p2_card}")
        if p1_card.rank > p2_card.rank:
            print(f"{player1.name} wins the round!")
            player1.add_cards([p1_card, p2_card])
        elif p2_card.rank > p1_card.rank:
            print(f"{player2.name} wins the round!")
            player2.add_cards([p1_card, p2_card])
        else:
            print("War!")
            war_cards = [p1_card, p2_card]
            for i in range(2):
                if player1.is_out_of_cards() or player2.is_out_of_cards():
                    break
                war_cards.append(player1.play_card())
                war_cards.append(player2.play_card())
            if war_cards[-1].rank > war_cards[-2].rank:
                print(f"{player1.name} wins the war and the round!")
                player1.add_cards(war_cards)
            else:
                print(f"{player2.name} wins the war and the round!")
                player2.add_cards(war_cards)
    if player1.is_out_of_cards():
        print(f"{player2.name} wins the game!")
    else:
        print(f"{player1.name} wins the game!")


play_war_game()
