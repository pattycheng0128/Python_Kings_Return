# | 交集union
math = {"Kevin", "Lily", "Lulu"}
physics = {"Lulu", "Peter", "John"}
allmember = math | physics
print(allmember)

# 也可直接用union
AorB = math.union(physics)
print(AorB)