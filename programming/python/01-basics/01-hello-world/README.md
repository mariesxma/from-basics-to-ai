# Lesson 1: Hello, world!

## What you will learn

- What a Python program is.
- How to display text with `print()`.
- How to run a Python file and change its output.

## The idea

A program is a set of instructions a computer follows. A Python file stores those instructions as text and ends in `.py`.

Our first instruction is:

```python
print("Hello, world!")
```

`print()` is a built-in function that displays a value. The parentheses contain what you want to display. The quotation marks tell Python that `Hello, world!` is text, called a **string**. The quotation marks themselves are not printed.

You can use matching single or double quotation marks. We use double quotes in this example.

## Run the example

From the repository root:

```bash
python3 programming/python/01-basics/01-hello-world/hello.py
```

On Windows, use `py` instead of `python3` if needed.

Expected output:

```text
Hello, world!
I am learning Python.
My journey from basics to AI starts here.
```

Python runs these instructions from top to bottom. Each `print()` call starts a new line of output by default. A line beginning with `#` is a comment: it explains the code and is not executed.

## Try it yourself

Open [exercise.py](exercise.py) in your editor and complete the three tasks in its comments. Save the file, then run:

```bash
python3 programming/python/01-basics/01-hello-world/exercise.py
```

Your wording can be different. Aim to print three lines: a greeting, something you want to learn, and why you want to learn it.

## Common mistakes

- **Missing quotation mark or closing parenthesis:** Python may report a `SyntaxError`. Check that quotes and parentheses come in matching pairs.
- **Using `Print` instead of `print`:** names are case-sensitive, so use lowercase `print`.
- **File not found:** check that your terminal is in the repository root and that the file path matches the command above.

## Check your understanding

Before moving on, explain why text needs quotation marks and predict what happens if you swap two `print()` lines. Then try it.

Next planned lesson: variables and basic types.
