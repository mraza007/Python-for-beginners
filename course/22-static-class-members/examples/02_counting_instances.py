"""Use a shared class attribute to count instances.

Run me:  python 02_counting_instances.py
"""

class Player:
    count = 0                 # shared across every Player

    def __init__(self, name):
        self.name = name
        Player.count += 1     # bump the shared counter on each new player

Player("Ann")
Player("Bo")
Player("Cy")

print("Players created:", Player.count)   # 3
