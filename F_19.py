def mul_f(a, b):
    return (a * b) % 19


k1 = []
for i in range(0, 18):
    k1.append(mul_f(1, i))
print(k1)

k3 = []
for i in range(0, 18):
    k3.append(mul_f(3, i))
print(k3)

k7 = []
for i in range(0, 18):
    k7.append(mul_f(7, i))
print(k7)

k13 = []
for i in range(0, 18):
    k13.append(mul_f(13, i))
print(k13)

k18 = []
for i in range(0, 18):
    k18.append(mul_f(18, i))
print(k18)
