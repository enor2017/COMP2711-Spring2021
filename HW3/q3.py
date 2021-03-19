# This is a program to verify the answer of question 3.
for x in range(0, 9 * 14 * 5):
    if (x % 9 == 4) and (x % 14 == 8) and (x % 5 == 3):
        print("x = " + str(x))