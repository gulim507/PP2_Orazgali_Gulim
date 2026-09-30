import re

text = "a123b"

result = re.fullmatch(r"a.*b", text)

if result:
    print("Match")
else:
    print("No match")