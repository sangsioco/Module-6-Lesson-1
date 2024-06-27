# Task 2: fetching data from the Pokemon API for Pikachu
import requests
import json


response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

"""
{
    "name": "Pikachu"
    "type": "Electric"
    "level": 25
}
"""
pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["types"])
print(pikachu_data["abilities"])

# Task 3: Analyzing and displaying data for Pickachu, Bulbasur, and Charmander

# pikachu: https://pokeapi.co/api/v2/pokemon/pikachu
# bulbasaur: https://pokeapi.co/api/v2/pokemon/bulbasaur
# charmander: https://pokeapi.co/api/v2/pokemon/charmander

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        pokemon = response.json()

        name = pokemon.get("name", 'No name')
        abilities = pokemon.get("abilities", [])
        weight = pokemon.get("weight", 0)

        print(f"Name: {name}")
        print("Abilities:")
        for ability_info in abilities:
            ability = ability_info.get("ability", {})
            ability_name = ability.get("name", "Unknown")
            print(f" - {ability_name}")

        return weight

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0

    for pokemon_name in pokemon_list:
        weight = fetch_pokemon_data(pokemon_name)
        if weight is not None:
            total_weight += weight
            count += 1

    if count > 0:
        average_weight = total_weight / count
        print(f"Average weight: {average_weight:.2f}")
    else:
        print("No valid Pokémon weights found.")

# Example usage:
pokemon_list = ["pikachu", "bulbasaur", "charmander"]
calculate_average_weight(pokemon_list)
