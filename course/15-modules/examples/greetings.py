"""A tiny custom module — just a Python file with functions.

Import it from another file with:  import greetings

Run me directly to see the demo:  python greetings.py
"""

def hello():
    return "Hello!"

def hey(name):
    return f"Hey {name}!"

# This block runs ONLY when the file is launched directly (python greetings.py),
# NOT when it is imported. That's because __name__ is "__main__" only for the
# file you actually run.
if __name__ == "__main__":
    print("Running greetings.py directly:")
    print(hello())
    print(hey("Ada"))
