"""Solution — Exercise 2: Count the objects created."""

class Player:
    count = 0

    def __init__(self):
        Player.count += 1

Player()
Player()
Player()
print(Player.count)
