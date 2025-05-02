from mulitply import multiply


def main(c, d):
    result = multiply(c, d)
    print(f"The product of {c} and {d} is {result}")

num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter another number: "))
main(num1, num2)

