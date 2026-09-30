import re

text = "HELLO hello Hello"

result = re.findall(r"hello", text, re.IGNORECASE)

print(result)