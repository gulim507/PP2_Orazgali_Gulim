import re

text = "Hello World Python apple"

result = re.findall(r"[A-Z][a-z]+", text)

print(result)