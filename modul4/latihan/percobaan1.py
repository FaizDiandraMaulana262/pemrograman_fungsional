def perkalian(a):
    def dengan(b):
        return a * b 
    return dengan

# Currying
print(perkalian(10)(5))

# HOF
kalikan = perkalian(10)
dengan = kalikan(5)

print(dengan)