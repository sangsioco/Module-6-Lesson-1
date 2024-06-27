import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 'Unknown')  # massValue gives the numeric value
            mass_exponent = planet.get('mass', {}).get('massExponent', '')  # massExponent gives the exponent part
            orbit_period = planet.get('sideralOrbit', 'Unknown')  # sideralOrbit gives the orbital period in days

            if mass != 'Unknown' and mass_exponent != '':
                mass = f"{mass}e{mass_exponent}"  # Combine value and exponent for scientific notation
            
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    return planets

def find_heaviest_planet(planets):
    heaviest_mass = -1
    heaviest_planet = None

    for planet in planets:
        if planet['isPlanet']:
            mass_value = planet.get('mass', {}).get('massValue')
            if mass_value and mass_value != 'Unknown':
                mass_value = float(mass_value)
                if mass_value > heaviest_mass:
                    heaviest_mass = mass_value
                    heaviest_planet = planet
    
    if heaviest_planet:
        name = heaviest_planet.get('englishName', 'Unknown')
        mass = heaviest_planet.get('mass', {}).get('massValue', 'Unknown')
        return name, mass
    else:
        return "Unknown", "Unknown"

# Example usage:
planets_data = fetch_planet_data()
name, mass = find_heaviest_planet(planets_data)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
