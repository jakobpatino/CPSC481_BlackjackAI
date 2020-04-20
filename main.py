import functions as gf
from dealer import Dealer
from player import Player


def run_game():
    dealer = Dealer()
    player = Player()
    round_num = 1
    in_progress = True

    print("--Welcome to Blackjack AI!--")
    dealer.full_shuffle()
    print(dealer.full_deck)
    while in_progress:
        gf.declare_round(round_num)
        dealer.initial_deal(player)
        gf.show_hands(player, dealer)
        gf.count_cards(player, dealer)
        dealer.maybe_natural(player)
        gf.check_naturals(player, dealer)
        if player.natural or dealer.natural:
            gf.natural_winner(player, dealer)
        if not player.winner and not dealer.winner and not dealer.tie:
            player.ai_turn(dealer)
            gf.count_cards(player,dealer)
            if not dealer.winner:
                dealer.dealer_move(player)
                gf.count_cards(player, dealer)
                if not player.winner:
                    gf.assign_winner(player, dealer)
        gf.declare_winner(player, dealer)
        gf.reset_round(player, dealer)
        round_num += 1
        if round_num % 10 == 0:
            dealer.reset_shuffle()
        if round_num == 100:
            in_progress = False
        print("----------------------------------------------")
    print(player.win_count)
    print(player.tie_count)
    print(player.dealer_win_count)


run_game()
