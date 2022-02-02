"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
"""


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count


# run --
# 0 - 2 : ABC
# 1 - 3 : BCD
# 2 - 4 : CDS +1
# 3 - 5 : DSX
# 4 - 6 : SXY
# 5 - 7 : XYZ
# 6 - 8 : YZC
# 7 - 9 : ZCD
# 8 - 10 : CDS +1
string = input("Enter a string: ")
subString = input("Enter a substring: ")
print("length of string: ", len(string))
print("length of sub string: ", len(subString))
print("i will run till: ", (len(string)-len(subString)+1)-1)
count = count_substring(string, subString)
print(count)
