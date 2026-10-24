import random
import requests

names = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Charizard"]


def play():
    name = random.choice(names)

    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        if response.status_code != 200:
            print("Pokémon not found or API unavailable.")
            return
        data = response.json()
    except (requests.RequestException, ValueError):
        print("Connection or data error. Please try again.")
        return

    print("Guess the Pokémon! Choices:", ", ".join(names))
    print("Height:", data["height"] / 10, "meters")
    print("Weight:", data["weight"] / 10, "kg")

    for attempt in range(3):
        guess = input(f"Guess {attempt + 1}/3: ").strip().lower()
        if guess == data["name"]:
            print("Correct! You win!")
            return
        if guess not in names:
            print("Invalid choice. Choose from the list.")
        else:
            print("Wrong guess!")

    print("The Pokémon was", data["name"].capitalize())


play()
