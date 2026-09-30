import re

text = "Hello World Python 123"

result = re.findall(r"[A-Z][a-z]+", text)

print(result)