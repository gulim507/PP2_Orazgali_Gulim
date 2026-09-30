import re

text = "My phone number is 12345"

result = re.findall(r"\d+", text)

print(result)