import requests

#question 1 task 2 
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response:
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    name = data['name']
    print(f"{name}")
    for  ability in abilities:
        print(f"Ability: {ability}")

else:
    print("Could not get information for this Pokemon.")


# question 1 task 3

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response:
        return response.json()
    else:
        print("Could not retrieve nformation on the specified pokemon.")

def calculate_average_weight(pokemon_list):
    total = 0

    for pokemon in pokemon_list:
        total += pokemon['weight']
    if pokemon_list:
        return total / len(pokemon_list)
    else:
        return None
    
def main():
    pokemon = ['charmeleon', 'ivysaur', 'weedle']
    data_list = []

    for name in pokemon:
        data = fetch_pokemon_data(name)

        if data:
            data_list.append(data)

            abilities = [ability['ability']['name'] for ability in data['abilities']]
            print(f"{name}")

            for ability in abilities:
                print(f"Ability: {ability}")

    average_weight = calculate_average_weight(data_list)
    print(f"Average weight of the Pokemon enter: {average_weight: .2f}")

if __name__ == "__main__":
    main()