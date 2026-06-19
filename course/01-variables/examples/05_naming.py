"""Naming rules (must-follow) and conventions (should-follow).

Run me:  python 05_naming.py
"""

# RULES — break these and Python raises an error:
#   * must start with a letter or underscore (not a digit)
#   * can contain letters, digits, underscores — nothing else
#   * are case-sensitive: total and Total are different names

user_name = "Sam"      # good: snake_case for normal variables
_internal = 42         # legal: a leading underscore is allowed

# CONVENTIONS — Python still runs, but the community frowns if you ignore them:
MAX_SCORE = 100        # UPPER_CASE signals "treat me as a constant"

print(user_name, _internal, MAX_SCORE)

# These would be ERRORS. Uncomment a line to see Python complain:
# 2cats = 10        # SyntaxError: can't start with a digit
# user-name = 10    # SyntaxError: hyphen is not allowed
# print(User_name)  # NameError: it's user_name, not User_name (case matters)
