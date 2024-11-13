import requests

# question 2 task 2

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass_data = planet.get('mass', {})
            if mass_data and 'massValue' in mass_data:
                try:
                    mass = float(mass_data['massValue'])
                except (ValueError, TypeError):
                    mass = 0
            else:
                mass = 0
            orbit_period = planet.get('sideralOrbit', 'Unknown')

            planet_data.append({
                'name' : name,
                'mass' : mass,
                'orbit_period' : orbit_period
            })

            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet_data



# question 2 task 3

def find_heaviest_planet_data(planets):

    if not planets: 
        return('Unknown', 0)

    heaviest_planet = None
    max_mass = 0

    for planet in planets:

        mass = planet['mass']
        if isinstance(mass, (int, float)) and mass > max_mass:
            max_mass = mass
            heaviest_planet = planet
    
    if heaviest_planet:
        return (heaviest_planet['name'], heaviest_planet['mass'])
    else:
        return ("Unknown", 0)

def main():

    planets = fetch_planet_data()
    name, mass = find_heaviest_planet_data(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")


if __name__ == "__main__":
    main()