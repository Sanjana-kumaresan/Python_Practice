"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand):
    """Calculate and return the average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    true_average = card_average(hand)

    first_last_average = (hand[0] + hand[-1]) / 2

    middle_index = len(hand) // 2
    middle_value = hand[middle_index]

    return first_last_average == true_average or middle_value == true_average


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    even_cards = hand[0::2]
    odd_cards = hand[1::2]

    even_average = sum(even_cards) / len(even_cards)
    odd_average = sum(odd_cards) / len(odd_cards)

    return even_average == odd_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    # Assuming Jack has value 11
    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand