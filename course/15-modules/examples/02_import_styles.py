"""Three ways to import.

Run me:  python 02_import_styles.py
"""

import random            # the whole module
import math as m         # give it a shorter alias
from math import sqrt, pi  # pull specific names in directly

print(m.floor(2.9))   # 2
print(sqrt(25))       # 5.0   (no "math." prefix needed)
print(pi)             # 3.141592653589793

random.seed(1)
print(random.choice(["heads", "tails"]))   # a repeatable coin flip
