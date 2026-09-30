import re

text = "The rain in Spain"

result = re.search(r"\bS\w+", text)

if result:
    print(result.span())
else:
    print("Not found")