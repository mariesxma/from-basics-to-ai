# 03 — Collections and progress

A complete Treasure Hunt game that builds on [02 — Functions and validation](../02-functions-and-validation/README.md).

## What changed

Keep the difficulty menu and helper functions. Add numbered inventory, unique-room tracking, recent route history, percentage progress, and bonus coins. The treasure target is counted from the map at the start of each game.

本阶段保留上一版，增加背包编号、去重记录、路线历史、百分比和金币。比较列表与集合各自适合记录什么。

## Run

From the repository root:

```bash
python3 projects/treasure-hunt/python/03-collections-and-progress/game.py
```

Or open this folder and run `python3 game.py`. On Windows, use `py` if needed. Python 3 is the only requirement; no extra packages or earlier-stage imports are needed.

## Rules

Choose 1 (10 health), 2 (7 health), or 3 (5 health). Collect all three treasures and return to camp alive. Forest and river cost 1 health per entry; cave costs 2. Commands: `north`, `south`, `east`, `west`, `take`, `status`, `help`, `quit`. After winning, losing, or quitting, choose whether to replay.

A winning route at any difficulty: `north`, `take`, `east`, `take`, `south`, `take`, `west`. Each replay resets the map and player state.

每个阶段都是完整独立游戏。先选择难度，收集三个宝藏，活着回营地；重玩会重置状态。

Use `status` to inspect progress. Each treasure awards 1–5 bonus coins once. Coins affect only the score, so randomness does not change the winning route. Everything resets on replay.

## Guided comparison

Compare this `game.py` with stage 2; the extra state and `show_status()` are the main additions.

| Step | Where to look | What to learn |
| --- | --- | --- |
| 1. Count the goal | Start of `play_game()` | Loop through `rooms.values()` and increment the treasure count with `+=`. |
| 2. Record movement | Movement branch | A list records every stop in order; a set records unique rooms with `.add()`. |
| 3. Show recent history | `show_status()` | `route[-3:]` selects up to three latest stops without changing the original list; `.join()` displays them. |
| 4. Number inventory | `show_status()` | `enumerate(..., start=1)` supplies a number and an item; `if not treasures` handles an empty list. |
| 5. Show progress | `show_status()` | Division gives a float; an f-string with `:.1f` displays one decimal place. |
| 6. Award coins | Import and `take` branch | Import the standard-library `random` module; `randint(1, 5)` includes both endpoints. Add coins only on successful collection. |

列表允许重复、保留顺序；集合记录唯一值。随机奖励只在成功拿到宝藏时发生，不能重复刷同一个宝藏。

## Optional quests

- Display an exploration percentage as well as treasure progress.
- Show the full route on a new `history` command.
- Add a treasure room with valid exits and enough health to complete the route; check that the target count updates.

## Completion checklist

- [ ] Win, lose, and replay with fresh state.
- [ ] Check status before and after collecting a treasure.
- [ ] Visit a room twice; explain the different list and set results.
- [ ] Explain `route[-3:]` when the route contains only one stop.
- [ ] Take the same treasure twice and confirm no extra coins appear.
- [ ] Explain why the progress percentage is predictable but the coin score can vary.

## Maintainer checks

```bash
python3 -m unittest discover -s projects/treasure-hunt/python/03-collections-and-progress -p 'test_*.py'
```

Tests use fixed rewards to verify scoring reliably. Learning the test framework is optional at this stage.

Next planned stage: **04 — Classes and objects**, reorganizing the game around Player, Room, and Game. It is not implemented yet.

[All Python stages](../README.md)
