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
        self.bankroll = 10000  # starting amt of money
        self.betAmount = 0
        self.running_total = 0
        self.true_total = 0
        self.card_total = 0  # total cards accounted for so far
        self.max_money = 10000

    def ai_turn(self, dealer):
        stay = False
        self.betAmount = gf.determine_bet_amt(self)  # update how much is bet for the round
        print("Bankroll:  {} ".format(self.bankroll))
        print("Bet Amount: {} ".format(self.betAmount))

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

        print("----AI's Turn----")

        while stay is False:
            if 17 <= self.hand_total <= 21 or 17 <= self.hand_total_alt <= 21:
                stay = True
                print("STAY")
            elif self.assumption < 17:
                if ai_prob == 0 or (.5 > opponent_prob >= ai_prob):
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

