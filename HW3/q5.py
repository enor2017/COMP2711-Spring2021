# This is a program to verify the answer of question 5.
for x in range(0, 137):
    for y in range(0, 137):
        if (21 * x + 18 * y) % 137 == 13 and \
            (32 * x + 15 * y) % 137 == 9:
            print("x = " + str(x) + ", y = " + str(y))