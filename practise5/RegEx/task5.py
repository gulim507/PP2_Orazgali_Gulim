import re

text = "The rain in Spain"

result = re.search(r"Spain", text)

if result:
    print("Found:", result.group())
else:
    print("Not found")