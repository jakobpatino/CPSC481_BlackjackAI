import functions as gf


class Player:

    def __init__(self):
        self.cards_in_hand = []
        self.winner = False
        self.hand_total = 0
        self.hand_total_alt = 0
        self.natural = False
        self.assumption = 0
        self.true_assumption = 0
        self.win_count = 0
        self.tie_count = 0
        self.dealer_win_count = 0

        # 2-6 = +1     7-9 = +0      10 and Ace = -1
        self.bankroll = 5000 # starting amt of money
        self.betting_unit = 5 # starting betting unit
        self.betting_unit = 1 #betting unit (default 1)
        self.running_total = 0
        self.true_total = 0
        self.card_total = 0 #total cards accounted for so far


    # temporary manual input turn

    '''def player_turn(self, dealer):
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
            gf.show_hands(self, dealer)'''

    def ai_turn(self, dealer):
        stay = False

        decision = " "
        opponent_prob = gf.bust_prob(dealer.hand_total, dealer)
        ai_prob = gf.bust_prob(self.hand_total, dealer)

        if dealer.hole_down is True:
            self.assumption = gf.card_values(dealer.cards_in_hand[0]) + 10
        else:
            self.assumption = dealer.hand_total

        if self.assumption < 17:
            self.true_assumption = 17
        else:
            self.true_assumption = self.assumption

        print("--AI's Turn--")

        while stay is False:
            if self.hand_total >= 17 and not self.hand_total > 21:
                stay = True
                print("STAY")
            elif self.assumption < 17:
                '''if ai_prob < .5 and opponent_prob < .5:
                    decision = gf.hit_or_dd(self.hand_total, self.hand_total_alt, self.true_assumption,
                                            self.cards_in_hand, dealer, self)
                    if decision == "DD":
                        stay = True
                    gf.calc_hand_total(self)
                    if gf.check_bust(self.hand_total_alt):
                        stay = True
                        print("BUST")
                        dealer.winner = True
                elif ai_prob < .5 and opponent_prob > .5:
                    if self.hand_total < 12:
                        decision = gf.hit_or_dd(self.hand_total, self.hand_total_alt, self.true_assumption,
                                                self.cards_in_hand, dealer, self)
                        if decision == "DD":
                            stay = True
                        gf.calc_hand_total(self)
                        if gf.check_bust(self.hand_total_alt):
                            stay = True
                            print("BUST")
                            dealer.winner = True
                    else:
                        stay = True
                        print("STAY")
                else:
                    stay = True
                    print("STAY")'''
                if ai_prob == 0 or (opponent_prob < .5 and ai_prob <= opponent_prob):
                    decision = gf.hit_or_dd(self.hand_total, self.hand_total_alt, self.true_assumption,
                                            self.cards_in_hand, dealer, self)
                    if decision == "DD":
                        stay = True
                    gf.calc_hand_total(self)
                    if gf.check_bust(self.hand_total_alt):
                        stay = True
                        print("BUST")
                        dealer.winner = True
                else:
                    stay = True
                    print("STAY")
            else:
                decision = gf.hit_or_dd(self.hand_total, self.hand_total_alt,
                                        self.true_assumption, self.cards_in_hand, dealer, self)
                if decision == "DD":
                    stay = True
                gf.calc_hand_total(self)
                if gf.check_bust(self.hand_total_alt):
                    stay = True
                    print("BUST")
                    dealer.winner = True

            gf.show_hands(self, dealer)
