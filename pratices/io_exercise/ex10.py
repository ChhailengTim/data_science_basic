# read file
with open('/Users/newmac/Large File/Leng\'s Docs/Python_DS/pratices/io_exercise/test.txt', "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])