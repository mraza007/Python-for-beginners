"""Solution — Exercise 1: A shared class attribute."""

class Robot:
    kind = "robot"

r1 = Robot()
r2 = Robot()
print(r1.kind, r2.kind)
