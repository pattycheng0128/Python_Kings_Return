#遞迴函數
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*(factorial(n-1)))

value = 3
print(factorial(value))
value = 5
print(factorial(value))
value = 1
print(factorial(value))