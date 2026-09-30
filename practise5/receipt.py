import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Find products, quantity and unit price
pattern = r"(\d+)\.\s*\n(.+?)\n(\d+,\d{3})\s+x\s+([\d ]+,\d{2})"

matches = re.findall(pattern, text)

items = []

for number, name, quantity, price in matches:
    quantity = float(quantity.replace(",", "."))
    price = float(price.replace(" ", "").replace(",", "."))

    items.append({
        "name": name.strip(),
        "quantity": quantity,
        "price": price
    })


# Calculate total
total = sum(item["quantity"] * item["price"] for item in items)


# Find date and time
date_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})", text)
time_match = re.search(r"Время:.*?(\d{2}:\d{2}:\d{2})", text)

date = date_match.group(1) if date_match else ""
time = time_match.group(1) if time_match else ""


# Find payment method
payment_match = re.search(
    r"Банковская карта:\s*\n([\d ]+,\d{2})",
    text
)

payment_method = "Банковская карта" if payment_match else ""


# Create result
result = {
    "date": date,
    "time": time,
    "items": items,
    "total": round(total, 2),
    "payment_method": payment_method
}


print(json.dumps(result, ensure_ascii=False, indent=4))