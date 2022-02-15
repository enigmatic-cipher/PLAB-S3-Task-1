"""
Task (1.1): Create a function named evenOdd that takes an integer n as input and print whether n is an even number or an odd number.
Task (1.2): Use evenOdd function from Task 1.1 to print even/odd for each element in the list. [10,9,12,5,7]
"""

def even_odd(n):
  if n%2==0:
    return "Even"
  else:
    return "Odd"

ls = [10,9,12,5,7]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  print(f"{e}: {even_odd(e)}")