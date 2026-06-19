"""Generator expressions: comprehensions with () instead of [].

Run me:  python 03_generator_expression.py
"""

squares = (n * n for n in range(1, 6))
print(squares)         # <generator object ...>  (nothing computed yet)
print(list(squares))   # [1, 4, 9, 16, 25]

# Great with sum()/max(): no intermediate list is built.
print(sum(n * n for n in range(1, 6)))   # 55
print(max(n * n for n in range(1, 6)))   # 25
