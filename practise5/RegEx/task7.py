import re

text = "Hello World Python"

result = re.sub(r"\s", "_", text)

print(result)