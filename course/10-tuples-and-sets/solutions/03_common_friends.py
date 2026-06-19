"""Solution — Exercise 3: Friends in common."""

alice = {"sam", "jo", "kim"}
bob = {"jo", "kim", "lee"}

common = alice & bob
print(f"Common: {sorted(common)}")
