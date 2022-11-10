print("Task one")

"""Without using any string methods, try to print the following:

( 123...n ) as string without spaces, whare n is a given input."""

a_given_input = int(input("please enter any given number:"))
for i in range(1, a_given_input + 1):
    print(i, end=" ")

"""Check if element exists in list in Python

list = test_list = [1, 6, 3, 5, 3, 4]

Input: 3 # Check if 3 exist or not.

Output: True"""
print("")
print("Task tow")

test_list = [1, 6, 3, 5, 3, 4]
if 3 in test_list:
    print(True)
else:
    print(False)

print("")
print("Task Three")

"""Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]

Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]

Output : [3, 2, 1]"""
hi = input("Enter a list element separated by space ")
original_list  = hi.split()

l = original_list.copy()
l[-1] = l[0]
l[0] = original_list[-1]
print(l)

print("")
print("Task five")

"""We are given a string and we need to reverse words of a given string

Examples:

Input : str =" geeks quiz practice code"

Output : str = code practice quiz geeks"""

input_string = input("Enter family members separated by space ")
our_func  = input_string.split(" ")
str = our_func[::-1]
print(str)

print("")
print("Task Six")
"""Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .

Examples :

Input : geeksforgeeks

Output : Not Accepted

All vowels except 'a','i','u' are not present
Input : ABeeIghiObhkUul

Output : Accepted

All vowels are present"""
vowels = set("aeiou")
input_method = (input("please inter the text").upper())
if vowels in set(input_method):
    print("Accepted")
else:
    print("Not Accepted")

print("")
print("Task Seven")

"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 65432*1 which is 720.

We are given n to calculate its factorial.

Given a character, we need to print its ASCII value

Examples :

Input : a

Output : 97

Input : D

Output : 68

NOTE: search about the ord() method to can solve these problem.
"""
A_letter = input("please enter A letter")
A_letter = A_letter.upper()
our_func2 = ord(A_letter)
print(our_func2)

print("")
print("Task Eight")
"""Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4

Output : 30"""

integer1 = 0
integer2 = int(input("please consider typing an input"))
for i in range(integer2):
    n = i**2
    i += 1