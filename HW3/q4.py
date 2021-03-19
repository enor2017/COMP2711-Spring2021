# This is a program to verify the answer of question 4.
def fast_power(a, b, c):  # calc a^b % c
    ans = 1
    a = a % c
    while b:
        if b & 1:
            ans = (ans * a) % c
        a = (a * a) % c
        b = b >> 1
    return ans

print(fast_power(8, 1027, 22))