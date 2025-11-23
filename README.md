# python-learning-journey
# File: README.md
###########################
# 🐍 Python Learning Journey
# Welcome to my Python Learning Journey repository!
# This repo contains all the concepts, notes, exercises, and projects documenting my progress from beginner to advanced Python.
#
# ## 🚀 What This Includes
# - Basics of Python
# - Intermediate concepts
# - Advanced topics
# - Mini and major projects
# - Notes and learning summaries
#
# ## 📁 Folder Structure
# - basics/ — Beginner concepts and practice files
# - intermediate/ — Modules, OOP, file handling
# - advanced/ — Decorators, generators, algorithms
# - projects/ — Real projects and applications
# - notes/ — Notes, summaries, and explanations
#
# ## ⭐ Support
# If you like this repository, consider giving it a star!


###########################
# File: basics/hello_world.py
###########################
print("Hello, Python! This is the beginning of my learning journey.")


###########################
# File: intermediate/example_module.py
###########################
# Example of a simple Python module

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


###########################
# File: advanced/decorators_example.py
###########################
# Example of a Python decorator

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name):
    return f"Hello, {name}!"


###########################
# File: projects/mini_project_1.py
###########################
# Mini Project: Simple Calculator

def calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("+ , - , * , /")
    op = input("Choose operation: ")

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operation!")

# Uncomment to run
# calculator()


###########################
# File: notes/python_notes.md
###########################
# Python Notes

## Variables
Python variables do not require explicit type declaration.

## Loops
Python supports `for` and `while` loops.

## Functions
Defined using the `def` keyword.
