'''
not operator
'''
# a = True
# b = False
# print(f"a={a} and b={b}")
# print(f"not a= {not a}, not b={not b}")
# print(f"a and (not b)= {a and not b}")

'''
Bitwise operators
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111.
'''
x = 10        # 0000 1010
y = 4         # 0000 0100
# x xor y =   # 0000 1110
# ----------------------------------
# 0 xor 0 = 0
# 1 xor 0 = 1 (odd number of 1(s))
# 1 xor 1 = 0 (even number of 1(s))
# ----------------------------------
# Bitwise AND
# print(x & y)

# Bitwise OR
# print(x | y)

# Bitwise NOT
# print(~x)

# Bitwise XOR
# print(x ^ y)

# Bitwise left and right shift
# Left Shift
print("\nBitwise Left Shift")
x = 7
print(f"value of x= {x}")  # 00000111
x = x << 1
# 00001110
print(
    f"value of 7 after left shifting it by 1= {x}\nThis is nothing but 7 * 2 as we left shifted by 1")
x = x << 3
# 01110000
print(
    f"After left shifting x=14 by 3, the x= {x}\nThis is nothing but 14 *2*2*2 as we left shifted by 3")

# Right Shift
print("\nBitwise Right Shift")
y = 192
print(f"value of y= {y}")  # 11000000
y = y >> 1
# 00001110
print(
    f"value of 192 after right shifting it by 1= {y}\nThis is nothing but 192/2 as we right shifted by 1")
y = y >> 2
# 01110000
print(
    f"After right shifting y=96 by 2, the y= {y}\nThis is nothing but (96/2)/ 2 as we right shifted by 2")
+
# Identity Operator
p = 5
q = 6
z = 1
print(p is q)
print(z is True)
