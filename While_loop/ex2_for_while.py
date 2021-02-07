def multiplication_while():
    number = range(0, 14)
    x = 12
    while number[x] > 0:
        print(" [ " + str(number[x]) + " ] ")
        i = 1
        while number[i] < 13:
            print(
                str(number[x])
                + " * "
                + str(number[i])
                + " = "
                + str(number[x] * number[i])
            )
            i += 1
        print("-------------------\n")
        x -= 1


def multiplication_for():
    for number in range(12, 0, -1):
        print(" [ " + str(number) + " ] ")
        for number1 in range(1, 13):
            print(str(number) + " * " + str(number1) + " = " + str(number * number1))
        print("-------------------\n")


multiplication_while()
multiplication_for()
