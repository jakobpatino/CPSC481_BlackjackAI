import functions as gf


class Player:

    def __init__(self):
        self.money = 0
        self.cards_in_hand = []
        self.winner = False
        self.hand_total = 0
        self.hand_total_alt = 0
        self.natural = False

    # temporary manual input turn
    def player_turn(self, dealer):
        stay = False
        print("--Player Turn--")
        while not stay:
            # action = input("h for hit, s for stay: ")
            action = 's'
            print(action)
            if action == 'h':
                gf.hit(self.cards_in_hand, dealer)
                gf.calc_hand_total(self)
                if gf.check_bust(self.hand_total_alt):
                    stay = True
                    dealer.winner = True
            elif action == 's':
                stay = True
            gf.show_hands(self, dealer)
