# Lesson 1: Plan your study time

How much time will you spend learning if you study for 25 minutes, four days a week? Build a small calculator to find out, then change it to match your own schedule.

No previous programming experience is needed. Follow the [Python setup instructions](../../README.md) first.

## Build something useful

A Python program is a sequence of instructions saved in a `.py` file. This one stores a study schedule, calculates its weekly total, and displays the result:

```python
topic = "Python"
minutes_per_day = 25
days_per_week = 4

weekly_minutes = minutes_per_day * days_per_week
weekly_hours = weekly_minutes / 60

print("Study topic:", topic)
print("Minutes per week:", weekly_minutes)
print("Hours per week:", round(weekly_hours, 2))
```

## Run it

Open a terminal in the repository root and run:

```bash
python3 programming/python/01-basics/01-study-planner/study_planner.py
```

On Windows, use `py` instead of `python3` if that is how your installation runs Python.

Expected output:

```text
Study topic: Python
Minutes per week: 100
Hours per week: 1.67
```

## Understand each part

| Code | What it means |
| --- | --- |
| `topic = "Python"` | Assign text to a variable named `topic`. A variable is a name you can use to refer to a value. Text is called a string and goes inside quotes. |
| `minutes_per_day = 25` | Assign a whole number, called an integer. Numbers used in calculations do not need quotes. |
| `minutes_per_day * days_per_week` | Multiply the two values. `*` means multiplication. |
| `weekly_minutes / 60` | Divide minutes by 60 to get hours. `/` produces a floating-point number, which can represent a fractional value. |
| `print("Minutes per week:", weekly_minutes)` | Display a label and a value, separated by a space. Each call ends with a new line by default. |
| `round(weekly_hours, 2)` | Round the value to two decimal places for display. This does not change the value stored in `weekly_hours`. |

Python runs these lines from top to bottom, so assign a variable before using it. The `=` sign assigns a value; it does not ask whether two values are equal. Lines beginning with `#` are comments for the reader.

## Make it yours

Open [exercise.py](exercise.py), which contains the working calculator and tasks to extend it:

1. Change the topic, minutes per day, and days per week to match your schedule. Use a positive number of minutes and between 1 and 7 days; this first version assumes sensible values.
2. Add a variable named `weeks` with a value of `6`. Calculate `total_minutes` using `weekly_minutes * weeks`, then print it with a label.
3. Try 30 minutes a day, five days a week, for six weeks. Predict the results before running.

Save your file, then run:

```bash
python3 programming/python/01-basics/01-study-planner/exercise.py
```

For the last task, you should get **150 minutes per week**, **2.5 hours per week**, and **900 total minutes**. Your labels can be different.

## When something goes wrong

- **`NameError`:** check your variable spelling and that you assigned it before using it. Python treats uppercase and lowercase letters differently.
- **`SyntaxError`:** check for a missing quote or closing parenthesis.
- **Unexpected calculations:** use `25`, not `"25"`, for a number. Quoted digits are text.
- **File not found:** check that your terminal is in the repository root and the path matches the command above.

## Why this matters for AI

Data and AI programs also store values, perform calculations, and display results. This planner introduces those building blocks; it uses ordinary arithmetic and does not use an AI model.

Next planned lesson: accept a study schedule with `input()` and convert the typed text into numbers.
