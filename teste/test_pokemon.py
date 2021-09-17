
import os
import sys
import pandas as pd
import pytest
from src.functions.pokemon import *

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


base = pd.read_csv("src/data/Pokemon.csv")

def test_choosePokemonByHp():
    """get hp correctly"""
    assert choosePokemonByHp(80, base) == "Venusaur"
    assert choosePokemonByHp(39, base) == "Charmander"
    """not get hp correctly"""
    assert choosePokemonByHp(39, base) != "Venusaur"
    assert choosePokemonByHp(80, base) != "Charmander"
    """get dont have this hp"""
    with pytest.raises(TypeError):
        choosePokemonByHp('2', base)
    """get invalid parameter"""
    with pytest.raises(ValueError):
        choosePokemonByHp(2, base)

def test_getIndexByName():
    """get prop generation correctly"""
    assert getIndexbyName("Venusaur", base) == 2
    """prop not found"""
    with pytest.raises(ValueError):
        getIndexbyName("Lorena", base)

def test_whoWins():
    """venosaur win charmander"""
    assert whoWins("Venusaur",  "Charmander", base) == "Venusaur"
