import random

binary_number = ''.join(random.choices('01', k=4))
decimal_number = int(binary_number, 2)

print("Random binary number:", binary_number)
print("Converted to base 10:", decimal_number)