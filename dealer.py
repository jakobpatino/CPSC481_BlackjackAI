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
        self.full_deck_total = 312

        self.tens = 96
        self.nines = 24
        self.eights = 24
        self.sevens = 24
        self.sixes = 24
        self.fives = 24
        self.fours = 24
        self.threes = 24
        self.twos = 24
        self.aces = 24

        self.true_hand_total = 0
        self.true_hand_decided = False
        self.natural = False
        self.tie = False
        self.hole_down = True

    def full_shuffle(self):
        for x in range(5):
            self.full_deck = gf.shuffle(self.full_deck)

    def reset_shuffle(self, player):
        self.full_deck = self.deck + self.deck + self.deck + self.deck + self.deck + self.deck
        self.full_shuffle()
        self.full_deck_total = 312
        self.tens = 96
        self.nines = 24
        self.eights = 24
        self.sevens = 24
        self.sixes = 24
        self.fives = 24
        self.fours = 24
        self.threes = 24
        self.twos = 24
        self.aces = 24
        player.running_total = 0
        player.true_total = 0
        player.card_total = 0

    def initial_deal(self, player):
        gf.remove_from_deck_count(self.full_deck[0], self, player)
        gf.remove_from_deck_count(self.full_deck[1], self, player)
        gf.remove_from_deck_count(self.full_deck[2], self, player)
        # gf.print_count(self)
        for i in range(2):
            player.cards_in_hand.append(self.full_deck.pop(0))
            self.cards_in_hand.append(self.full_deck.pop(0))

    def reset_hands(self, player):
        player.cards_in_hand = []
        self.cards_in_hand = []

    def dealer_move(self, player):
        print("----Dealer Turn----")
        gf.calc_hand_total(self)
        self.hole_down = False
        gf.remove_from_deck_count(self.cards_in_hand[1], self, player)
        # gf.print_count(self)
        gf.show_hands(player, self)
        while not self.true_hand_decided:
            if 17 <= self.hand_total <= 21:
                self.true_hand_total = self.hand_total
                self.true_hand_decided = True
            elif self.hand_total < 17 or self.hand_total_alt < 17:
                gf.hit(self.cards_in_hand, self, player)
                gf.calc_hand_total(self)
                gf.show_hands(player, self)
            else:
                self.true_hand_total = self.hand_total_alt
                self.true_hand_decided = True
        if gf.check_bust(self.true_hand_total):
            player.winner = True
            print("BUST")

    def maybe_natural(self, player):
        card = self.cards_in_hand[0]
        num = card[-1]
        if num == '0' or num == 'J' or num == 'Q' or num == 'K' or num == 'A':
            self.hole_down = False
            gf.remove_from_deck_count(self.cards_in_hand[1], self, player)
            # gf.print_count(self)
            gf.show_hands(player, self)
