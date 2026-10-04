# Treasure Hunt — Python

## Setup

Install Python 3 from [python.org](https://www.python.org/downloads/) and choose a text editor. Check your installation:

```bash
python3 --version
```

On Windows, try `py --version` and replace `python3` with `py` in the commands below if needed.

## Choose a stage

Each folder is a complete standalone snapshot. Start at 01 and compare each later version with the previous one. Earlier games stay available rather than being overwritten.

每个文件夹都是完整可运行的版本，按顺序比较变化；新阶段不会覆盖旧阶段。

| Stage | What it adds | Status |
| --- | --- | --- |
| [01 — Foundations](01-foundations/README.md) | Original terminal game: variables, conditions, loops, basic collections and functions | Playable |
| [02 — Functions and validation](02-functions-and-validation/README.md) | Difficulty menu, parameters, return values, numeric input and exceptions | Playable |
| [03 — Collections and progress](03-collections-and-progress/README.md) | Inventory, sets, slicing, percentages and random rewards | Playable |
| 04 — Classes and objects | Player, Room and Game classes | Planned |
| 05 — Files and saving | Save/load, JSON, modules and tests | Planned |
| 06 — Graphical interface | Window, buttons and events | Planned |

Only implemented stages have folders. Each README explains what changed, what to learn, how to run, and how to practise.

## Run foundations

From the repository root:

```bash
python3 projects/treasure-hunt/python/01-foundations/game.py
```

Or open `projects/treasure-hunt/python/01-foundations/` in your editor and run this from that folder:

```bash
python3 game.py
```

This version needs no extra packages or accounts. Follow the [project guide](01-foundations/README.md) to play, understand the code, and complete quests.

[Other Treasure Hunt versions](../README.md)

## What does foundations cover?

The [learning map](01-foundations/LEARNING-MAP.md) lists the stages, concepts used in the game, and foundations still to practise.
