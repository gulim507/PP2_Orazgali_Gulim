import re

text = "hello"

result = re.search(r"^hello$", text)

if result:
    print("Match")
else:
    print("No match")