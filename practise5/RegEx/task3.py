import re

text = "hello_world test_text Python_code"

result = re.findall(r"[a-z]+_[a-z]+", text)

print(result)