import re

text = "helloWorldPython"

result = re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()

print(result)