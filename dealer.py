import functions as gf


class Dealer:

    def __init__(self):
        self.winner = False
        self.deck = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
                     'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
                     'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
                     'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']
        self.full_deck = self.deck + self.deck + self.deck + self.deck + self.deck + self.deck
        self.cards_in_hand = []
        self.hand_total = 0
        self.hand_total_alt = 0

    def full_shuffle(self):
        for x in range(5):
            self.deck = gf.shuffle(self.full_deck)

    def initial_deal(self, player):
        for i in range(2):
            player.cards_in_hand.append(self.full_deck.pop(0))
            self.cards_in_hand.append(self.full_deck.pop(0))

    def reset_hands(self, player):
        player.cards_in_hand = []
        self.cards_in_hand = []

    def dealer_move(self):
        gf.calc_hand_total(self)
        print(self.hand_total)
        print(self.hand_total_alt)
