import pytest
from model import GameModel


def test_add_plant_and_zombie():
    m = GameModel()
    m.add_plant(100, 2)
    m.add_zombie(700, 2)
    assert len(m.plants[2]) == 1
    assert len(m.zombies[2]) == 1


def test_zombie_moves_in_update():
    m = GameModel()
    m.add_zombie(700, 1)
    z0 = m.zombies[1][0]
    m.update()
    assert z0.x == 699


def test_collision_stops_zombie():
    m = GameModel()
    m.add_plant(500, 3)
    m.add_zombie(520, 3)
    z = m.zombies[3][0]
    m.update()
    assert z.active is False


def test_no_collision_different_lane():
    m = GameModel()
    m.add_plant(500, 2)
    m.add_zombie(520, 3)
    z = m.zombies[3][0]
    m.update()
    assert z.active is True
    assert z.x == 519
