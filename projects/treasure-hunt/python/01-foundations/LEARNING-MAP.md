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
| 4. Add treasure and danger 加入宝藏和危险 | Collection and health changes 收集与扣血 | `.append()`, dictionary mutation, subtraction, comparisons, `.join()`, `None` checks | `take` and movement branches; see stage 7 helpers | Explain why treasure cannot be collected twice and why revisits hurt. 解释为什么不能重复拿宝藏，以及为什么重返房间会扣血。 |
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

- Tuples also store difficulty names and health options; see stage 6. 元组也用于难度菜单，见阶段 6。
- Exceptions handle terminal interruptions and invalid numeric input; more exception patterns come later. 异常现在也处理无效数字输入，更多模式留待后续。
- Local state and mutable objects: `room` refers to a dictionary inside `rooms`; it is not a copy. 局部变量与可变对象；修改 `room` 也会修改地图中的那个房间。
- `if __name__ == "__main__"`: starts the game when run directly. 入口判断这里只用于启动程序。

## Stages 6–9: expanded foundations

These stages are implemented in the same `game.py`. They extend the five-stage guided build rather than creating another project.

这些阶段已经在同一个游戏里实现，接着前五阶段继续学。

| Stage | Feature | Concepts | Where | Try it |
| --- | --- | --- | --- | --- |
| 6. Choose difficulty 选择难度 | Numbered menu with safe input | Tuples, `for`, `range()`, indexing, `int()`, `ValueError`, `continue`, chained comparisons | `choose_health()` | Enter `hello`, `0`, `4`, then `2`. Explain why only the last choice is accepted. |
| 7. Reuse rules 复用规则 | Damage and treasure helpers | Parameters, arguments, returned values, `max()`, `None`, `is not None` | `apply_damage()`, `find_treasure()` | Predict `apply_damage(3, 5)` and why an empty room returns `None`. |
| 8. Track progress 记录进度 | Inventory, recent route, visited rooms | Sets and `.add()`, list `.append()`, negative slicing, `enumerate()`, division, floats, f-strings | `show_status()` and movement | Visit the same room twice: why does the route grow but the set count stay the same? |
| 9. Award a bonus 随机奖励 | One random coin reward per treasure | Standard-library import, `random.randint()`, `+=`, randomness | Import and `take` branch | Take the same treasure twice; check that coins increase only once. |

### How the new code works · 新代码怎么理解

- `choose_health()` uses `range(len(names))` to visit menu indexes. A user picks 1–3, while tuples use indexes 0–2, so lookup uses `choice - 1`. `int()` converts typed text; `except ValueError` handles invalid text and `continue` starts the next input attempt.
  菜单从 1 开始显示，但索引从 0 开始；输入不是整数时提示并重问。
- `apply_damage(health, damage)` receives two arguments and returns a calculated value. The caller assigns the result back to `health`. `max(0, ...)` prevents negative health.
  函数接收数据、计算、返回结果；调用方更新血量。
- `find_treasure()` returns a room name or `None`, meaning no result. `is not None` checks whether a treasure was found before collecting it.
  `None` 表示没有找到宝藏，不是字符串，也不是数字零。
- `visited` is a set: adding an existing room does not duplicate it. `route` is a list: each move adds a stop, including repeats. `route[-3:]` selects up to the latest three entries without changing the original list.
  集合记录去过哪些房间；列表记录按顺序怎么走的；切片取最近三步。
- `enumerate(treasures, start=1)` supplies both a display number and an item. `progress = len(treasures) / total_treasures * 100` produces a percentage; `{progress:.1f}` displays one decimal place in an f-string.
  编号遍历同时拿到序号和内容；除法计算比例，格式化控制显示小数位。
- `random.randint(1, 5)` picks an integer including both endpoints. `coins += reward` adds that amount. Tests can replace the random draw with a fixed value to check scoring reliably. Randomness affects only the bonus, so the winning route stays predictable.
  随机金币在 1 到 5 之间；测试固定奖励值，避免结果时好时坏。
- A `for` loop over `rooms.values()` counts available treasures when a game starts. The win condition uses that count instead of a fixed number, so adding a treasure room does not require rewriting the win rule.
  开局统计地图里的宝藏数量，胜利条件跟着地图变化。

### Still to practise · 仍需补充

The game now practises parameters, numeric conversion, iteration, tuples, sets, slicing, floats, formatting, imports, and `None`. It still does not cover every Python fundamental. Further practice can include more string/list operations, copying versus shared references, default arguments, and debugging with breakpoints. These are not yet dedicated lessons.

现在新增基础已有实际功能承载，但仍不是全部 Python 基础；还可以练习更多容器操作、复制与引用、默认参数和断点调试。

File handling, JSON saves, splitting code into modules, and automated tests belong to the planned intermediate version in this repository. Classes and graphical interfaces come later. This is our learning sequence, not a universal boundary for what counts as Python foundations.

文件读写、JSON 存档、多文件组织和自动化测试安排在中级版本；类和图形界面在后面。这是本仓库的学习顺序，不是 Python 基础的唯一划分标准。

## Completion · 完成标准

Use the [project completion checklist](README.md#completion-checklist). For each stage above, explain the feature in your own words and demonstrate its behavior. Optional extensions do not have to be completed to finish this first project.

按项目清单验收；能用自己的话解释每阶段功能，并运行演示。完成第一项目不要求一次做完所有扩展。
