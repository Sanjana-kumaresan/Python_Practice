"""
Functions used in preparing Guido's gorgeous lasagna.

This module provides helper functions to calculate
bake time, preparation time, and total elapsed time.
"""

# Constants
EXPECTED_BAKE_TIME = 40      # minutes
PREPARATION_TIME = 2         # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time.

    :param elapsed_bake_time: int - time already spent baking
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate preparation time assuming 2 minutes per layer.

    :param number_of_layers: int
    :return: int - total preparation time
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total elapsed time (prep + bake).

    :param number_of_layers: int
    :param elapsed_bake_time: int
    :return: int - total elapsed time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


# Test prints
print("Expected Bake Time:", EXPECTED_BAKE_TIME)
print("Bake Time Remaining (10 mins passed):", bake_time_remaining(10))
print("Preparation Time (3 layers):", preparation_time_in_minutes(3))
print("Elapsed Time (3 layers, 20 mins baked):", elapsed_time_in_minutes(3, 20))
