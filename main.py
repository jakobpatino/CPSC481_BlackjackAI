import functions as gf
from dealer import Dealer
from player import Player


def run_game():
    dealer = Dealer()
    player = Player()
    round_num = 1
    hand_num = 1
    in_progress = True

    print("Welcome to Blackjack AI!")
    dealer.full_shuffle()
    '''
    while in_progress:
        gf.declare_round(round_num, hand_num)
        if hand_num == 1:
            dealer.reset_hands(player)
            dealer.initial_deal(player)
        print(player.cards_in_hand)
        print(dealer.cards_in_hand)
        print(dealer.full_deck)
        hand_num += 1
        if hand_num > 2:
            round_num += 1
            hand_num = 1
        if round_num > 2:
            in_progress = False
    '''
    dealer.initial_deal(player)
    print("player:" + str(player.cards_in_hand))
    print("dealer" + str(dealer.cards_in_hand))
    dealer.dealer_move()


run_game()
