from ecc import FieldElement

a = FieldElement(7,13)
b = FieldElement(6,13)

print(a==b)
print(a==a)

print(a+b)
print(a-b)
