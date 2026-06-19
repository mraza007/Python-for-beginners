"""Creating strings with different quotes, and measuring them.

Run me:  python 01_creating_strings.py
"""

single = 'Hello'
double = "Hello"            # single and double quotes both work
sentence = "It's fine"     # double quotes let the text contain an apostrophe

paragraph = """This string
spans multiple lines."""   # triple quotes preserve line breaks

print(single)
print(sentence)
print(paragraph)
print(len(single))         # 5  -> number of characters
