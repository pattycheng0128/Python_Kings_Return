# intersection_update
A = {"apple", "banana", "pineapple"}
B = {"apple", "banana", "grape"}
C = {"orange", "strawberry", "banana"}
# A將是A和B的交集
ret_value = A.intersection_update(B)
print(ret_value)
print(A)
print(B)

# A將是A，B和C的交集
ret_value = A.intersection_update(B, C)
print(ret_value)
print(A)
print(B)
print(C)

