#!/usr/bin/python3

import requests

pokeapi = "https://pokeapi.co/api/v2/pokemon/"

def main():
    pokedex = requests.get(f"{pokeapi}?limit=100000")
    pokedex = pokedex.json()

    user_input = input("What's that pokemon? ")



    for pokemon in pokedex["results"]:
        if user_input == pokemon.get("name"):
            print(f'It\'s {pokemon.get("name")}!')
            #print(pokemon.get("url"))

            info = pokemon.get("url")
            pokeinfo = requests.get(info)
            pokeinfo = pokeinfo.json()

            for poke in pokeinfo["abilities"]:
                print("Ability:",poke["ability"]["name"])

            

if __name__ == "__main__":
    main()
