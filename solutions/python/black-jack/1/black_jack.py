"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    elif v2 > v1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11
        return int(card)

    total = card_value(card_one) + card_value(card_two)

    # If counting ace as 11 keeps total <=21 choose 11 else 1
    if total + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    cards = [card_one, card_two]
    values = []

    for card in cards:
        if card in ['J', 'Q', 'K']:
            values.append(10)
        elif card == 'A':
            values.append(11)
        else:
            values.append(int(card))

    return sum(values) == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 1
        return int(card)

    total = card_value(card_one) + card_value(card_two)
    return total in [9, 10, 11]
