# gdc algo to find the greatest common divisor
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def euclidalg(p, q):
    if q == 0:
        return p
    else:
        return euclidalg(q, p % q)


def lcm(m, n):
    return (m * n) / gcd(m, n)


print("lcm: ", lcm(4, 5))
print("lcm: ", lcm(15, 12))
print("lcm: ", lcm(15, 18))
print("lcm: ", lcm(15, 24))
print("lcm: ", lcm(18, 24))
print("lcm: ", lcm(54, 36))
print("lcm: ", lcm(54, 12))
