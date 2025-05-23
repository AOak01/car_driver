import pygame
import pytest
from driving_game import *


def test_player_initilised():
    player = Player()
    assert player.x == 100
    assert player.y == 100

def test_player_move_up_one():
    player = Player()
    assert player.x == 