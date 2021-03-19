# This is a program to verify the answer of question 1.
for a in range(0, 42):
    for b in range(0, 42):
        if 32 * b - 21 * a == 19:
            print("a = " + str(a) + ", b = " + str(b))