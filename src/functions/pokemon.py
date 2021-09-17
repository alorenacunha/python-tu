# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:22:19 2020

@author: rodolfo.neves
"""

def choosePokemonByHp(hp, pokemons):
    if(isinstance(hp,int) == False):
        raise TypeError("parameter has to be a int")
    pokemonsHp = pokemons["HP"]
    pokemonsName = pokemons["Name"]
    idxs = [i for i,x in enumerate(pokemonsHp) if x==hp]
    if(len(idxs) == 0):
        raise ValueError("parameter not found")
    first = idxs[0]
    return pokemonsName[first]

def getIndexbyName(name, pokemons):
    pokemonsName = pokemons["Name"]
    names = list(map(lambda x: x.lower(), pokemonsName))
    name_idxs = [i for i,item in enumerate(names) if item==name.lower()]
    if(len(name_idxs) == 0):
        raise ValueError("vish " + name + " is not a pokemon")
    first = name_idxs[0]
    return first

def getPropByName(prop, name, pokemons):
    print(prop)
    print(name)
    props = pokemons[prop]
    idx = getIndexbyName(name, pokemons)
    value = props[idx]
    return value

def getHpByName(name, pokemons):
    return getPropByName("HP", name, pokemons)

def getAttackByName(name, pokemons):
    return getPropByName("Attack", name, pokemons)

def getDefenseByName(name, pokemons):
    return getPropByName("Defense", name, pokemons)

def whoWins(pokemonAttack, pokemonsDefense, pokemons):
    atk_value = getAttackByName(pokemonAttack, pokemons)
    def_value =  getDefenseByName(pokemonsDefense, pokemons)
    
    if atk_value > def_value:
        return pokemonAttack
    elif atk_value < def_value:
        return pokemonsDefense
    else:
        return "Draw"

