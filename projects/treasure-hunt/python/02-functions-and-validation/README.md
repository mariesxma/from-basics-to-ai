# 02 — Functions and validation

A complete Treasure Hunt game that builds on [01 — Foundations](../01-foundations/README.md).

## What changed

The original map, commands, treasure rules, and replay flow stay familiar. This version adds a difficulty menu and extracts damage and treasure checks into reusable functions. Inventory remains a simple list; route tracking and random rewards come in stage 3.

本阶段只增加难度选择和可复用函数。用熟悉的游戏练习参数、返回值和输入验证。

## Run

From the repository root:

```bash
python3 projects/treasure-hunt/python/02-functions-and-validation/game.py
```

Or open this folder and run `python3 game.py`. On Windows, use `py` if needed. Python 3 is the only requirement; no extra packages or earlier-stage imports are needed.

## Rules

Choose 1 (10 health), 2 (7 health), or 3 (5 health). Collect all three treasures and return to camp alive. Forest and river cost 1 health per entry; cave costs 2. Commands: `north`, `south`, `east`, `west`, `take`, `status`, `help`, `quit`. After winning, losing, or quitting, choose whether to replay.

A winning route at any difficulty: `north`, `take`, `east`, `take`, `south`, `take`, `west`. Each replay resets the map and player state.

每个阶段都是完整独立游戏。先选择难度，收集三个宝藏，活着回营地；重玩会重置状态。

## Guided comparison

Read the two `game.py` files side by side. Rebuild these changes in your own copy if you want hands-on practice.

| Step | Where to look | What to learn |
| --- | --- | --- |
| 1. Define reusable rules | `apply_damage(health, damage)` | Parameters receive arguments; `return` sends back a result. `max(0, ...)` prevents negative health. |
| 2. Represent no result | `find_treasure(room, location)` | Return a room label or `None`. Use `is not None` before collecting. |
| 3. Display choices | Start of `choose_health()` | Tuples hold names and health values; `for` and `range()` visit indexes; f-strings display numbered choices. |
| 4. Validate input | Input loop in `choose_health()` | `int()` converts text, `except ValueError` handles non-integers, `continue` retries. Check the range before indexing with `choice - 1`. |
| 5. Connect the functions | `play_game()` | Call each helper and use its returned value. The game loop still controls the expedition. |

先理解函数接收什么、返回什么，再看游戏如何调用它。输入验证分两步：能否转换为整数，以及整数是否在允许范围内。

## Optional quests

- Add a fourth difficulty; update the prompt and range message as well as the tuples.
- Write a `has_won(location, treasures)` helper and use its returned boolean.

## Completion checklist

- [ ] Win a game and replay.
- [ ] Enter text, `1.5`, `0`, and `4`; explain why they are rejected.
- [ ] Explain the difference between a parameter and an argument using `apply_damage`.
- [ ] Predict `apply_damage(3, 5)` and `find_treasure` for camp.
- [ ] Explain why the displayed menu starts at 1 but tuple indexes start at 0.

[Next: 03 — Collections and progress](../03-collections-and-progress/README.md) · [All Python stages](../README.md)
