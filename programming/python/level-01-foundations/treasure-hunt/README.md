# Treasure Hunt

**Level 1 — Foundations · Complete terminal game · No extra packages**

Explore four rooms, collect three treasures, and return to camp before your health runs out. The game includes movement, collection, hazards, win and loss conditions, help, input validation, quitting, and replay.

## Play

Follow the [Python setup](../../README.md), then run this from the repository root:

```bash
python3 programming/python/level-01-foundations/treasure-hunt/game.py
```

On Windows, use `py` instead of `python3` if needed. Type a command and press Enter.

```text
forest (1 damage) ---- cave (2 damage)
      |                      |
camp (safe) ---------- river (1 damage)
```

Up is north; right is east. You start at camp with 7 health. Every entry into a hazardous room costs health, including return visits. Each non-camp room has one treasure, which you collect with `take`. Invalid commands and collecting treasure cost no health. You lose at zero health and win by bringing all three treasures back to camp alive.

Commands: `north`, `south`, `east`, `west`, `take`, `status`, `help`, `quit`. After a win, loss, or quit, choose whether to play again. A replay resets everything.

<details>
<summary>Need a hint? Show a winning route</summary>

Enter these commands one at a time: `north`, `take`, `east`, `take`, `south`, `take`, `west`. You return to camp with 3 health and all three treasures.

</details>

## Guided build

Read [game.py](game.py) alongside these stages. To rebuild it yourself, create a separate `my_game.py` and add one stage at a time. Each stage contributes to the same game.

### 1. Describe the world

Start with `create_rooms()`. `def` defines a function: a named group of instructions. Calling it with `create_rooms()` runs those instructions. `return` sends a value back to the caller.

The world is a **dictionary**, written with `{}`. It connects keys such as `"camp"` to values. Each room is another dictionary containing exits, treasure, and damage. `rooms["camp"]["exits"]` looks up the camp's exits. Quoted values are strings (text); `True` and `False` are booleans (yes/no values).

Build the map first and try printing one room's exits. Can you explain why an exit needs both a direction and a destination?

### 2. Create the player state

In `play_game()`, `location`, `health`, and `treasures` are variables: names for values. `=` assigns a value. Health is an integer (whole number). `treasures = []` creates an empty **list**, which stores a sequence of values.

`print()` displays information. Commas let it display several values together. `len(treasures)` counts collected treasures. Create your starting state and print it before adding movement.

### 3. Let the player act

`while True` repeats the game loop until a `return` ends the function. Indentation groups the instructions inside a function, loop, or condition; keep it consistent with the example.

`input()` waits for typed text. `.strip().lower()` removes surrounding whitespace and makes text lowercase, so ` NORTH ` works too. `if`, `elif`, and `else` choose which instructions run. `==` compares values; unlike `=`, it does not assign them.

Start by handling `help` and `quit`. Then use `command in room["exits"]` to check whether a move exists before looking up the destination. An unsupported command should show a message and keep the game running.

### 4. Add treasure and danger

`treasures.append(location)` adds an item to the list. Setting `room["treasure"] = False` prevents collecting it twice. Every move subtracts the destination's damage from health.

Add these rules and test them: collect the same treasure twice, revisit a dangerous room, and inspect your collection with `status`. The expression `", ".join(treasures)` turns the list of room names into readable text.

### 5. Finish the game

`health <= 0` checks for a loss. The win condition uses `and`: the player must be at camp **and** have three treasures. `return` ends the current expedition in either case.

The outer loop in `main()` offers a replay. Calling `play_game()` again creates fresh rooms and player state. The inner replay loop accepts only `yes` or `no`; `break` exits that inner loop when the answer is valid.

The final `if __name__ == "__main__":` starts the game when this file runs directly. The `try` / `except` block handles closing terminal input or pressing Ctrl+C gracefully. These are supporting details you will explore more deeply in later levels.

## Optional quests

- **Cartographer:** add a fifth room and connect it in both directions. Keep the game winnable.
- **Healer:** add a potion that restores health once per expedition.
- **Navigator:** add a `map` command that displays the map.
- **Game designer:** introduce a difficulty choice that changes starting health.

Complete the core game first. Each quest is a small extension to the same working project.

## Completion checklist

- [ ] Run the game and win an expedition.
- [ ] Trigger a loss and successfully replay with fresh state.
- [ ] Try an invalid command and collect a treasure twice; explain what happens.
- [ ] Explain how the room dictionary and treasure list differ.
- [ ] Explain where the loop continues and where the game ends.
- [ ] Change one game rule and verify its effect.

Finishing this checklist completes Level 1. Quests are optional; there is no automatic score or unlock system.

[Back to the level path](../../README.md)
