"""A small, complete treasure hunt using only Python's built-in features."""

import random


def create_rooms():
    # Each room is a dictionary. Exits map directions to other room names.
    return {
        "camp": {"exits": {"north": "forest", "east": "river"}, "treasure": False, "damage": 0},
        "forest": {"exits": {"south": "camp", "east": "cave"}, "treasure": True, "damage": 1},
        "river": {"exits": {"west": "camp", "north": "cave"}, "treasure": True, "damage": 1},
        "cave": {"exits": {"west": "forest", "south": "river"}, "treasure": True, "damage": 2},
    }


def choose_health():
    """Convert menu input to a number and return the chosen starting health."""
    names = ("Explorer", "Adventurer", "Survivor")
    health_options = (10, 7, 5)
    for index in range(len(names)):
        print(f"{index + 1}. {names[index]}: {health_options[index]} health")
    while True:
        try:
            choice = int(input("Choose difficulty (1-3): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if 1 <= choice <= len(names):
            return health_options[choice - 1]
        print("Choose 1, 2, or 3.")


def apply_damage(health, damage):
    """Return remaining health, never below zero."""
    return max(0, health - damage)


def find_treasure(room, location):
    """Return a treasure label, or None when this room has no treasure."""
    if room["treasure"]:
        return location
    return None


def show_status(treasures, visited, route, coins, total_treasures, total_rooms):
    progress = len(treasures) / total_treasures * 100
    print(f"Treasure progress: {progress:.1f}% | Bonus coins: {coins}")
    print(f"Unique rooms visited: {len(visited)}/{total_rooms}")
    print("Recent route:", " -> ".join(route[-3:]))
    if not treasures:
        print("Your inventory is empty.")
    for number, treasure in enumerate(treasures, start=1):
        print(f"{number}. Treasure from {treasure}")


def play_game():
    rooms = create_rooms()
    location = "camp"
    treasures = []
    visited = {"camp"}
    route = ["camp"]
    coins = 0
    total_treasures = 0
    for room in rooms.values():
        if room["treasure"]:
            total_treasures += 1
    print("\nTREASURE HUNT")
    health = choose_health()
    print(f"Collect all {total_treasures} treasures and return to camp alive.")
    print("Hazards hurt every time you enter a room. Plan your route!")
    print("Commands: north, south, east, west, take, status, help, quit")

    while True:
        room = rooms[location]
        print("\nLocation:", location, "| Health:", health, "| Treasure:", len(treasures), "/", total_treasures)
        print("Exits:", ", ".join(room["exits"]))
        if room["treasure"]:
            print("There is treasure here! Type take to collect it.")

        command = input("> ").strip().lower()
        if command == "quit":
            print("You leave the expedition. Come back for another adventure!")
            return
        elif command == "help":
            print("Type an exit direction to move. Use take to collect treasure.")
            print("Use status to view your collection, or quit to end the expedition.")
        elif command == "status":
            show_status(treasures, visited, route, coins, total_treasures, len(rooms))
        elif command == "take":
            treasure = find_treasure(room, location)
            if treasure is not None:
                treasures.append(treasure)
                room["treasure"] = False
                reward = random.randint(1, 5)
                coins += reward
                print(f"Treasure collected! Bonus: {reward} coins.")
            else:
                print("There is no treasure to collect here.")
        elif command in room["exits"]:
            location = room["exits"][command]
            route.append(location)
            visited.add(location)
            damage = rooms[location]["damage"]
            health = apply_damage(health, damage)
            if damage > 0:
                print("A hazard costs you", damage, "health.")
            if health <= 0:
                print("You ran out of health. Game over!")
                return
            if location == "camp" and len(treasures) == total_treasures:
                print(f"You returned to camp with all {total_treasures} treasures. You win!")
                show_status(treasures, visited, route, coins, total_treasures, len(rooms))
                return
        else:
            print("That command is not available here. Type help for instructions.")


def main():
    try:
        while True:
            play_game()
            while True:
                answer = input("Play again? (yes/no): ").strip().lower()
                if answer in ("yes", "no"):
                    break
                print("Please type yes or no.")
            if answer == "no":
                print("Thanks for playing!")
                return
    except (EOFError, KeyboardInterrupt):
        print("\nAdventure closed. See you next time!")


if __name__ == "__main__":
    main()
