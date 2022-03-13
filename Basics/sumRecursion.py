def sum(n):
    if n == 0:
        return 0
    return sum(n-1)+n


totalSum = sum(5)
print(f"Summation= {totalSum}")
# Logic
'''
we need to find sum of n numbers
1+2+3+4+......n
we can write this as 
1+2+3+4+....(n-2)+(n-1)+n
that is: Sum= Sum(n-1) + n
Your base case will be n = 0, return 0 and close the recursion
'''
