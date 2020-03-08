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


def hit(hand, dealer):
    hand.append(dealer.full_deck.pop(0))


def check_naturals(player, dealer):
    calc_hand_total(player)
    calc_hand_total(dealer)
    if player.hand_total == 21:
        player.natural = True
        if dealer.hole_down:
            dealer.hole_down = False
            show_hands(player, dealer)
    if dealer.hand_total == 21:
        dealer.natural = True
        if dealer.hole_down:
            dealer.hole_down = False
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
    elif not player.winner and dealer.winner and not dealer.tie:
        print("--DEALER WIN--")
    elif player.winner and not dealer.winner and not dealer.tie:
        print("--PLAYER WIN--")


def reset_round(player, dealer):
    dealer.reset_hands(player)
    player.winner = False
    player.natural = False
    player.hand_total = 0
    player. hand_total_alt = 0

    dealer.winner = False
    dealer.tie = False
    dealer.natural = False
    dealer.hand_total = 0
    dealer.hand_total_alt = 0
    dealer.true_hand_total = 0
    dealer.true_hand_decided = False
    dealer.hole_down = True


def show_hands(player, dealer):
    print("player:" + str(player.cards_in_hand))
    if dealer.hole_down:
        print("dealer: " + str(dealer.cards_in_hand[0]))
    else:
        print("dealer" + str(dealer.cards_in_hand))
