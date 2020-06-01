# Reverse The Number

'''
If an Integer N, write a program to reverse the given number.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the reverse of the given number N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input
4
12345
31203
2123
2300
Output
54321
30213
3212
32
'''

# cook your dish here
T = int(input())
for row in range(T):
	s = input()
	while s[-1] == '0':
		s=s[:-1]
	print(s[::-1])
