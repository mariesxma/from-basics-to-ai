# Foundations learning map · 基础学习地图

This level teaches a useful first set of Python foundations through one complete game. It does **not** cover every Python fundamental. Completing it means you understand this project, not that you have mastered all of Python.

这个级别用一个完整游戏串起第一批 Python 基础。完成它代表你能理解和修改这个项目，不代表已经学完所有 Python 基础。

Keep the folder name `01-foundations/`. Use this map to see the stages and learning content without splitting the game into many separate projects.

文件夹保留简洁名称；学习阶段写在这里。所有阶段都围绕同一个 `game.py`。

## Stages · 学习阶段

These stages match the five sections in the [guided build](README.md#guided-build). Start by running the game, then follow the stages. Read the named functions in [game.py](game.py); the names remain useful even when line numbers change.

先运行游戏，再按下面的阶段学习。每个阶段对应 README 的一个构建步骤。

| Stage 阶段 | Game feature 游戏功能 | Python content 学习内容 | Where to look 代码位置 | Check your understanding 验收 |
| --- | --- | --- | --- | --- |
| 1. Describe the world 描述世界 | Rooms and exits 房间与出口 | `def`, calling functions, returning a value, nested dictionaries, keys, strings, booleans, comments, indentation | `create_rooms()` | Explain how camp's north exit leads to forest. 解释营地如何通过 north 找到森林。 |
| 2. Create player state 创建玩家状态 | Location, health, collection 位置、血量、收集清单 | Variables, assignment, integers, empty lists, `print()`, `len()` | Beginning of `play_game()` | Change starting health and predict the effect. 修改初始血量并预测结果。 |
| 3. Let the player act 接收行动 | Input, commands, movement 输入、指令、移动 | `input()`, `.strip()`, `.lower()`, `while`, `if/elif/else`, `==`, membership with `in`, dictionary lookup | Command loop in `play_game()` | Explain why ` NORTH ` works and an unavailable direction does not. 解释输入处理和无效方向。 |
| 4. Add treasure and danger 加入宝藏和危险 | Collection and health changes 收集与扣血 | `.append()`, dictionary mutation, subtraction, comparisons, `.join()`, empty-string fallback with `or` | `take` and movement branches | Explain why treasure cannot be collected twice and why revisits hurt. 解释为什么不能重复拿宝藏，以及为什么重返房间会扣血。 |
| 5. Finish and replay 结束与重玩 | Win, loss, quit, replay 胜负、退出、重玩 | `and`, `return`, nested loops, `break`, fresh local state; introduction to tuples, `try/except`, and the entry-point guard | End of `play_game()` and `main()` | Win, lose, replay, and explain which loop/function each exit ends. 实际验证胜负和重玩，解释退出的是哪层循环或函数。 |

## Coverage · 覆盖范围

### Practised directly · 已有实际练习

- Variables and basic values: strings, integers, booleans. 变量、字符串、整数、布尔值。
- Lists and nested dictionaries: lookup, adding items, and changing values. 列表与嵌套字典的读取和修改。
- Input/output and basic string methods. 输入输出和基本字符串方法。
- Conditions, comparisons, boolean operations, and membership checks. 条件、比较、逻辑运算和成员判断。
- `while` loops, nested loops, and `break`. 循环、嵌套循环和跳出循环。
- Defining and calling functions, returning values, and ending a function. 定义和调用函数、返回值和结束函数。
- Reading program flow and checking behavior manually. 阅读执行流程和手动验证行为。

### Introduced, not explored deeply · 出现了，但还没深入

- Tuples: `("yes", "no")` groups accepted answers. 元组这里只用于保存可接受的回答。
- Exceptions: `EOFError` and `KeyboardInterrupt` provide a graceful exit. 异常这里只处理输入结束和键盘中断。
- Local state and mutable objects: `room` refers to a dictionary inside `rooms`; it is not a copy. 局部变量与可变对象；修改 `room` 也会修改地图中的那个房间。
- `if __name__ == "__main__"`: starts the game when run directly. 入口判断这里只用于启动程序。

### More foundations to practise · 后续还要补的基础

These are **planned exercises**, not features already implemented in the game. They can be learned through extensions or another foundations project.

下面是计划练习，并非当前游戏已经具备的功能。可以通过扩展游戏或其他同级项目练习。

| Topic 主题 | Same-game practice idea 同背景练习 |
| --- | --- |
| Function parameters and arguments 函数参数 | Write `apply_damage(health, damage)` that returns the new health. |
| `for`, `range()`, and iteration 遍历 | Print a numbered inventory, one item per line. |
| Numeric conversion and `ValueError` 数字转换与错误处理 | Ask for a starting-health number; handle non-numeric and invalid values. |
| Floats, division, and formatting 浮点数、除法、格式化 | Show the percentage of treasures collected with an f-string. |
| List indexing and slicing 列表索引和切片 | Record a route and show its latest three stops. |
| Sets and uniqueness 集合与去重 | Track the unique rooms visited. |
| `None` and optional results 空值与可选结果 | Have a treasure-search function return `None` when nothing is found. |
| Imports and standard-library modules 导入和标准库 | Add random rewards, then explain how randomness changes repeatable testing. |
| Debugging and simple assertions 调试与简单断言 | Check a damage calculation for zero damage and damage greater than remaining health. |

File handling, JSON saves, splitting code into modules, and automated tests belong to the planned intermediate version in this repository. Classes and graphical interfaces come later. This is our learning sequence, not a universal boundary for what counts as Python foundations.

文件读写、JSON 存档、多文件组织和自动化测试安排在中级版本；类和图形界面在后面。这是本仓库的学习顺序，不是 Python 基础的唯一划分标准。

## Completion · 完成标准

Use the [project completion checklist](README.md#completion-checklist). For each stage above, explain the feature in your own words and demonstrate its behavior. Optional extensions do not have to be completed to finish this first project.

按项目清单验收；能用自己的话解释每阶段功能，并运行演示。完成第一项目不要求一次做完所有扩展。
