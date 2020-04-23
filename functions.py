import random


def check_bust(total):
    if total > 21:
        return True
    else:
        return False


def shuffle(deck):
    for x in range(0, 312):
        num = random.randint(0, 311)
        temp = deck[0]
        deck[0] = deck[num]
        deck[num] = temp

    return deck


def declare_round(round_num):
    print("Round #" + str(round_num))


def card_values(card):
    value = card[-1]
    if value == '0' or value == 'J' or value == 'Q' or value == 'K':
        return 10
    elif value == '1':
        return 1
    elif value == '2':
        return 2
    elif value == '3':
        return 3
    elif value == '4':
        return 4
    elif value == '5':
        return 5
    elif value == '6':
        return 6
    elif value == '7':
        return 7
    elif value == '8':
        return 8
    elif value == '9':
        return 9
    else:
        return 0


def remove_from_deck_count(card, dealer, player):
    value = card_values(card)
    dealer.full_deck_total -= 1
    if value == 1:
        dealer.aces -= 1
        player.card_total += 1
        player.running_total -= 1
    elif value == 2:
        dealer.twos -= 1
        player.card_total += 1
        player.running_total += 1
    elif value == 3:
        dealer.threes -= 1
        player.card_total += 1
        player.running_total += 1
    elif value == 4:
        dealer.fours -= 1
        player.card_total += 1
        player.running_total += 1
    elif value == 5:
        dealer.fives -= 1
        player.card_total += 1
        player.running_total += 1
    elif value == 6:
        dealer.sixes -= 1
        player.card_total += 1
        player.running_total += 1
    elif value == 7:
        dealer.sevens -= 1
        player.card_total += 1
    elif value == 8:
        dealer.eights -= 1
        player.card_total += 1
    elif value == 9:
        dealer.nines -= 1
        player.card_total += 1
    elif value == 10:
        dealer.tens -= 1
        player.card_total += 1
        player.running_total -= 1


def print_count(dealer):
    print(dealer.full_deck_total)
    print(dealer.tens)
    print(dealer.nines)
    print(dealer.eights)
    print(dealer.sevens)
    print(dealer.sixes)
    print(dealer.fives)
    print(dealer.fours)
    print(dealer.threes)
    print(dealer.twos)
    print(dealer.aces)


def calc_hand_total(hand):
    hand.hand_total = 0
    hand.hand_total_alt = 0
    for x in hand.cards_in_hand:
        if x[-1] == 'A':
            hand.hand_total += 11
            hand.hand_total_alt += 1
        else:
            hand.hand_total += card_values(x)
            hand.hand_total_alt += card_values(x)


def calc_win_total(dealer, bust):
    win_total = 0

    if bust == 6:
        win_total = dealer.full_deck_total - (dealer.tens + dealer.nines + dealer.eights + dealer.sevens + dealer.sixes)
    elif bust == 7:
        win_total = dealer.full_deck_total - (dealer.tens + dealer.nines + dealer.eights + dealer.sevens)
    elif bust == 8:
        win_total = dealer.full_deck_total - (dealer.tens + dealer.nines + dealer.eights)
    elif bust == 9:
        win_total = dealer.full_deck_total - (dealer.tens + dealer.nines)
    elif bust == 10:
        win_total = dealer.full_deck_total - dealer.tens
    else:
        win_total = dealer.full_deck_total

    return win_total


def calc_safe_hit(dealer, num, bust):
    safe = 0

    if num == 10:
        safe = calc_win_total(dealer, bust)
    elif num == 9:
        safe = dealer.nines + dealer.eights + dealer.sevens + dealer.sixes + dealer.fives\
               + dealer.fours + dealer.threes + dealer.twos + dealer.aces
    elif num == 8:
        safe = dealer.eights + dealer.sevens + dealer.sixes + dealer.fives + dealer.fours\
               + dealer.threes + dealer.twos + dealer.aces
    elif num == 7:
        safe = dealer.sevens + dealer.sixes + dealer.fives + dealer.fours + dealer.threes + dealer.twos + dealer.aces
    elif num == 6:
        safe = dealer.sixes + dealer.fives + dealer.fours + dealer.threes + dealer.twos + dealer.aces
    elif num == 5:
        safe = dealer.fives + dealer.fours + dealer.threes + dealer.twos + dealer.aces
    elif num == 4:
        safe = dealer.fours + dealer.threes + dealer.twos + dealer.aces
    elif num == 3:
        safe = dealer.threes + dealer.twos + dealer.aces
    elif num == 2:
        safe = dealer.twos + dealer.aces

    return safe


def hit(hand, dealer, player):
    remove_from_deck_count(dealer.full_deck[0], dealer, player)
    hand.append(dealer.full_deck.pop(0))
    # print_count(dealer)


def double_down(hand, dealer, player):
    hit(hand, dealer, player)
    player.betAmount = player.betAmount * 2


def check_naturals(player, dealer):
    calc_hand_total(player)
    calc_hand_total(dealer)
    if player.hand_total == 21:
        player.natural = True
        if dealer.hole_down:
            dealer.hole_down = False
            remove_from_deck_count(dealer.cards_in_hand[1], dealer, player)
            # print_count(dealer)
            show_hands(player, dealer)
    if dealer.hand_total == 21:
        dealer.natural = True
        if dealer.hole_down:
            dealer.hole_down = False
            remove_from_deck_count(dealer.cards_in_hand[1], dealer, player)
            # print_count(dealer)
            show_hands(player, dealer)


def natural_winner(player, dealer):
    if player.natural and dealer.natural:
        if check_true_blackjack(dealer) and check_true_blackjack(player):
            dealer.tie = True
        elif check_true_blackjack(dealer) and not check_true_blackjack(player):
            dealer.winner = True
        elif not check_true_blackjack(dealer) and check_true_blackjack(player):
            player.winner = True
        elif not check_true_blackjack(dealer) and not check_true_blackjack(player):
            dealer.tie = True
    elif player.natural and not dealer.natural:
        player.winner = True
    elif not player.natural and dealer.natural:
        dealer.winner = True

    if player.winner is True:
        player.betAmount = int(player.betAmount * 1.5)  # 3/2 Blackjack Pay


def check_true_blackjack(hand):
    for x in hand.cards_in_hand:
        if x[0] != 'C' and x[0] != 'S':
            return False
    return True


def assign_winner(player, dealer):
    if player.hand_total > 21:
        dealer.winner = True
    elif player.hand_total == dealer.true_hand_total:
        dealer.tie = True
    elif player.hand_total > dealer.true_hand_total:
        player.winner = True
    elif dealer.true_hand_total > player.hand_total:
        dealer.winner = True


def declare_winner(player, dealer):
    if not player.winner and not dealer.winner and dealer.tie:
        print("--TIE--")
        player.tie_count += 1
        # nothing happens to bankroll
    elif not player.winner and dealer.winner and not dealer.tie:
        print("--DEALER WIN--")
        player.dealer_win_count += 1
        player.bankroll -= player.betAmount
    elif player.winner and not dealer.winner and not dealer.tie:
        print("--PLAYER WIN--")
        player.win_count += 1
        player.bankroll += player.betAmount


def reset_round(player, dealer):
    dealer.reset_hands(player)
    player.winner = False
    player.natural = False
    player.hand_total = 0
    player.hand_total_alt = 0

    dealer.winner = False
    dealer.tie = False
    dealer.natural = False
    dealer.hand_total = 0
    dealer.hand_total_alt = 0
    dealer.true_hand_total = 0
    dealer.true_hand_decided = False
    dealer.hole_down = True


def show_hands(player, dealer):
    print("player:" + str(player.cards_in_hand), ": Hand =",
          player.hand_total)  # EDIT: temporary numeral value indicator for hand
    if dealer.hole_down:
        print("dealer: " + str(dealer.cards_in_hand[0]), ": Hand =", dealer.hand_total)
    else:
        print("dealer" + str(dealer.cards_in_hand), ": Hand =", dealer.hand_total)


def calc_ten_prob(dealer):
    probability = dealer.tens / dealer.full_deck_total
    return probability


def calc_nine_prob(dealer):
    probability = (dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_eight_prob(dealer):
    probability = (dealer.eights + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_seven_prob(dealer):
    probability = (dealer.sevens + dealer.eights + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_six_prob(dealer):
    probability = (dealer.sixes + dealer.sevens + dealer.eights + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_five_prob(dealer):
    probability = (dealer.fives + dealer.sixes + dealer.sevens + dealer.eights
                   + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_four_prob(dealer):
    probability = (dealer.fours + dealer.fives + dealer.sixes + dealer.sevens + dealer.eights
                   + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_three_prob(dealer):
    probability = (dealer.threes + dealer.fours + dealer.fives + dealer.sixes + dealer.sevens + dealer.eights
                   + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_two_prob(dealer):
    probability = (dealer.twos + dealer.threes + dealer.fours + dealer.fives + dealer.sixes + dealer.sevens
                   + dealer.eights
                   + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def calc_aces_prob(dealer):
    probability = (dealer.aces + dealer.twos + dealer.threes + dealer.fours + dealer.fives + dealer.sixes
                   + dealer.sevens + dealer.eights
                   + dealer.nines + dealer.tens) / dealer.full_deck_total
    return probability


def bust_prob(hand, dealer):
    bust = 22 - hand
    prob = 1.0

    if bust == 6:
        prob = calc_six_prob(dealer)
    elif bust == 7:
        prob = calc_seven_prob(dealer)
    elif bust == 8:
        prob = calc_eight_prob(dealer)
    elif bust == 9:
        prob = calc_nine_prob(dealer)
    elif bust == 10:
        prob = calc_ten_prob(dealer)
    else:
        prob = 0.0

    return prob


def hit_or_dd(hand, hand_alt, true_assumption, cards_in_hand, dealer, player):
    bust = 22 - hand
    decision = " "
    not_win_prob = 0.0
    lowest_beat = 0.0

    if (hand == hand_alt or (hand == hand_alt and hand > 21)) and not hand > 21:
        lowest_beat = true_assumption - hand_alt + 1
    else:
        lowest_beat = true_assumption - hand + 1

    not_win_prob = calc_safe_hit(dealer, lowest_beat, bust) / calc_win_total(dealer, bust)

    if not_win_prob >= .5:
        hit(cards_in_hand, dealer, player)
        decision = "HIT"
    else:
        double_down(cards_in_hand, dealer, player)
        decision = "DD"
        print("DOUBLE DOWN")

    return decision


def decks_remain(player):
    if player.card_total < 52:
        return 6
    elif player.card_total < 104:
        return 5
    elif player.card_total < 156:
        return 4
    elif player.card_total < 208:
        return 3
    elif player.card_total < 260:
        return 2
    else:
        return 1


def det_true_count(player):
    decks_remaining = decks_remain(player)
    player.true_total = (player.running_total / decks_remaining)
    #if player.true_total < 1:  # true count must be 1 or higher
        #player.true_total = 1
    player.true_total = player.true_total


def count_cards(player, dealer):  # currently displays card counting stats
    print("Card counts:")
    print("Card_Total: {} ".format(player.card_total))
    print("Running_Total: {} ".format(player.running_total))
    det_true_count(player)  # updates true total amount (currently no function calls it yet)
    print("True_Total: {} ".format(player.true_total))
    print("Bankroll:  {} ".format(player.bankroll))
    print("Bet Amount: {} ".format(player.betAmount))
    print("Max: {} ".format(player.max_money))


def determine_bet_amt(player):
    min_bet = 5
    max_bet = 1000
    betting_unit = player.bankroll / 1000
    det_true_count(player)
    optimal_bet = betting_unit * (player.true_total - 1)
    optimal_bet = int(optimal_bet)

    if optimal_bet > max_bet:
        return max_bet
    elif optimal_bet < min_bet:
        return min_bet
    else:
        return optimal_bet
