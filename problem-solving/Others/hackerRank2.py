"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score."""

arr = [2, 3, 6, 6, 6, 5]
arr = sorted(arr)
print(arr)
i = 0
n = 6
x = 2
for i in range(n):
    if arr[n-x] != arr[n-(x-1)]:
        print("Ans: ", arr[n-x])
        break
    else:
        x = x+1
        print(x)
