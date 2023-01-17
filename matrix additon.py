# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:59:22 2023

@author: Aryaman Kumar
"""

matrix1=[[j for j in range (3)] for i in range (3)]
print("Matrix 1")
for i in range(len(matrix1)):
    print(matrix1[i])
matrix2=[[x for x in range(3)] for y in range(3)]
print("Matrix2")
for i in range(len(matrix2)):
    print(matrix2[i])
result1=[[matrix2[j][i]+matrix1[j][i] for i in range(len(matrix1))]for j in range(len(matrix2))]
print("On adding")
for i in range(len(result1)):
  print(result1[i])
result2=[[sum(a * b for a, b in zip(matrix1_row, matrix2_col))for matrix2_col in zip(*matrix2)]for matrix1_row in matrix1]
print("On multiplying")
for r in result2:
    print(r)
