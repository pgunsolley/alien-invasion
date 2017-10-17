"""
A place to put observers

Observers should accept keyword arguments.
"""


def player_move_right(**kwargs):
    """
    Move the player to the right.

    :param event:
    :return:
    """
    kwargs['player'].moving_right = True


def player_move_left(**kwargs):
    """
    Move the player to the left.

    :param event:
    :param player:
    :return:
    """
    kwargs['player'].moving_left = True


def player_stop_moving_left(**kwargs):
    """
    Stop the character from moving.

    :return:
    """
    kwargs['player'].moving_left = False


def player_stop_moving_right(**kwargs):
    """
    Stop the character from moving.

    :return:
    """
    kwargs['player'].moving_right = False


def player_shoot(**kwargs):
    """
    Fire weapon.

    :param kwargs:
    :return:
    """
    kwargs['player'].fire_bullet()
