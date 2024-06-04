# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:07:05 2024

@author: USER
"""

# Problem Description 
# You are given two numbers A and B.
# You have to add them without using arithmetic operators and return their sum.
# Problem Constraints
# 1 <= A, B <= 109
# Input Format
# The first argument is the integer A. The second argument is the integer B.

# Output Format
# Return a single integer denoting their sum.



# Example Output
# Output 1:
# 13
# Output 2:

# 7


# Example Explanation
# Explanation 1:
# 3 + 10 = 13
# Explanation 2:

# 6 + 1 = 7.
# Note, you have to add without using arithmetic operators.

def addNumbers(A, B):
    while (B > 0):
        common_bit = A & B
        A ^= B
        B = common_bit << 1
    return A
    
# Example Input
# Input 1:
A = 3
B = 10
# Input 2:
A = 6
B = 1

A = 452887384
B = 989233850
addNumbers(A, B)


# # C++
# int Solution::addNumbers(int A, int B) {
#     while (B != 0) {
#         int carry = A & B;
#         A = A ^ B;
#         B = carry << 1;
#     }
#     return A;
# }

# GO
# /**
#  * @input A : Integer
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# func addNumbers(A int , B int )  (int) {
#     var C int
#     for B!=0 {
#         C = A&B;
#         A = A^B;
#         B = C << 1;
#     }
#     return A;
# }
