# 差集different
math = {"Kevin", "Lily", "Lulu"}
physics = {"Lulu", "Peter", "John"}

math_only = math - physics
print("只參加數學夏令營:", math_only)

physics_only = physics - math
print("只參加物理夏令營:", physics_only)

# 也可直接用different
math_only = math.difference(physics)
print(math_only)

physics_only = physics.difference(math)
print(physics_only)