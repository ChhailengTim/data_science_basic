wieght1, price1 = eval(input("Enter wieght and price: "))
wieght2, price2 = eval(input("Enter wieght and price: "))

package1 = price1 / wieght1
package2 = price2 / wieght2


if package1 > package2:
    print(f"Package 2 has the better price.")
elif package1 < package2:
    print(f"Package 1 has the better price.")
else:
    print(f"Both packages have the same price.")