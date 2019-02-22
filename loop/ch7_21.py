print("test-1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=", ")
print()
print("test-2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=", ")