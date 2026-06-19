"""@staticmethod and @classmethod.

Run me:  python 03_static_and_classmethods.py
"""

class Temperature:
    @staticmethod
    def c_to_f(celsius):          # no self — just a related helper
        return celsius * 9 / 5 + 32

    @classmethod
    def freezing(cls):            # cls is the class itself
        return cls.c_to_f(0)

print(Temperature.c_to_f(100))   # 212.0
print(Temperature.freezing())    # 32.0
