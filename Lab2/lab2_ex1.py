kilograms = [1, 3, "...", 197, 199]
pounds = [2.2, 6.6, "...", 433.4, 437.8]
print(f"{'Kilograms':<15} {'Pounds':<10}")
print("-" * 25)

for kg, lb in zip(kilograms, pounds):
    print(f"{kg:<15} {lb:<10}")
