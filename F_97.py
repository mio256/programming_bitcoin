def mul_f(a, b):
    return (a * b) % 97


def pow_f(a, b):
    return (a**b) % 97


print(mul_f(mul_f(95, 45), 31))
print(mul_f(mul_f(17, 13), mul_f(19, 44)))
print(mul_f(pow_f(12, 7), pow_f(77, 49)))
