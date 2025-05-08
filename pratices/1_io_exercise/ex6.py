# # read test.txt
# with open('/Users/newmac/Large File/Leng\'s Docs/Python_DS/pratices/io_exercise/test.txt', "r") as fp:
#     lines = fp.readlines()

# # open new file in write mode
# with open("new_file.txt", "w") as fp:
#     count = 0
#     # iterate each lines from a test.txt
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
#             # write current line
#             fp.write(line)
#         # in each iteration reduce the count
#         count += 1
