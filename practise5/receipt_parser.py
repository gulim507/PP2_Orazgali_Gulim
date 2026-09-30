import re

with open("raw.txt", "r") as file:
    text = file.read()

prices = re.findall(r"x ([\d ]+,\d{2})", text)

products = re.findall(r"\d+\.\n(.+)", text)

total = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)

date_time = re.search(r"Время: (.+)", text)

payment = re.search(r"(Банковская карта):", text)

print("RECEIPT INFORMATION")
print("-------------------")

print("Products:")
for product in products:
    print("-", product)

print("\nPrices:")
for price in prices:
    print("-", price)

print("\nTotal:", total.group(1))
print("Date and time:", date_time.group(1))
print("Payment method:", payment.group(1))